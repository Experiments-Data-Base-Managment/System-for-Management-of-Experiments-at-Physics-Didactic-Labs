#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import serial
import time

class SerialCommunication:
	
	START = '1'
	
	END = '0'
	
	REQUEST_DURATION = '2'
	
	def __init__(self):
	
		self.channel = serial.Serial('/dev/ttyACM0',9600)
	
		time.sleep(1.8)
		
	
	def send(self, data):
	
		self.channel.write(data)
	
	
	def receive(self, qnt_byte):
	
		self.text = self.channel.read(qnt_byte)
	
		return self.text
	
	
	def close_connection(self):
	
		self.channel.close()
	
	
	def start_arduino(self):
	
		self.send(self.START)
		
	
	def stop_arduino(self):
	
		self.send(self.END)


	def request_duration_experiment(self):
		
		self.send(self.REQUEST_DURATION)
	
	def get_channel(self):
		
		return self.channel


'''
port_serial = SerialCommunication()

port_serial.request_duration_experiment()

while(port_serial.get_channel().in_waiting == 0):
			time.sleep(1)
			
qnt_byte = port_serial.get_channel().in_waiting

duration_of_experiment = port_serial.receive(qnt_byte)

port_serial.get_channel().reset_input_buffer

port_serial.close_connection()

print(qnt_byte)
print(duration_of_experiment)
'''
