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
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
location=$(cat <<EOF

      location /hbnb_static {
        alias /data/web_static/current;
      }
EOF
)
sed -i.bak "/^.\{0\}server {/a ${location//$'\n'/$'\\\n'}" /etc/nginx/sites-available/default
sudo service nginx restart
