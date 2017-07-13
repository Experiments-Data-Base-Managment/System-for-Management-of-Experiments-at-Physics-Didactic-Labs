#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import sys
sys.path.append("../")
from controller.Controller_New_Experiment import ControllerScreenExperiment
from datetime import datetime
from model.Experiment import Experiment
from Window import Main, Gtk

controller = ControllerScreenExperiment()

class WindowNewExperiment:
	
	experiment = ''
	
	def __init__(self, path):
		
		self.window = Main()
				
		self.window.set_handler(controller.get_handler())

		self.window.set_file_ui(path)
		
		self.window.connect_handles_ui()
		
		self.window.set_name_object("main_window")

		controller.set_screen_experiment(self)
		
		self.window.start_window()
		
		self.set_date_view(\
			self.window.get_object_from_window("date"))

		self.set_time_view(\
			self.window.get_object_from_window("time"))
		
		controller.set_id_experiment_view(\
			self.window.get_object_from_window("id_experiment"))
			
	def get_text(self,entry):
		text = entry.get_text()
		return text
		
	def get_textbuffer(self, textbuffer):
		text = textbuffer.get_text(textbuffer.get_start_iter(), textbuffer.get_end_iter(), True) 
		return text	
	
	def set_date_view(self, entry):
		now = datetime.now()		
		entry.set_text((str(now.day) if (now.day >= 10) else '0'+str(now.day))+'/'\
			+(str(now.month) if (now.month >= 10) else '0'+str(now.month))+'/'+str(now.year))

	def convert_format_date_bd(self,entry):
		self.date = entry.split('/')
		return self.date[2] + '-' + self.date[1] + '-' + self.date[0]

	def set_time_view(self, entry):
		now = datetime.now()
		entry.set_text((str(now.hour) if (now.hour >= 10) else '0'+str(now.hour))+':'\
			+(str(now.minute) if (now.minute >= 10) else '0'+str(now.minute))+':'\
				+(str(now.second) if (now.second >= 10) else '0'+str(now.second)))					
	
	def set_experiment(self):
		self.experiment = Experiment(\
			self.window.get_object_from_window("institution").get_text(),\
			self.window.get_object_from_window("course").get_text(),\
			self.window.get_object_from_window("class").get_text(),\
			self.window.get_object_from_window("teacher").get_text(),\
			self.window.get_object_from_window("student").get_text(),\
			self.window.get_object_from_window("experiment").get_text(),\
			self.window.get_object_from_window("id_experiment").get_text(),\
			self.convert_format_date_bd(self.window.get_object_from_window("date").get_text()),\
			self.window.get_object_from_window("time").get_text(),\
			self.window.get_object_from_window("state_city").get_text(),\
			self.get_textbuffer(self.window.get_object_from_window("description").get_buffer()))
		
	def get_experiment(self):
		return self.experiment
			
	def show_window(self):
		Gtk.main()
