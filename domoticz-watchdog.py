import urllib.parse
import urllib.request
from time import sleep
import os, json

domoticz_ip = '127.0.0.1' #domoticz ip
domoticz_port = 8080 #domoticz HTTP port
request_interval = 30 #time between queries
request_attempts = 5 #number of reconnection attempts
request_attempts_interval = 5 #time between reconnection attempts
request_timeout = 5 #request timeout
wait_for_domoticz = 30 #wait for domoticz

url = 'http://' + str(domoticz_ip) + ':' + str(domoticz_port) +'/json.htm?type=command&param=getversion'

def restart_domoticz():
    try:
        os.system('systemctl restart domoticz')
    except:
        print ('error while restarting domoticz')
    sleep(wait_for_domoticz)

def check_domoticz_status():
    try:
        request = urllib.request.urlopen(url, timeout=request_timeout).read().decode('utf-8')
        if json.loads(request)['status'] == 'OK': return True
        else: return False
    except Exception as e:
        return False

while True:
    if not check_domoticz_status():
        count = 0
        success = False
        sleep(request_attempts_interval)
        while count < request_attempts and not success:
            print("attempt to reconnect")
            if check_domoticz_status(): success = True
            count += 1
            sleep(request_attempts_interval)
            print(count < request_attempts)
        if not success:
            print("restarting domoticz!")
            restart_domoticz()
        else:
            sleep(request_interval) 
    else:
        sleep(request_interval)    
    
