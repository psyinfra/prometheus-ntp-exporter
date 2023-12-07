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
prometheus_ntp_exporter --web.listen-address :10006 --ntp.servers europe.pool.ntp.org --ntp.version 4
```

This command exports the NTP response data requested from `europe.pool.ntp.org` using NTP version 4,
with the following output:

```text
# HELP ntp_ntplib_error Python ntplib has encountered an error (1=True, 0=False)
# TYPE ntp_ntplib_error gauge
ntp_ntplib_error{server="europe.pool.ntp.org",version="4"} 0.0
# HELP ntp_offset Time offset between the client and server time
# TYPE ntp_offset gauge
ntp_offset{server="europe.pool.ntp.org",version="4"} 0.0011394023895263672
# HELP ntp_delay Round-trip time to transfer the NTP request over the network
# TYPE ntp_delay gauge
ntp_delay{server="europe.pool.ntp.org",version="4"} 0.03658151626586914
# HELP ntp_leap Leap indicator
# TYPE ntp_leap gauge
ntp_leap{server="europe.pool.ntp.org",version="4"} 0.0
```

### Extended usage example
prometheus_ntp_exporter --web.listen-address :10006 --ntp.servers europe.pool.ntp.org --ntp.version 4 --extended

The `--extended` argument adds transmit, receive, originate, and reference timestamp metrics:

```text
# HELP ntp_ntplib_error Python ntplib has encountered an error (1=True, 0=False)
# TYPE ntp_ntplib_error gauge
ntp_ntplib_error{server="europe.pool.ntp.org",version="4"} 0.0
# HELP ntp_offset Time offset between the client and server time
# TYPE ntp_offset gauge
ntp_offset{server="europe.pool.ntp.org",version="4"} 0.0008738040924072266
# HELP ntp_delay Round-trip time to transfer the NTP request over the network
# TYPE ntp_delay gauge
ntp_delay{server="europe.pool.ntp.org",version="4"} 0.05418825149536133
# HELP ntp_leap Leap indicator
# TYPE ntp_leap gauge
ntp_leap{server="europe.pool.ntp.org",version="4"} 0.0
# HELP ntp_tx_time Transmit timestamp in system time
# TYPE ntp_tx_time gauge
ntp_tx_time{server="europe.pool.ntp.org",version="4"} 1.7019662521828747e+09
# HELP ntp_recv_time Receive timestamp in system time
# TYPE ntp_recv_time gauge
ntp_recv_time{server="europe.pool.ntp.org",version="4"} 1.7019662521826444e+09
# HELP ntp_orig_time Originate timestamp in system time
# TYPE ntp_orig_time gauge
ntp_orig_time{server="europe.pool.ntp.org",version="4"} 1.7019662521546764e+09
# HELP ntp_ref_time Reference timestamp in system time
# TYPE ntp_ref_time gauge
ntp_ref_time{server="europe.pool.ntp.org",version="4"} 1.701966210580937e+09
# HELP ntp_dest_time Destination timestamp in system time
# TYPE ntp_dest_time gauge
ntp_dest_time{server="europe.pool.ntp.org",version="4"} 1.701966252209095e+09
```


## Multiple NTP servers
Multiple NTP servers can be specified, but the same NTP version will be used 
for each of them. Example:

```commandline
prometheus_ntp_exporter --ntp.servers europe.pool.ntp.org de.pool.ntp.org --ntp.version 4
```

This will export NTP statistics from both `europe.pool.ntp.org` and `de.pool.ntp.org` using NTP version 4.
