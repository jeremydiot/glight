#!/bin/sh

# python uninstall
sudo pip3 uninstall glight

# service uninstall
sudo /etc/init.d/glight-deamon stop
sudo update-rc.d glight-deamon remove
sudo rm /etc/init.d/glight-deamon
sudo systemctl daemon-reload