# ec

```shell
sudo apt install nginx
sudo apt install supervisor
ssh-keygen
sudo apt install python3-virtualenv
virtualenv -p python3 venv
pip3 install Flask-Admin
pip3 install flask_sqlalchemy
pip3 install gunicorn
sudo vim /etc/supervisor/conf.d/ec.conf
sudo supervisord -c /etc/supervisor/supervisord.conf
/bin/bash start.sh
```