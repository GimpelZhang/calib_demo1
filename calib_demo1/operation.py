# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from cmd_str.models import CMD_CONTENT
import os

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
		commandtest='cd ~/catkin_ws/;source ./devel/setup.bash;roslaunch octopus_pgm_map_creator start.launch'
		commandtest='gnome-terminal -x bash -c "'+commandtest+';" &'
		os.system(commandtest)
	return HttpResponse(message)
