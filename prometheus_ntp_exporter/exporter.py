import logging

import ntplib
from prometheus_client import Summary
from prometheus_client.core import GaugeMetricFamily

from . import EXPORTER_PREFIX


logger = logging.getLogger('prometheus_ntp_exporter')

# Measure collection time
REQUEST_TIME = Summary(
    'ntp_collector_collect_seconds',
    'Time spent to collect metrics from the NTP server')


class NTPExporter:
    def __init__(self, ntp_server, ntp_version):
        self.ntp_server = ntp_server
        self.ntp_version = ntp_version

    @REQUEST_TIME.time()
    def collect(self):
        labels = [self.ntp_server, str(self.ntp_version)]
        c = ntplib.NTPClient()

        try:
            response = c.request(self.ntp_server, version=self.ntp_version)
        except ntplib.NTPException as exc:
            logger.error(f'NTPException({exc})')
            g = GaugeMetricFamily(
                name=f'{EXPORTER_PREFIX}_ntpexception',
                labels=['server', 'version'],
                documentation='NTPException (1 = True, 0 = False)')
            g.add_metric(labels, 1)
            yield g
            return

        g = GaugeMetricFamily(
            name=f'{EXPORTER_PREFIX}_ntpexception',
            labels=['server', 'version'],
            documentation='NTPException (1 = True, 0 = False)')
        g.add_metric(labels, 0)
        yield g

        g = GaugeMetricFamily(
            name=f'{EXPORTER_PREFIX}_offset', labels=['server', 'version'],
            documentation='offset')
        g.add_metric(labels, response.offset)
        yield g

        g = GaugeMetricFamily(
            name=f'{EXPORTER_PREFIX}_delay', labels=['server', 'version'],
            documentation='round-trip delay')
        g.add_metric(labels, response.delay)
        yield g

        g = GaugeMetricFamily(
            name=f'{EXPORTER_PREFIX}_tx_time', labels=['server', 'version'],
            documentation='Transmit timestamp in system time')
        g.add_metric(labels, response.tx_time)
        yield g

        g = GaugeMetricFamily(
            name=f'{EXPORTER_PREFIX}_recv_time', labels=['server', 'version'],
            documentation='Receive timestamp in system time')
        g.add_metric(labels, response.recv_time)
        yield g

        g = GaugeMetricFamily(
            name=f'{EXPORTER_PREFIX}_orig_time', labels=['server', 'version'],
            documentation='Originate timestamp in system time')
        g.add_metric(labels, response.orig_time)
        yield g

        g = GaugeMetricFamily(
            name=f'{EXPORTER_PREFIX}_ref_time', labels=['server', 'version'],
            documentation='Reference timestamp in system time')
        g.add_metric(labels, response.ref_time)
        yield g

        g = GaugeMetricFamily(
            name=f'{EXPORTER_PREFIX}_dest_time', labels=['server', 'version'],
            documentation='Destination timestamp in system time')
        g.add_metric(labels, response.dest_time)
        yield g

        g = GaugeMetricFamily(
            name=f'{EXPORTER_PREFIX}_leap', labels=['server', 'version'],
            documentation='Leap indicator')
        g.add_metric(labels, response.leap)
        yield g
