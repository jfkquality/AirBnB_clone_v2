#!/usr/bin/env bash
# Setup web static
sudo apt-get update -y
sudo apt-get -y install nginx
sudo mkdir -p /var/www/html
sudo mkdir -p /data/web_static
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/{releases/test,shared)
sudo mkdir -p /data/web_static/{releases/test,shared)
echo "Web-static deployed!" > /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/current /data/web_static/releases/test/
sudo chown -hR ubuntu:ubuntu /data
sudo sed -i '/http {/a \
    \tserver {\
    \t\tlocation /hbnb_static/ {\
      \t\t\talias /data/web_static/current\
    \t\t}\
    \t}
' /etc/nginx/nginx.conf
# sed -i "/http {/a ${location//$'\n' /$'\\\n'}" /etc/nginx/nginx.conf
sudo service nginx restart
