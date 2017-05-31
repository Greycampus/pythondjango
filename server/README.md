# setting django server using gunicorn and nginx

## Introdution

This tutorial will guide you through set up of a production server for a django user by using wsgi component of python and nginx server.

nginx (pronounced engine-x) is a free, open-source, high-performance HTTP server and reverse proxy, as well as an IMAP/POP3 proxy server.

## Prerequisites

A ubuntu machine(with root privileges) with internet

## Installation of Gunicorn and its configuration

we are directly skipping to installation of gunicorn keeping in mind that, you already set python3 as default, created and tested a sample django project after iinstallation of pip and django.
> **NOTE:** If you didnt do any above steps go to
> - [python installation](../python/README.md)
> - [django installation](../django/README.md)

using pip install gunicorn component of python. uWSGI acts as a bridge between the deployment server and the django application.

```bash
pip install gunicorn
```
Let's test gunicorn's ability to serve the project. We can do this by entering our project directory  and use gunicorn to *WSGI* module
```bash
cd sampleproj
gunicorn --bind 0.0.0.0:8000 sampleproj.wsgi
```
We passed Gunicorn a module by specifying the relative directory path to Django's wsgi.py file, which is the entry point to our application, using Python's module syntax. Inside of this file, a function called *application* is defined, which is used to communicate with the application.you can open the django project without even running server explicitly.

Now Let's  create gunicorn systemd service file

```bash
sudo gedit /etc/systemd/system/gunicorn.service
```
add following lines to opened file.Start with the [Unit] section, which is used to specify metadata and dependencies. We'll put a description of our service here and tell the init system to only start this after the networking target has been reached.[Service] section will specify the user and group that we want to process to run under. We will give our regular user account ownership of the process since it owns all of the relevant files. We'll give group ownership to the www-data group so that Nginx can communicate easily with Gunicorn.Finally, we'll add an [Install] section. This will tell systemd what to link this service to if we enable it to start at boot. We want this service to start when the regular multi-user system is up and running:
```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=raghavendra
Group=www-data
WorkingDirectory=/home/raghavendra/sampleproj
ExecStart=/usr/local/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/raghavendra/sampleproj/sampleproj.sock sampleproj.wsgi:application

[Install]
WantedBy=multi-user.target

```
With that, our systemd service file is complete. Save and close it now.

> **NOTE:** don't forget to change username and project folder as per your creation in files.

We can now start the Gunicorn service we created and enable it so that it starts at boot:

```bash
    sudo systemctl start gunicorn
    sudo systemctl enable gunicorn
```
checking Gunicorn socket file

```bash
sudo systemctl status gunicorn
```
The output should be similar to :

![guni](../assets/guni.png)

f you make changes to the `/etc/systemd/system/gunicorn.service` file, reload the daemon to reread the service definition and restart the Gunicorn process by typing:
```bash
sudo systemctl daemon-reload
sudo systemctl restart gunicorn

```

## installing and Configuring nginx for deployment

install nginx:
```bash
sudo apt-get install nginx
sudo /etc/init.d/nginx start
```
now check that nginx is serving by visiting [localhost](http://localhost/). If its successful, that means that nginx is listening to port 80 and we need to reconfigure it to listen for port 8000.

configure nginx:

Now that Gunicorn is set up, we need to configure Nginx to pass traffic to the process

start by creatting a new server block in Nginx's `site-enabled` directory:

```bash
sudo gedit /etc/nginx/sites-enabled/sampleproj
```
add following lines to the file opened and don't forget to change username and project folder name:
```
server {
    listen 80;
    server_name server_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/raghavendra/sampleproj;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/sammy/myproject/myproject.sock;
    }
}
```
let's configure django to accept the domain specified in `server_name`.  Open *sampleproj/setting.py* from project folder and add host to be accepted.
```python
...
ALLOWED_HOSTS = ['.sampleproj.com','localhost']
...
```
lets test Nginx and restart it.
```bash
sudo nginx -t
sudo systemctl restart nginx
```
now lets edit the hosts file to open the domain specified in the server.
```bash
gedit /etc/hosts
```
add the host below the last line specifying hosts starting with `127.0.0.1`:
```
...
127.0.0.1	sampleproj.com
...
```
Now you should see the specified domain(sampleproj.com in mycase) to view you application:

![oo](../assets/sampr.png)
