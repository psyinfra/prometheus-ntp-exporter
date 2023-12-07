# prometheus-ntp-exporter
A Python-based Prometheus exporter for NTP client statistics that sends a 
request to an NTP server using [ntplib](https://github.com/cf-natali/ntplib) 
and exports the response via the Prometheus client.

## Installation
```commandline
git clone git@github.com:psyinfra/prometheus-ntp-exporter.git
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

### Usage example
```commandline
prometheus_ntp_exporter --web.listen-address :9951 --ntp.server europe.pool.ntp.org --ntp.version 3
```

This command exports the NTP response data requested from `europe.pool.ntp.org` using NTP version 3.

### Output example
```text
# HELP ntp_ntpexception NTPException (1 = True, 0 = False)
# TYPE ntp_ntpexception gauge
ntp_ntpexception{server="europe.pool.ntp.org",version="3"} 0.0
# HELP ntp_offset offset
# TYPE ntp_offset gauge
ntp_offset{server="europe.pool.ntp.org",version="3"} 0.003192901611328125
# HELP ntp_delay round-trip delay
# TYPE ntp_delay gauge
ntp_delay{server="europe.pool.ntp.org",version="3"} 0.039783477783203125
# HELP ntp_tx_time Transmit timestamp in system time
# TYPE ntp_tx_time gauge
ntp_tx_time{server="europe.pool.ntp.org",version="3"} 1.7019496886073093e+09
# HELP ntp_recv_time Receive timestamp in system time
# TYPE ntp_recv_time gauge
ntp_recv_time{server="europe.pool.ntp.org",version="3"} 1.701949688607213e+09
# HELP ntp_orig_time Originate timestamp in system time
# TYPE ntp_orig_time gauge
ntp_orig_time{server="europe.pool.ntp.org",version="3"} 1.7019496885841284e+09
# HELP ntp_ref_time Reference timestamp in system time
# TYPE ntp_ref_time gauge
ntp_ref_time{server="europe.pool.ntp.org",version="3"} 1.7019490234449077e+09
# HELP ntp_dest_time Destination timestamp in system time
# TYPE ntp_dest_time gauge
ntp_dest_time{server="europe.pool.ntp.org",version="3"} 1.7019496886240082e+09
# HELP ntp_leap Leap indicator
# TYPE ntp_leap gauge
ntp_leap{server="europe.pool.ntp.org",version="3"} 0.0
```