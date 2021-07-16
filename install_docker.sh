#!/bin/bash

echo " ~~~ NOTICE: ~~~ "
echo "This script will curl for docker executables, install them to your machine, and add the current USER to the docker usergroup."
echo "If these sound like things you want to do, run this script with sudo.  Read it first if you want.  Buyer beware."
echo "Executing..."
echo "-----------------"

curl -sSL https://get.docker.com/ | sh
curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
groupadd docker
usermod -aG docker $USER
