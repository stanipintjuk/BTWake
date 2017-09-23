# BTWake

A simple WoL but with bluetooth.

# Intro

These scripts will make your bluetooth enabled Raspberry Pi send a WoL magic packet to your PC when a bluetooth device (e.i. your phone) is close enough to be detected.

# Installation
This project is a quick hack and designed to work on my raspberry pi. Files and folders referenced in these scripts need to be adjusted if you wish to install it in a different way.

## Clone
Clone project into home folder

## System Dependencies

``` 
apt install etherwake python3-pip python-dev bluetooth libbluetooth-dev 
```

## Python Dependencies
You need to create an environment called 'env' in the project folder and install pybluez.

```
virtualenv -p python3 env
source env/bin/activate
pip install pybluez
```

## Systemd

Open btwake.service, go to the line that starts with `ExecStart`.
Change the first parameter of the `run.sh` script to be the bluetooth address of your bluetooth device, and the second address to your PCs MAC address.

You now need to place this unit file into the correct folder and start it.

```
cp ./btwake.service /lib/systemd/system/btwake.service
sudo chmod 644 /lib/systemd/system/btwake.service
sudo systemct daemon-reload
sudo systemctl enable btwake.service
sudo systemctl start btwake.service
```

## Modifying etherwake permissions

At last you need to allow any user to run etherwake as root.
**WARNING** Doing this is a serious security issue and you really shouldn't be doing this. Me neither for that matter.

```chmod u+s /usr/sbin/etherwake```

