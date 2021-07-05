# python-system-admin
## Reading and Collecting performance Data using SNMP

### Environment:
- Ubuntu 18.04
- python3
### Setup SNMP in Management server and Managed device
- Install snmpd in Ubuntu
```
$ sudo apt-get update
$ sudo apt-get install snmpd
$ sudo apt install snmp
```
- Adjust the ip
``` 
$ nano /etc/snmp/snmpd.conf
```
- Restart the snmpd service
```
$ sudo service snmpd restart
$ sudo service snmpd status
```
- Check snmp and oid
```
$ snmpwalk -v 2c -c public -O e 127.0.0.1
$ snmpwalk -v 2c -c public -O e [host_IP]
```
### Install pysnmp package
```
$ sudo pip3 install pysnmp
$ sudo pip3 install pyasn1
```

### Intall RRDToll to store the data
```
$ sudo apt-get update -y
$ sudo apt-get install -y rrdtool
```

### Create Cronjob with
```
$ crontab -e
$ crontab -l
*/1 * * * * (cd /home/dcn/python-system-admin/chapter1-Collect-data-SNMP; python3 snmp.py > log.txt)
```

### Install Jinja2, flask and run the web app
```
$ pip3 install Jinja2
$ pip3 install flask
$ python3 flask-web.py
```