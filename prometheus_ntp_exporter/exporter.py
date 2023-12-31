import logging

import ntplib
from prometheus_client import Summary
from prometheus_client.core import GaugeMetricFamily

from . import EXPORTER_PREFIX


logger = logging.getLogger('prometheus_ntp_exporter')

# Measure collection time
REQUEST_TIME = Summary(
    f'{EXPORTER_PREFIX}_collector_collect_seconds',
    'Time spent to collect metrics from the NTP server')


class NTPExporter:
    def __init__(
            self, ntp_servers: list[str], ntp_version: int,
            extended: bool = False):
        self.ntp_servers = ntp_servers
        self.ntp_version = ntp_version
        self.extended = extended

    @REQUEST_TIME.time()
    def collect(self):
        c = ntplib.NTPClient()

        for ntp_server in self.ntp_servers:
            labels = [ntp_server, str(self.ntp_version)]
            try:
                response = c.request(ntp_server, version=self.ntp_version)
            except ntplib.NTPException as exc:
                response = None
                logger.error(f'NTPException({exc})')

            g = GaugeMetricFamily(
                name=f'{EXPORTER_PREFIX}_ntplib_error_info',
                labels=['server', 'version'],
                documentation=(
                    'Python ntplib has encountered an error (1=True, '
                    '0=False)'))

            if response is None:
                g.add_metric(labels, 1)
                yield g
                return
            else:
                g.add_metric(labels, 0)
                yield g

            g = GaugeMetricFamily(
                name=f'{EXPORTER_PREFIX}_offset_seconds',
                labels=['server', 'version'],
                documentation=(
                    'Time offset between the client and server time'))
            g.add_metric(labels, response.offset)
            yield g

            g = GaugeMetricFamily(
                name=f'{EXPORTER_PREFIX}_delay_seconds',
                labels=['server', 'version'],
                documentation=(
                    'Round-trip time to transfer the NTP request over the '
                    'network'))
            g.add_metric(labels, response.delay)
            yield g

            g = GaugeMetricFamily(
                name=f'{EXPORTER_PREFIX}_leap_info',
                labels=['server', 'version'],
                documentation='Leap indicator')
            g.add_metric(labels, response.leap)
            yield g

            if self.extended:
                g = GaugeMetricFamily(
                    name=f'{EXPORTER_PREFIX}_tx_time_timestamp_seconds',
                    labels=['server', 'version'],
                    documentation='Transmit timestamp in system time')
                g.add_metric(labels, response.tx_time)
                yield g

                g = GaugeMetricFamily(
                    name=f'{EXPORTER_PREFIX}_recv_time_timestamp_seconds',
                    labels=['server', 'version'],
                    documentation='Receive timestamp in system time')
                g.add_metric(labels, response.recv_time)
                yield g

                g = GaugeMetricFamily(
                    name=f'{EXPORTER_PREFIX}_orig_time_timestamp_seconds',
                    labels=['server', 'version'],
                    documentation='Originate timestamp in system time')
                g.add_metric(labels, response.orig_time)
                yield g

                g = GaugeMetricFamily(
                    name=f'{EXPORTER_PREFIX}_ref_time_timestamp_seconds',
                    labels=['server', 'version'],
                    documentation='Reference timestamp in system time')
                g.add_metric(labels, response.ref_time)
                yield g

                g = GaugeMetricFamily(
                    name=f'{EXPORTER_PREFIX}_dest_time_timestamp_seconds',
                    labels=['server', 'version'],
                    documentation='Destination timestamp in system time')
                g.add_metric(labels, response.dest_time)
                yield g
