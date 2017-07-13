#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import sys
sys.path.append('../')
#from DAO.Result_Experiment_DAO import ResultExperimentDAO

class Handler:
	
	def __init__(self, controller):	
		
		self.controller = controller
		
		
	def on_button_save_clicked(self, button):
		
		print("O Handle Funciona para button_save")

		
	def on_button_cancel_clicked(self, button):
		
		print("O Handle Funciona para button_cancel")
		
		#self.serial.stop_arduino()
		
class ControllerScreenResultExperiment:
	
	def __init__(self):
		
		self.handler = Handler(self)
		
	
	def set_screen_result_experiment(self, screen_result_experiment):
		
		self.screen_result_experiment = screen_result_experiment
		
	
	def get_screen_result_experiment(self):
		
		return self.screen_result_experiment
		
	
	def get_handler(self):
		
		return self.handler
