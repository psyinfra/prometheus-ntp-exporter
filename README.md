# prometheus-ntp-exporter
A Python-based Prometheus exporter for NTP statistics that sends a request to 
an NTP server using [ntplib](https://github.com/cf-natali/ntplib) and exports 
the response via the Prometheus client.

## Installation
```commandline
git clone git@jugit.fz-juelich.de:inm7/infrastructure/loony_tools/prometheus-ntp-exporter.git
cd prometheus-ntp-exporter
pip install .
```

## Usage

    usage: prometheus_ntp_exporter [-h] [-w LISTEN_ADDRESS] --ntp.server NTP_SERVER --ntp.version NTP_VERSION [-l LOG_LEVEL]
    
    Python-based Prometheus exporter for NTP time offset
    
    optional arguments:
      -h, --help            show this help message and exit
      -w LISTEN_ADDRESS, --web.listen-address LISTEN_ADDRESS
                            Address and port to listen on (default = :9951)
      --ntp.server NTP_SERVER
                            Address of target NTP server
      --ntp.version NTP_VERSION
                            NTP version
      -l LOG_LEVEL, --log LOG_LEVEL
                            Specify logging level

### Example
```commandline
prometheus_ntp_exporter --web.listen-address :9951 --ntp.server europe.pool.ntp.org --ntp.version 3
```

This command exports the NTP response data requested from `europe.pool.ntp.org` using NTP version 3.
