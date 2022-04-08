from app.load_configuration import get_connections, get_jobs
import requests

def get_token(username, password, user_id, url, ssl_verify):
  api_path = '/api/v2/users/{}/personal_tokens/'.format(user_id)
  url = url + api_path
  r = requests.post(url=url, auth=(username,password), verify=ssl_verify)
  token = r.json()['token']
  return token

def get_job_templates(token, url, ssl_verify, id):
    api_path = '/api/v2/job_templates/{}/jobs?order_by=-id'.format(id)
    url = url + api_path
    token = 'Bearer {}'.format(token)
    headers = {'Authorization': token}
    r = requests.get(url=url, headers=headers, verify=ssl_verify)
    if r.status_code == 200:
        job_templates = r.json()

        if len(job_templates['results']) > 0:
          name = job_templates['results'][0]['name']
          if 'created_by' in job_templates['results'][0]['summary_fields']:
            username = job_templates['results'][0]['summary_fields']['created_by']['username']
          if 'schedule' in job_templates['results'][0]['summary_fields']:
            username = 'scheduled'
          launch_type = job_templates['results'][0]['launch_type']
          status = job_templates['results'][0]['status']

          if status == 'successful':
            status = 0
          if status == 'new':
            status = 1
          if status == 'pending':
            status = 2
          if status == 'waiting':
            status = 3
          if status == 'running':
            status = 4
          if status == 'failed':
            status = 5
          if status == 'error':
            status = 6
          if status == 'canceled':
            status = 7

          return id, name.replace(' ','_'), username, launch_type, status
         
def stats_job_templates(config_path):
  configurations = get_connections(config_path)

  username = configurations['username']
  password = configurations['password']
  user_id = configurations['userid']
  url = configurations['url']
  ssl = configurations['ssl_verify']
 
  token = get_token(username, password, user_id, url, ssl)
  list_jobs = get_jobs(config_path)
 
  stats = []
  for job in list_jobs:
    stats.append(get_job_templates(token, url, ssl, job))
  return stats

