# Project version
VERSION = '1.0.0'

# Default port used by the NTP Exporter
DEFAULT_PORT = 9951  # TODO: Change this; doesn't have to be official

# Prefix used for the names of all exported metrics
EXPORTER_PREFIX = 'ntp'

__all__ = [DEFAULT_PORT, EXPORTER_PREFIX, VERSION]
