#!/usr/bin/env bash
# Script that configures Nginx server with some folders and files
# Install Nginx if it is not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create necessary folders if they do not already exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo chown -R ubuntu:ubuntu /data/

# Create a fake HTML file for testing purposes
echo "<html>
  <head>
    <title>Testing Nginx configuration</title>
  </head>
  <body>
    <p>This is a test page.</p>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link to the /data/web_static/releases/test/ folder
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Update the Nginx configuration file to serve /data/web_static/current/
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
