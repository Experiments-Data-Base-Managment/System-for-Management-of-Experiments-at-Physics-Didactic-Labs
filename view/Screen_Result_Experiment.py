#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import sys
import matplotlib.pyplot as plt
sys.path.append("../")
from controller.Controller_Result_Experiment import ControllerScreenResultExperiment
from Window import Main, Gtk, GdkPixbuf

controller = ControllerScreenResultExperiment()

			
class WindowResultExperiment:

	def __init__(self, path, set_results, controller_screen_new_experiment):
		
		self.set_results = set_results
		
		self.window = Main()
		
		self.window.set_handler(controller.get_handler())

		self.window.set_file_ui(path)
		
		self.window.connect_handles_ui()
		
		controller.set_screen_result_experiment(self)
		
		controller.set_controller_screen_new_experiment(controller_screen_new_experiment)
		
		self.window.set_name_object("result_window")
		
		self.set_table(self.window.get_object_from_window("tabela_resultados"))
	
		self.set_tree_view(self.window.get_object_from_window("tree_view"))
	
		self.create_columns()
		
		self.index = 0
		
		self.axis_x = []
		
		self.axis_y = []
		
		#set_results.print_set_results()
		
		
		while (self.index < len(self.set_results.get_measurements())):
			
			self.times_and_volts = self.set_results.get_specific_measurement(self.index).split('|')
			
			for i in range(0,len(self.times_and_volts)-1):
				self.times_and_volts[i] = self.times_and_volts[i].split(';')
				self.insert_data_table(self.times_and_volts[i][0], self.times_and_volts[i][1])
				'''
					add measurements datas to vector
				'''
				self.axis_x.append(self.times_and_volts[i][0])
				self.axis_y.append(self.times_and_volts[i][1])

			self.index += 1
		'''
			Create graphics from collected data, save it and show him in result screen
		'''	
		
		plt.plot(self.axis_x,self.axis_y)
		plt.xlabel('Time')
		plt.ylabel('voltage')
		plt.title('Capacitor Load Process')
		plt.grid(True)
		plt.tight_layout()
		
		plt.savefig("curva_capacitor.jpeg", dpi = 800)
		graphic = self.window.get_object_from_window("graphic")
		
		#make picture
		self.pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="curva_capacitor.jpeg", width=700, height=500, preserve_aspect_ratio=True)
		graphic.set_from_pixbuf(self.pixbuf)
		#graphic.set_from_file("curva_capacitor.jpeg")
			
		
		controller.fill_experiments_data()
		
		'''
		#codigo teste preenchimento corpo texto
		self.set_value_volt(4.9)
		self.set_value_second(25)
		self.insert_data_table()
		'''
		
	def show_window(self):
		self.window.start_window()
		Gtk.main()
	
	'''
		Os métodos a partir deste ponto do código lidam com a estrutura de tabela
		apresentada na tela de resultados.
	'''
	def set_table(self, table):	 
		self.table = table
	
	def set_tree_view(self, treeView):
		self.treeView = treeView
	
	'''
		Método que cria o número de colunas da tabela de resultados e define o tipo de dado
	'''
	def create_columns(self):
		cell = Gtk.CellRendererText()
		self.treeView.get_column(0).pack_start(cell, False)
		self.treeView.get_column(0).add_attribute(cell, "text", 0)
		self.treeView.get_column(1).pack_start(cell, False)
		self.treeView.get_column(1).add_attribute(cell, "text", 1)

	
	def insert_data_table(self, volt, seconds):
		'''
			iter_tree = table.get_iter_first();		
		
			if( iter_tree != None):
				iter_tree = self.table.insert_after(iter_tree,[self.volt,self.second])
				self.table.row_changed(iter_tree,iter_tree)
				print "There are rows in the table." \
					+ str(self.table[iter_tree][0]) + " and " + str(self.table[iter_tree][1]) + "."
			else:
		'''
		
		iter_tree = self.table.prepend([volt,seconds])
		
		'''
			self.table.row_changed(iter_tree,iter_tree)
			print "Until this moment there wasn't row in the table, but now there is and its values is: " \
			+ str(self.table[iter_tree][0]) + " and " + str(self.table[iter_tree][1])		
		'''
	def set_value_volt(self, volt):
		self.volt = volt
	
	def set_value_second(self, seconds):
		self.second = seconds
		
	def get_control(self):
		return self.controller
		
	'''
		Método que retorna o objeto window
	'''
	def get_window(self):
		return self.window

#windowResult = WindowResultExperiment("../view/xml_windows/result_experiment.glade")

#windowResult.show_window()

