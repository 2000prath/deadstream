#!/bin/bash

sudo cp timemachine.service /etc/systemd/system/.
sudo cp connect_network.service /etc/systemd/system/.
sudo chmod 644 /etc/wpa_supplicant/wpa_supplicant.conf
sudo chown root /etc/wpa_supplicant/wpa_supplicant.conf
sudo chgrp root /etc/wpa_supplicant/wpa_supplicant.conf

sudo systemctl daemon-reload
sudo systemctl enable timemachine.service 
sudo systemctl enable connect_network.service

# since this is version 2 branch of the code, make sure that the board is a version 2 board. 
# If it is not a v2 board, then make it one by adding the gpio-shutdown command.
#
version=`$HOME/deadstream/bin/board_version.sh | awk '/version/ {print $2}'`
if [ $version -ne "2" ]; then
  echo 'sudo echo "dtoverlay=gpio-shutdown" >> /boot/config.txt'
  sudo bash -c 'echo "dtoverlay=gpio-shutdown" >> /boot/config.txt'
fi

exit 0
