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
# HELP ntp_ntplib_error_info Python ntplib has encountered an error (1=True, 0=False)
# TYPE ntp_ntplib_error_info gauge
ntp_ntplib_error_info{server="europe.pool.ntp.org",version="4"} 0.0
# HELP ntp_offset_seconds Time offset between the client and server time
# TYPE ntp_offset_seconds gauge
ntp_offset_seconds{server="europe.pool.ntp.org",version="4"} 0.0016868114471435547
# HELP ntp_delay_seconds Round-trip time to transfer the NTP request over the network
# TYPE ntp_delay_seconds gauge
ntp_delay_seconds{server="europe.pool.ntp.org",version="4"} 0.04280233383178711
# HELP ntp_leap_info Leap indicator
# TYPE ntp_leap_info gauge
ntp_leap_info{server="europe.pool.ntp.org",version="4"} 0.0
```

### Extended usage example
```commandline
prometheus_ntp_exporter --web.listen-address :10006 --ntp.servers europe.pool.ntp.org --ntp.version 4 --extended
```

The `--extended` argument adds transmit, receive, originate, and reference timestamp metrics:

```text
# HELP ntp_ntplib_error_info Python ntplib has encountered an error (1=True, 0=False)
# TYPE ntp_ntplib_error_info gauge
ntp_ntplib_error_info{server="europe.pool.ntp.org",version="4"} 0.0
# HELP ntp_offset_seconds Time offset between the client and server time
# TYPE ntp_offset_seconds gauge
ntp_offset_seconds{server="europe.pool.ntp.org",version="4"} -0.00022172927856445312
# HELP ntp_delay_seconds Round-trip time to transfer the NTP request over the network
# TYPE ntp_delay_seconds gauge
ntp_delay_seconds{server="europe.pool.ntp.org",version="4"} 0.037148475646972656
# HELP ntp_leap_info Leap indicator
# TYPE ntp_leap_info gauge
ntp_leap_info{server="europe.pool.ntp.org",version="4"} 0.0
# HELP ntp_tx_time_timestamp_seconds Transmit timestamp in system time
# TYPE ntp_tx_time_timestamp_seconds gauge
ntp_tx_time_timestamp_seconds{server="europe.pool.ntp.org",version="4"} 1.702035625010663e+09
# HELP ntp_recv_time_timestamp_seconds Receive timestamp in system time
# TYPE ntp_recv_time_timestamp_seconds gauge
ntp_recv_time_timestamp_seconds{server="europe.pool.ntp.org",version="4"} 1.70203562501062e+09
# HELP ntp_orig_time_timestamp_seconds Originate timestamp in system time
# TYPE ntp_orig_time_timestamp_seconds gauge
ntp_orig_time_timestamp_seconds{server="europe.pool.ntp.org",version="4"} 1.7020356249922676e+09
# HELP ntp_ref_time_timestamp_seconds Reference timestamp in system time
# TYPE ntp_ref_time_timestamp_seconds gauge
ntp_ref_time_timestamp_seconds{server="europe.pool.ntp.org",version="4"} 1.7020356088360066e+09
# HELP ntp_dest_time_timestamp_seconds Destination timestamp in system time
# TYPE ntp_dest_time_timestamp_seconds gauge
ntp_dest_time_timestamp_seconds{server="europe.pool.ntp.org",version="4"} 1.702035625029459e+09
```


## Multiple NTP servers
Multiple NTP servers can be specified, but the same NTP version will be used 
for each of them. Example:

```commandline
prometheus_ntp_exporter --ntp.servers europe.pool.ntp.org de.pool.ntp.org --ntp.version 4
```

This will export NTP statistics from both `europe.pool.ntp.org` and `de.pool.ntp.org` using NTP version 4.
