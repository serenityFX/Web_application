sudo /etc/init.d/nginx start
gunicorn -D -b 0.0.0.0:8080 hello:wsgi_application
