#import matplotlib.pyplot as plt
import numpy as np

def validation():

	##########################################################################
	##			Load First File 				##
	
	file_name = 'data_dev.txt'
	file = open(file_name, 'r')

	lists = []
	for line in file.readlines():
		fname = line.rstrip().split(',') #using rstrip to remove the \n
		lists.append(fname)
	
	##########################################################################
	##			Load Second File 				##

	file_name = 'data_check.txt'
	file = open(file_name, 'r')

	lists2 = []
	for line in file.readlines():
		fname2 = line.rstrip().split(',') #using rstrip to remove the \n
		lists2.append(fname2)
	
	##########################################################################
	##		First take values from frist file 			##
	##									##
	##########################################################################

	x = []
	y = []
	z = []
	det = []
	num = []#2194

	init_x = []
	init_y = []
	init_z = []

	obj = {}
	for t in range(10000):
    		obj['evt'+str(t)] = {'x':[],'y':[],'z':[],'det':{}}
	v = 0
	print(len(lists))
	print(len(lists2))
	for i in range(len(lists)):
    		if '=' not in lists[i][0]:
        		if i == 0: 
            			init_x.append(float(lists[0][0]))
            			init_y.append(float(lists[0][1]))
            			init_z.append(float(lists[0][2]))
        		#Pre
        		x.append(float(lists[i][0]))
        		y.append(float(lists[i][1]))
        		z.append(float(lists[i][2]))
        		#Post
        		x.append(float(lists[i][3]))
        		y.append(float(lists[i][4]))
        		z.append(float(lists[i][5]))
        		det.append(lists[i][7])
        		det.append(lists[i][8])
    		elif '=' in lists[i][0] and v < 900:
        		num.append(lists[i][0])
        		obj['evt'+str(v)]['x'] = x
        		obj['evt'+str(v)]['y'] = y
        		obj['evt'+str(v)]['z'] = z
        		obj['evt'+str(v)]['det'] = det
        		x = []
        		y = []
        		z = []
        		det = []
        		v+=1
        		#print(v)
        		#print(v)
        		if (i+1) < (len(lists)):
            			if '=' not in lists[i+1][0]:
                		#print(i)
                			init_x.append(float(lists[i+1][0]))
                			init_y.append(float(lists[i+1][1]))
                			init_z.append(float(lists[i+1][2]))

	##########################################################################
        ##              First take values from second file                      ##
        ##                                                                      ##
        ##########################################################################

	x2 = []
	y2 = []
	z2 = []
	det2 = []
	num2 = [] #2194
	init_x2 = []
	init_y2 = []
	init_z2 = []

	obj2 = {}
	for t in range(10000):
		obj2['evt'+str(t)] = {'x':[],'y':[],'z':[],'det':{}}
	v = 0
	for i in range(len(lists2)):
		if '=' not in lists2[i][0]:
			if i == 0:
				init_x2.append(float(lists2[0][0]))
				init_y2.append(float(lists2[0][1]))
				init_z2.append(float(lists2[0][2]))
        		#Pre2
			x2.append(float(lists2[i][0]))
			y2.append(float(lists2[i][1]))
			z2.append(float(lists2[i][2]))
        		#Post
			x2.append(float(lists2[i][3]))
			y2.append(float(lists2[i][4]))
			z2.append(float(lists2[i][5]))

			det2.append(lists2[i][7])
			det2.append(lists2[i][8])
		elif '=' in lists2[i][0] and v <900:
			num2.append(lists2[i][0])
			obj2['evt'+str(v)]['x'] = x2
			obj2['evt'+str(v)]['y'] = y2
			obj2['evt'+str(v)]['z'] = z2
			obj2['evt'+str(v)]['det'] = det2
			x2 = []
			y2 = []
			z2 = []
			det2 = []
			v+=1
        		#print(v)
			if (i+1) < (len(lists2)):
				if '=' not in lists2[i+1][0]:
                			#print(i)
					init_x2.append(float(lists2[i+1][0]))
					init_y2.append(float(lists2[i+1][1]))
					init_z2.append(float(lists2[i+1][2]))
	
	
	##########################################################################
	##			Start Checks					## 	
	##########################################################################
	
	for d in range(len(obj)):
		for i in range(len(obj['evt'+str(d)]['det'])):
			#if obj['evt'+str(d)]['z'][i] != obj2['evt'+str(d)]['z'][i]:
			if abs(obj['evt'+str(d)]['x'][i] - obj2['evt'+str(d)]['x'][i]) > .1:
				print(d,obj['evt'+str(d)]['x'][i],obj2['evt'+str(d)]['x'][i],obj['evt'+str(d)]['det'][i],obj2['evt'+str(d)]['det'][i])
				break		
validation()	
