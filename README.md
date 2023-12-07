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

    usage: prometheus_ntp_exporter [-h] [-w LISTEN_ADDRESS] [--ntp.servers NTP_SERVERS [NTP_SERVERS ...]]
                                   [--ntp.version NTP_VERSION] [-e] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
    
    Python-based Prometheus exporter for NTP client statistics
    
    optional arguments:
      -h, --help            show this help message and exit
      -w LISTEN_ADDRESS, --web.listen-address LISTEN_ADDRESS
                            Address and port to listen on (default = :10006)
      --ntp.servers NTP_SERVERS [NTP_SERVERS ...]
                            Addresses of one or more target NTP servers
      --ntp.version NTP_VERSION
                            NTP version
      -e, --extended        Export transmit, receive, originate, and reference timestamps in system time
      -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --log {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                            Specify logging level


### Usage example
```commandline
prometheus_ntp_exporter --web.listen-address :10006 --ntp.servers europe.pool.ntp.org --ntp.version 3
```

This command exports the NTP response data requested from `europe.pool.ntp.org` using NTP version 3.

### Output example
```text
# HELP ntp_ntpexception Connection to the NTP server has timed out (1=True, 0=False)
# TYPE ntp_ntpexception gauge
ntp_ntpexception{server="europe.pool.ntp.org",version="3"} 0.0
# HELP ntp_offset offset
# TYPE ntp_offset gauge
ntp_offset{server="europe.pool.ntp.org",version="3"} 0.0030574798583984375
# HELP ntp_delay round-trip delay
# TYPE ntp_delay gauge
ntp_delay{server="europe.pool.ntp.org",version="3"} 0.021947860717773438
# HELP ntp_leap Leap indicator
# TYPE ntp_leap gauge
ntp_leap{server="europe.pool.ntp.org",version="3"} 0.0
```

## Multiple NTP servers
Multiple NTP servers can be specified, but the same NTP version will be used 
for each of them. Example:

```commandline
prometheus_ntp_exporter --ntp.servers europe.pool.ntp.org de.pool.ntp.org --ntp.version 3
```

This will export NTP statistics from both `europe.pool.ntp.org` and `de.pool.ntp.org` using NTP version 3.
