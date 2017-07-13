#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import sys
import threading
sys.path.append("../")
from Window import Main, Gtk
from controller.Controller_Load_Results import ControllerScreenLoadResult

controller = ControllerScreenLoadResult()


class WindowLoadResult:
	
	def __init__(self, path, wait_screen, set_results):
		
		self.wait_screen = wait_screen
		
		self.set_results = set_results
		
		self.window = Main()
		
		self.window.set_handler(controller.get_handler())

		self.window.set_file_ui(path)
		
		self.window.connect_handles_ui()
		
		self.window.set_name_object("poupup_progress_bar")
		
		controller.set_screen_load_results(self)

		self.window.start_window()
		
		self.window.get_object_from_window("button_screen_results").hide()
	
	def show_window(self):
	
		Gtk.main()
		
	
	def get_controller(self):
	
		return controller
	
		
	def get_progress_bar(self):
	
		return self.window.get_object_from_window("progressbar")
	
	
	def get_window(self):
	
		return self.window
	
	
	def get_wait_screen(self):
		
		return self.wait_screen
		

	def get_set_results(self):
	
		return self.set_results
		
	
	def get_results(self):
		
		return self.set_results
		
'''
windowResult = WindowLoadResult("../view/xml_windows/load_results.glade")

windowResult.show_window()
'''
