# AWX_JOBS_EXPORTER
Exportador de metricas personalizado hecho en Python para monitoreo de jobs del AWX con Prometheus.

Una vez clonado el proyecto debes realizar los siguiente:

- Instalar las librerias:

```
pip3 install -r requirements.txt
```

- Editar el archivo **configuration.yml**
```
---
connections:
  url: 'http://192.168.XX.XX' # IP AWX
  ssl_verify: False
  username: 'user' 
  password: 'passwd'
  userid: X

jobs:
- 1
- 2
- 3
```
- Editar el archivo awx_jobs_exporter.service con los datos necesarios.

- Mover la configuracion de servicio en **/lib/systemd/system**
```
mv ap/awx_jobs_exporter.service /lib/systemd/system/

systemctl daemon-reload

systemctl start awx_jobs_exporter.service

systemctl status awx_jobs_exporter.service

systemctl enable awx_jobs_exporter.service

```

- Verificamos que esté escuchando en el puerto **99091**:
```
netstat -ptnl |grep 9091
```