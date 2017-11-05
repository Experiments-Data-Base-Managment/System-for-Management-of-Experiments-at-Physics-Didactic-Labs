#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import sys
sys.path.append("../")
from controller.Controller_New_Experiment import ControllerScreenExperiment
from datetime import datetime
from Window import Main, Gtk

controller = ControllerScreenExperiment()

class WindowNewExperiment:

	'''
		M�todo construtor da tela
	'''
	def __init__(self, path):
		
		self.window = Main()
				
		self.window.set_handler(controller.get_handler())

		self.window.set_file_ui(path)
		
		self.window.connect_handles_ui()
		
		self.window.set_name_object("main_window")

		controller.set_screen_experiment(self)
		
		self.fill_form_fields()
		
		self.window.start_window()
	'''
		M�todo que atribui os valores iniciais de data, hora e n�mero do experimento  
	'''
	def fill_form_fields(self):
			
		self.set_date_view(\
			self.window.get_object_from_window("date"))

		self.set_time_view(\
			self.window.get_object_from_window("time"))
		
		controller.set_id_experiment_view(\
			self.window.get_object_from_window("id_experiment"))
	'''
		M�todo que pega e retorna o texto de um objeto campo do formul�rio
	'''		
	def get_text(self,entry):
		text = entry.get_text()
		return text
	'''
		M�todo que retorna as strings do campo descricao do experimento
	'''	
	def get_textbuffer(self, textbuffer):
		text = textbuffer.get_text(textbuffer.get_start_iter(), textbuffer.get_end_iter(), True) 
		return text	
	'''
		M�todo que atribui a data atual ao campo Data do fomul�rio
	'''
	def set_date_view(self, entry):
		now = datetime.now()		
		
		#
		entry.set_text((str(now.day) if (now.day >= 10) else '0'+str(now.day))+'/'\
			+(str(now.month) if (now.month >= 10) else '0'+str(now.month))+'/'+str(now.year))
	'''
		M�todo que converte a data para o formato aceito pelo banco de dados
	'''
	def convert_format_date_bd(self,entry):
		self.date = entry.split('/')
		return self.date[2] + '-' + self.date[1] + '-' + self.date[0]
	'''
		M�todo que atribui a hora atual ao campo Hora do formul�rio
	'''
	def set_time_view(self, entry):
		now = datetime.now()
		
		#
		entry.set_text((str(now.hour) if (now.hour >= 10) else '0'+str(now.hour))+':'\
			+(str(now.minute) if (now.minute >= 10) else '0'+str(now.minute))+':'\
				+(str(now.second) if (now.second >= 10) else '0'+str(now.second)))				

	'''
		M�todo que retorna o objeto window
	'''
	def get_window(self):
		return self.window
	'''
		M�todo que torna a tela v�sivel para o usu�rio
	'''		
	def show_window(self):
		Gtk.main()
