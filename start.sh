. venv/bin/activate

#请修改生产环境的监听端口
port=0
env=product

exec gunicorn -b127.0.0.1:${port} --threads=2 -e ENV=${env} run:app

