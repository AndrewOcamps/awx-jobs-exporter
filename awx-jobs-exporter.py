import time
import os
import argparse
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import start_http_server
from app.main import stats_job_templates

parser = argparse.ArgumentParser(description='Ansible AWX jobs Status for Prometheus')
parser.add_argument('--config', default='configuration.yml', help='Path for configuration file.')
parser.add_argument('--listen-address', default='9091', type=int, help='Address on which to expose metrics and web interface.')

args = parser.parse_args()

class CustomCollector(object):
    def __init__(self):
      pass

    def collect(self):
      g = GaugeMetricFamily("awx_jobs_status", 'Ansible AWX jobs Status', labels=['awx_job_id','awx_job_name', 'awx_username', 'awx_launch_type'])
      for result in stats_job_templates(args.config):
        g.add_metric([str(result[0]),str(result[1]),str(result[2]),str(result[3])], result[4])
      yield g

if __name__ == '__main__':
    start_http_server(args.listen_address)
    REGISTRY.register(CustomCollector())
    while True:
        time.sleep(1)


