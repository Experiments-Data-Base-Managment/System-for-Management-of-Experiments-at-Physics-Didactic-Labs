#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GdkPixbuf
		
class Main:				
						
	def __init__(self):
		self.builder = Gtk.Builder()

	def set_handler(self,handlers):
		self.handlers = handlers
				
	def set_file_ui(self, name_file):
		self.name_file = name_file
		self.builder.add_from_file(self.name_file)
	
	def connect_handles_ui(self):
		self.builder.connect_signals(self.handlers)
				
	def set_name_object(self, name_object):
		self.name_object = name_object
		
	def build_window(self):
		self.window = self.builder.get_object(self.name_object)
		self.window.show_all()

	def start_window(self):
		self.build_window()
	
	def get_object_from_window(self, name_object):
		return self.builder.get_object(name_object)
	
	def get_window(self):
		return self.window
