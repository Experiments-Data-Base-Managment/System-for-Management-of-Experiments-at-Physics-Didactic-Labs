#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import sys
sys.path.append('../')
#from view import Screen_Result_Experiment
from view.Screen_Result_Experiment import WindowResultExperiment



class Handler:
		
	def __init__(self, controller_screen_load):

		self.controller_screen_load = controller_screen_load
			
	def on_button_screen_results_clicked(self, button):
		
		print("O Handle Funciona para button_results")			
		
		self.controller_screen_load.get_screen_load_results().window.get_window().destroy()
		
		self.screen_result = WindowResultExperiment("../view/xml_windows/result_experiment.glade", self.controller_screen_load.get_screen_load_results().get_set_results(), self.controller_screen_load.get_controller_screen_new_experiment())
						
		self.screen_result.show_window()
		
class ControllerScreenLoadResult:
	
	def __init__(self):
	
		self.handler = Handler(self)
	
	def get_handler(self):
	
		return self.handler

	
	def set_screen_load_results(self, screen_load_results):
	
		self.screen_load_results = screen_load_results
	
	
	def get_screen_load_results(self):
	
		return self.screen_load_results

					
	def fill_progress_bar(self, user_data):
		
		self.get_screen_load_results().get_progress_bar().set_fraction(self.get_screen_load_results().get_wait_screen().get_actual_fraction())
		
		self.percentage = str(self.get_screen_load_results().get_progress_bar().get_fraction()*100).split('.')
		
		self.get_screen_load_results().get_progress_bar().set_text(self.percentage[0] + '%')
		
		#print "ESTE E O VALOR ATUAL DA BARRA DE STATUS" + str(self.get_screen_load_results().get_progress_bar().get_fraction())
		
		if(self.get_screen_load_results().get_progress_bar().get_fraction() < 1):
			return True
		else:
			self.screen_load_results.get_window().get_object_from_window("button_screen_results").show()
			return False
			
	def set_controller_screen_new_experiment(self, controller_screen_new_experiment):
		self.controller_screen_new_experiment = controller_screen_new_experiment
		
	def get_controller_screen_new_experiment(self):
		return self.controller_screen_new_experiment
