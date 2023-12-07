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

### Usage example
```commandline
prometheus_ntp_exporter --web.listen-address :9951 --ntp.server europe.pool.ntp.org --ntp.version 3
```

This command exports the NTP response data requested from `europe.pool.ntp.org` using NTP version 3.

### Output example
```text
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 341.0
python_gc_objects_collected_total{generation="1"} 28.0
python_gc_objects_collected_total{generation="2"} 0.0
# HELP python_gc_objects_uncollectable_total Uncollectable objects found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 41.0
python_gc_collections_total{generation="1"} 3.0
python_gc_collections_total{generation="2"} 0.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="9",patchlevel="2",version="3.9.2"} 1.0
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 1.792e+08
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 2.0619264e+07
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1.70194968066e+09
# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 0.09
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 6.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1024.0
# HELP ntp_collector_collect_seconds Time spent to collect metrics from the NTP server
# TYPE ntp_collector_collect_seconds summary
ntp_collector_collect_seconds_count 1.0
ntp_collector_collect_seconds_sum 8.909264579415321e-07
# HELP ntp_collector_collect_seconds_created Time spent to collect metrics from the NTP server
# TYPE ntp_collector_collect_seconds_created gauge
ntp_collector_collect_seconds_created 1.701949681426648e+09
# HELP ntp_ntpexception NTPException (1 = True, 0 = False)
# TYPE ntp_ntpexception gauge
ntp_ntpexception{server="europe.pool.ntp.org",version="3"} 0.0
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