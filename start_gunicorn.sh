sudo /etc/init.d/nginx start
gunicorn -D -b 0.0.0.0:8000 ask.wsgi
