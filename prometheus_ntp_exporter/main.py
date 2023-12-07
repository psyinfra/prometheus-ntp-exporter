import argparse
import logging
import time
import urllib.parse

from prometheus_client import start_http_server, REGISTRY

from . import DEFAULT_PORT
from .exporter import NTPExporter


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            'Python-based Prometheus exporter for NTP client statistics'))
    parser.add_argument(
        '-w', '--web.listen-address',
        dest='listen_address',
        required=False,
        type=str,
        default=f':{DEFAULT_PORT}',
        help=f'Address and port to listen on (default = :{DEFAULT_PORT})')
    parser.add_argument(
        '--ntp.servers',
        dest='ntp_servers',
        required=False,
        type=str,
        nargs='+',
        default=['europe.pool.ntp.org'],
        help='Addresses of one or more target NTP servers')
    parser.add_argument(
        '--ntp.version',
        dest='ntp_version',
        required=False,
        type=int,
        default=3,
        help='NTP version')
    parser.add_argument(
        '-e', '--extended',
        dest='extended',
        default=False,
        action='store_true',
        help=(
            'Export transmit, receive, originate, and reference timestamps in '
            'system time'))
    parser.add_argument(
        '-l', '--log',
        dest='log_level',
        required=False,
        type=str,
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        default='WARNING',
        help='Specify logging level')
    return parser.parse_args()


def main():
    args = parse_args()
    logging.basicConfig(
        level=args.log_level,
        format='[%(asctime)s] %(levelname)s: %(message)s')
    logger = logging.getLogger('prometheus_ntp_exporter')
    logger.setLevel(args.log_level)
    logger.info(f'Log level: {logging.getLevelName(logger.level)}')

    try:
        listen_addr = urllib.parse.urlsplit(f'//{args.listen_address}')
        addr = listen_addr.hostname if listen_addr.hostname else '0.0.0.0'
        port = listen_addr.port if listen_addr.port else DEFAULT_PORT
        logger.info(f'Target NTP server(s): {args.ntp_servers}')
        logger.info(f'NTP version: {args.ntp_version}')

        if args.extended:
            logger.info('Exporting extended timestamp data')

        REGISTRY.register(NTPExporter(
            ntp_servers=args.ntp_servers,
            ntp_version=args.ntp_version,
            extended=args.extended))
        start_http_server(port, addr=addr)
        logger.info(f'Listening on {listen_addr.netloc}')
    except KeyboardInterrupt:
        logger.info('Interrupted by user')
        exit(0)
    except Exception as exc:
        logger.error(exc)
        logger.critical(
            'Exporter shut down due while starting the server. Please contact '
            'your administrator.')
        exit(1)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info('Interrupted by user')
        exit(0)
    except Exception as exc:
        logger.error(exc)
        logger.critical(
            'Exporter shut down unexpectedly. Please contact your '
            'administrator.')
        exit(1)
