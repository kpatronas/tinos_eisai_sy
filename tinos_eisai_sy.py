#!/usr/bin/env python3
import os
import sys
from subprocess import PIPE, Popen

def cmd(cmd):
    """
    Execute command and get results
    """
    with Popen(command, stdout=PIPE, stderr=None, shell=True) as process:
        output = process.communicate()[0].decode("utf-8")
    return output[0:-1]

if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except Exception as ex:
        print(str(ex))
        exit(-1)
    sz = int(os.path.getsize(filename))
    command="df -B1 %s | tr -s \" \" | tail -n 1"%(filename)
    partition=cmd(cmd=command)
    used,avail=partition.split()[2:4]
    part=partition.split()[0]
    used=int(used)
    avail=int(avail)
    total=used+avail
    total_perc=round((sz/total)*100,3)
    print('%s,%s,%s(%%),%s'%(filename,sz,total_perc,part))
