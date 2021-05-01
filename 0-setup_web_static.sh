#!/usr/bin/env bash
# This script configures a web server for deployment of web_static.
# Install NginX if it not already installed
apt-get -y update
apt-get -y install nginx
# Allow NginX through the firewall
ufw allow 'Nginx HTTP'
# Listen to port 80

# Create folders if not existing
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
# Create fake HTML file to test.
touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
# Create symbolic link 'current' pointing to 'releases/test'
# If the link exists, remove and create a new one
ln -fs /data/web_static/releases/test/ /data/web_static/current
# Give ownership (recursively) of the data/ folder to the ubuntu user AND group
chown -R ubuntu:ubuntu /data/
# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sed -i '/listen 80 default_server/a location /hbnb_static {\n\talias /data/web_static/current/;\n\tautoindex on;\n}\n' /etc/nginx/sites-available/default
# Restart NginX
service nginx restart
# Always exit successfully
exit 0
