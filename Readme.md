first clone git clone https://github.com/rahult017/cisco_project.git
after that cd cisco_project
source myenv/bin/activate
then install
pip install paramiko
after that pip install requirements.txt
For Question 1
	cd router_cisco
	python manage.py migrate
	create superuser
		python manage.py createsuperuser --username root --email root@example.com
	to generate token for user
		python manage.py drf_create_token root
		python manage.py runserver
 		username root
	 password root

 To Deploy project on Nginx with guincorn on ubuntu 
 sudo apt update
 sudo apt install nginx curl
 pip install django gunicorn
 gunicorn --bind 0.0.0.0:8000 router_ciscp.wsgi
 after that create a file as below
 sudo nano /etc/systemd/system/gunicorn.socket
 and paste below code
 [Unit]
 Description=gunicorn socket

 [Socket]
 ListenStream=/run/gunicorn.sock

 [Install]
 WantedBy=sockets.target
sudo nano /etc/systemd/system/gunicorn.service
copy below code 
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=sammy
Group=www-data
WorkingDirectory=/home/sammy/myprojectdir
ExecStart=/home/sammy/myprojectdir/myprojectenv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          router_cisco.wsgi:application

[Install]
WantedBy=multi-user.target




sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo systemctl status gunicorn.socket
sudo journalctl -u gunicorn.socket
sudo systemctl status gunicorn
sudo systemctl daemon-reload
sudo systemctl restart gunicorn



sudo nano /etc/nginx/sites-available/myproject
and paste below code

server {
    listen 80;
    server_name server_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/sammy/myprojectdir;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}