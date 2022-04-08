import yaml
import os

def load_configuration(config):
  with open(config, 'r') as f:
    configuration = yaml.load(f, Loader=yaml.FullLoader)

  return configuration

def get_connections(config):
  config = load_configuration(config)
  return config['connections']

def get_jobs(config):
  config = load_configuration(config)
  return config['jobs']

