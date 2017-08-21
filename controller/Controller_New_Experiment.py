#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import sys
import threading
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GObject
sys.path.append('../')
from DAO.New_Experiment_DAO import NewExperimentDAO
from view.Screen_Load_Results import WindowLoadResult
from model.Serial_Communication import SerialCommunication, time
from model.Wait_Screen import WaitScreen
from model.Set_Results import SetResults
 
dao_new_experiment = NewExperimentDAO()

set_results = SetResults()

wait_screen = WaitScreen()

class ThreadMonitoring(threading.Thread):
	
	def __init__(self):	
		
		threading.Thread.__init__(self)	
		
					
	def run(self):
		
		self.start_measurement_experiment()
		
		time.sleep(0.4)
		print "ESSE E O TIME DE DURACAO< FUNCIONA: " + wait_screen.get_duration_experiment()
		
		self.get_measurement_data()


	#recovery total time of duration experiment from arduino and set it in status object			
	def	start_measurement_experiment(self):
		
		self.port_serial = SerialCommunication()

		self.port_serial.request_duration_experiment()

		if(self.port_serial.get_channel().in_waiting == 0 ):
			time.sleep(0.3)
			
		self.qnt_byte = self.port_serial.get_channel().in_waiting

		self.duration_of_experiment = self.port_serial.receive(self.qnt_byte)
		
		self.port_serial.get_channel().flush()
		
		wait_screen.set_duration_experiment(self.duration_of_experiment)
		

	def get_measurement_data(self):
			
		self.port_serial.start_arduino()
		
		self.index = 0
				
		while True:
			
			while(self.port_serial.get_channel().in_waiting < 6):
				time.sleep(0.8)
				
			self.qnt_bytes = self.port_serial.get_channel().in_waiting
			
			self.data = self.port_serial.receive(self.qnt_bytes)
			
			print "ULTIMO PARTE DOS BYTES: " + self.data[self.qnt_bytes-1]
						
			self.port_serial.get_channel().flush()
			
			set_results.add_measurement(self.data)
		
			print set_results.get_measurements()[self.index]
				
			self.split_data(set_results.get_measurements()[self.index])
				
			wait_screen.set_new_fraction(int(self.time_measured[0]))
						
			self.index += 1
			
			if(self.time_measured[0] == wait_screen.get_duration_experiment()):
				
				break
		
	
	def split_data(self, data):
	
		self.time_measured = data.split(';')
	
class Handler:
	
	def __init__(self, controller):
		self.controller = controller
	
	#def on_button_save_clicked(self, button):
	#	print("O Handle Funciona para button_save")
	#	controller.set_values_db(self.screen_experiment)
	#	print("Valores salvos")
	
	def on_button_run_clicked(self, button):
		
		print("O Handle Funciona para button_run")
		
		self.controller.screen_experiment.set_experiment()
		
		thread2 = ThreadMonitoring()
		
		thread2.start()
		
		self.screen_load_result = WindowLoadResult("../view/xml_windows/load_results.glade", wait_screen, set_results)
		
		GObject.timeout_add(1000, self.screen_load_result.get_controller().fill_progress_bar, None)	
		
		self.screen_load_result.show_window()	
	

class ControllerScreenExperiment:			
	
	def __init__(self):
	
		self.handler = Handler(self)
	
	
	def get_handler(self):
	
		return self.handler
	
						
	def set_id_experiment_view(self, entry):
	
		entry.set_text(dao_new_experiment.get_last_id())
	
	
	def get_screen_experiment(self):
		
		return self.screen_experiment
		
		
	def set_screen_experiment(self, screen_experiment):
		
		self.screen_experiment = screen_experiment	
		
		'''
		self.dao_new_experiment.insert_table_experiments(\
			window.get_object_from_window("institution").get_text(),\
			window.get_object_from_window("course").get_text(),\
			window.get_object_from_window("class").get_text(),\
			window.get_object_from_window("teacher").get_text(),\
			window.get_object_from_window("student").get_text(),\
			window.get_object_from_window("experiment").get_text(),\
			window.get_object_from_window("id_experiment").get_text(),\
			self.convert_format_date_bd(window.get_object_from_window("date").get_text()),\
			window.get_object_from_window("time").get_text(),\
			window.get_object_from_window("state_city").get_text(),\
			self.get_textbuffer(window.get_object_from_window("description").get_buffer()))			
		'''
