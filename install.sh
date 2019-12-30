#!/bin/bash

echo "Starting domoticz-watchdog install script!"

echo "Copy domoticz-watchdog service"
cp /home/pi/domoticz-watchdog/domoticz-watchdog.service /lib/systemd/system/domoticz-watchdog.service

echo "Daemon reload"
systemctl daemon-reload

echo "Starting service"
systemctl start domoticz-watchdog

echo "Enable service at system start"
systemctl enable domoticz-watchdog

echo "Installation complete!"
