import configparser
import requests
import subprocess
import platform
import datetime
import argparse

parser = argparse.ArgumentParser(description='Auto authentification for IbarakiUniv LAN')
parser.add_argument('-n','--nolog', action='store_true', default=False,
                    help='add no logs to auth-request.log')
parser.add_argument('-a','--all', action='store_true', default=False,
                    help='add logs when ping successed too')
parser.add_argument('-c','--clear', action='store_true', default=False,
                    help='clear auth-request.log then run')
args = parser.parse_args()

inifile = configparser.ConfigParser()
inifile.read('./config.txt', 'UTF-8')

service = inifile.get('default','SERVICE_NAME')
host = inifile.get('default','PING_TARGET')
user = inifile.get('default','USERNAME')
pw = inifile.get('default','PASSWORD')
url = "https://auth.ibaraki.ac.jp/cgi-bin/Login.cgi"

def ping_os_switch():
    pf = platform.system()
    if pf == 'Linux':
        timeout, times = '-W', '-c'
    elif pf == 'Darwin': #Mac
        timeout, times = '-t', '-c'
    elif pf == 'Windows':
        timeout, times = '-W', '-n'
    return ["ping", timeout, "3", times, "1", host]

def is_connected(cmd):
    ping = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    ping.communicate()
    return ping.returncode == 0

def auth_login():
    payload = {"uid":user,"pwd":pw}
    requests.post(url, data=payload)

def write_log(connected):
    dt_now = str(datetime.datetime.now())
    if args.clear == True: a_or_w = "w"
    else: a_or_w = "a"
    with open("auth-request.log", a_or_w) as f:
        if connected == True and args.all == True:
            f.write(dt_now+" Ping to "+host+" successed.\n")
        elif connected == False and args.nolog == False:
            f.write(dt_now+" Ping failed so auth requested.\n")

if __name__ == '__main__':
    pingcmd = ping_os_switch()
    if is_connected(pingcmd) == False:
        write_log(False)
        auth_login()
    elif is_connected(pingcmd) == True:
        write_log(True)
