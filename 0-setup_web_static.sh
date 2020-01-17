#!/usr/bin/env bash
# Setup web static
sudo apt-get update -y
sudo apt-get -y install nginx
sudo mkdir -p /var/www/html
sudo mkdir -p /data/web_static/{releases/test,shared}
cat <<EOF > /data/web_static/releases/test/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF
sudo ln -s /data/web_static/current /data/web_static/releases/test/
sudo chown -hR ubuntu:ubuntu /data

location=$(cat <<EOF
      location /hbnb_static/ {
        alias /data/web_static/current;
      }
EOF
)

sed -i.bak "/^.\{0\}server {/a ${location//$'\n'/$'\\\n'}" /etc/nginx/sites-available/default

# sed -i.bak "/http {/a ${location//$'\n'/$'\\\n'}" /data/web_static/current

# sudo sed -i '/http {/a\
#     \tserver {\
#     \t\tlocation /hbnb_static/ {\
#       \t\t\talias /data/web_static/current\
#     \t\t}\
#     \t}\
# ' /etc/nginx/nginx.conf

# sed -i "/http {/a ${location//$'\n' /$'\\\n'}" /etc/nginx/nginx.conf

sudo service nginx restart
