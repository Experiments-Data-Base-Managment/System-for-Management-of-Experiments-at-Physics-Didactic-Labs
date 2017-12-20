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
		
	def set_controller_screen_new_experiment(self, controller_screen_new_experiment):
		self.controller_screen_new_experiment = controller_screen_new_experiment
		
	def get_controller_screen_new_experiment(self):
		return self.controller_screen_new_experiment
	
	def get_handler(self):
		return self.handler

	def fill_experiments_data(self):
		self.get_screen_result_experiment().get_window().get_object_from_window("label_lamp_color").set_text(self.get_controller_screen_new_experiment().get_experiment().get_lamps_color())
		self.get_screen_result_experiment().get_window().get_object_from_window("label_distance").set_text(self.get_controller_screen_new_experiment().get_experiment().get_distance_lamp_photocell())
		self.get_screen_result_experiment().get_window().get_object_from_window("label_photocell").set_text(self.get_controller_screen_new_experiment().get_experiment().get_type_photocell())
		self.get_screen_result_experiment().get_window().get_object_from_window("label_lamp_power").set_text(self.get_controller_screen_new_experiment().get_experiment().get_lamp_power())
		
	
	def fill_table_results(self):
		tau = int(self.get_controller_screen_new_experiment().get_experiment().get_tau())	
				
		for i in range(0, len(self.get_screen_result_experiment().get_set_results().get_measurements())):
			results = self.get_screen_result_experiment().get_set_results().get_measurements()[i].split('|')			
			for j in range (0, len(results)):
				if(results[j].split(';')[0] == str(tau)):
					self.get_controller_screen_new_experiment().get_experiment().set_voltage_capacitor_tau(results[j].split(';')[1])
					break
					
		resistor = self.get_controller_screen_new_experiment().get_experiment().get_resistor()
		capacitor = self.get_controller_screen_new_experiment().get_experiment().get_capacitor()
		temp_color = self.get_controller_screen_new_experiment().get_experiment().get_lamps_color()
		voltage_lamp = self.get_controller_screen_new_experiment().get_experiment().get_lamp_power()
		distance = self.get_controller_screen_new_experiment().get_experiment().get_distance_lamp_photocell()
		voltage_photocell = self.get_controller_screen_new_experiment().get_experiment().get_volt_photocell()
		voltage_capacitor_tau = self.get_controller_screen_new_experiment().get_experiment().get_voltage_capacitor_tau()
		print voltage_capacitor_tau
		self.get_controller_screen_new_experiment().get_experiment().calc_energy_capacitor()
		energy_capacitor = self.get_controller_screen_new_experiment().get_experiment().get_energy_capacitor()
		
		self.get_screen_result_experiment().get_table_results().prepend([int(resistor),float(capacitor), float(tau),temp_color,float(voltage_lamp),distance,float(voltage_photocell),float(voltage_capacitor_tau),float(energy_capacitor)])

		#self.get_screen_result_experiment().get_table_results().prepend()
