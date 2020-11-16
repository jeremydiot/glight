#!/bin/sh

# python install
python3 setup.py test
python3 setup.py bdist_wheel
sudo pip3 install ./dist/*.whl

# service install
sudo cp glight-deamon /etc/init.d/.
sudo chmod 0755 /etc/init.d/glight-deamon
sudo systemctl daemon-reload
sudo /etc/init.d/glight-deamon start
sudo update-rc.d glight-deamon defaults
