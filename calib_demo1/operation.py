# -*- coding: utf-8 -*-
import paramiko
from django.http import HttpResponse
from django.shortcuts import render_to_response
from cmd_str.models import CMD_CONTENT
# import os

def world_start(request):
	request.encoding = 'utf-8'
	message = ''
	for key in request.POST:
		if request.POST[key] == '':
			message = '请填写完整信息'
			break
	if 'world_name' in request.POST and message == '':
		message = '你选择了'+str(request.POST['world_name'].encode('utf-8')) + ',你的信息录入完成。谢谢配合~'
		test1 = CMD_CONTENT(world_name = request.POST['world_name'])
		test1.save()
		commandtest="cd calib_demo1/third_party;python3 -c 'import param1_calculation;print(param1_calculation.get_param(2))'"
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ip1 = '10.1.14.135'
		username1 = 'junchuan'
		passwd1='simulation'
		ssh.connect(ip1,22,username1,passwd1,timeout=5)
		stdin, stdout, stderr = ssh.exec_command(commandtest)
		out1=stdout.readlines()
		message=message+out1[0]
		ssh.close()       
	return HttpResponse(message)
# commandtest='cd /home/junchuan/catkin_ws/;source ./devel/setup.bash;roslaunch octopus_pgm_map_creator start.launch'
# commandtest='gnome-terminal -x bash -c "'+commandtest+';" &'