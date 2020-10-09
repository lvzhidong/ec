. venv/bin/activate

#请修改生产环境的监听端口
port=10125
env=product

exec gunicorn -b0.0.0.0:${port} --threads=2 -e ENV=${env} wsgi:app

