import json
import os
from subprocess import Popen,PIPE
SGINQ='/usr/bin/sg_inq'
SGREADCAP='/usr/bin/sg_readcap'
DEV_DIR='/dev/rdsk'
DEV_DIR='/dev/rdsk'
def get_device_details(device):
        DEVPATH=DEV_DIR+'/'+device+'s0'
        line=[SGINQ,DEVPATH,'--page','0xc5','--raw']
        session=Popen(line,stdin=PIPE,stderr=PIPE,stdout=PIPE)
        stdout,stderr=session.communicate()
	if (stderr):
		return False
        details=stdout[4:]
        return(json.loads(details))
def get_device_size(device):
        DEVPATH=DEV_DIR+'/'+device+'s0'
        line=[SGREADCAP,DEVPATH]
        session=Popen(line,stdin=PIPE,stderr=PIPE,stdout=PIPE)
        stdout,stderr=session.communicate()
	if (stderr):
		return False
        size=stdout.strip().split(',')[-1]
        return(size)
def get_devices():
        udevs=[]
        devices=os.listdir(DEV_DIR)
        for dev in devices:
                udev=dev.split('s')[0]
                udevs.append(udev)
        return list(set(udevs))
def device_report(devices):
	print "{0:42} {1:8}\t{2:15} {3:10} {4:10}".format("Device","Size","Volume","Array","Pool")
	print "-"*87
	for device in devices:
		detail=get_device_details(device)
		size=get_device_size(device)
		if  (detail):
			if ( detail['vol'] ):
				name=detail['vol']
			else:
				name="N/A"
			if ( detail['system_name'] ):
				system=detail['system_name']
			else:
				system='N/A'
			if ( detail['pool'] ):
				pool=detail['pool']
			else:
				pool='N/A'
			print "{0:40} {1:>10}\t{2:15} {3:10} {4:10}".format(device,size, name, system, pool)
		
devices=get_devices()
device_report(devices)
