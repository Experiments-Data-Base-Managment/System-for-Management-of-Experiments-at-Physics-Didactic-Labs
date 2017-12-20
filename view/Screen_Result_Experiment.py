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
		
		self.set_tables(self.window.get_object_from_window("tabela_resultados"),self.window.get_object_from_window("liststore_result_experiment"))
	
		self.set_tree_views(self.window.get_object_from_window("tree_view"),self.window.get_object_from_window("tree_view2"))
	
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
		plt.xlabel('Tempo')
		plt.ylabel('Tensao')
		plt.title('Processo de Carga do Capcitor')
		plt.grid(True)
		
		#plt.tight_layout()
		
		plt.savefig("curva_capacitor.jpeg", dpi = 800)
		graphic = self.window.get_object_from_window("graphic")
		
		#make picture
		self.pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="curva_capacitor.jpeg", width=700, height=500, preserve_aspect_ratio=True)
		graphic.set_from_pixbuf(self.pixbuf)
		#graphic.set_from_file("curva_capacitor.jpeg")
		
		
		controller.fill_experiments_data()
		
		controller.fill_table_results()
				
	def show_window(self):
		self.window.start_window()
		Gtk.main()
	
	'''
		Os métodos a partir deste ponto do código lidam com a estrutura de tabela
		apresentada na tela de resultados.
	'''
	def set_tables(self, table_1, table_2):	 
		self.table_1 = table_1
		self.table_2 = table_2
	
	def set_tree_views(self, tree_view_1, tree_view_2):
		self.tree_view_1 = tree_view_1
		self.tree_view_2 = tree_view_2
	
	'''
		Método que cria o número de colunas da tabela de resultados e define o tipo de dado
	'''
	def create_columns(self):
		
		cell_tree_view_1 = Gtk.CellRendererText()
		self.tree_view_1.get_column(0).pack_start(cell_tree_view_1, False)
		self.tree_view_1.get_column(0).add_attribute(cell_tree_view_1, "text", 0)
		self.tree_view_1.get_column(1).pack_start(cell_tree_view_1, False)
		self.tree_view_1.get_column(1).add_attribute(cell_tree_view_1, "text", 1)
		
		cell_tree_view_2 = Gtk.CellRendererText()
		self.tree_view_2.get_column(0).pack_start(cell_tree_view_2, False)
		self.tree_view_2.get_column(0).add_attribute(cell_tree_view_2, "text", 0)
		self.tree_view_2.get_column(1).pack_start(cell_tree_view_2, False)
		self.tree_view_2.get_column(1).add_attribute(cell_tree_view_2, "text", 1)
		
		self.tree_view_2.get_column(2).pack_start(cell_tree_view_2, False)
		self.tree_view_2.get_column(2).add_attribute(cell_tree_view_2, "text", 2)
		self.tree_view_2.get_column(3).pack_start(cell_tree_view_2, False)
		self.tree_view_2.get_column(3).add_attribute(cell_tree_view_2, "text", 3)
		
		self.tree_view_2.get_column(4).pack_start(cell_tree_view_2, False)
		self.tree_view_2.get_column(4).add_attribute(cell_tree_view_2, "text", 4)
		self.tree_view_2.get_column(5).pack_start(cell_tree_view_2, False)
		self.tree_view_2.get_column(5).add_attribute(cell_tree_view_2, "text", 5)
		
		self.tree_view_2.get_column(6).pack_start(cell_tree_view_2, False)
		self.tree_view_2.get_column(6).add_attribute(cell_tree_view_2, "text", 6)
		self.tree_view_2.get_column(7).pack_start(cell_tree_view_2, False)
		self.tree_view_2.get_column(7).add_attribute(cell_tree_view_2, "text", 7)
		
		self.tree_view_2.get_column(8).pack_start(cell_tree_view_2, False)
		self.tree_view_2.get_column(8).add_attribute(cell_tree_view_2, "text", 8)
	
	def insert_data_table(self, volt, seconds):
		iter_tree = self.table_1.prepend([volt,seconds])

	def set_value_volt(self, volt):
		self.volt = volt
	
	def set_value_second(self, seconds):
		self.second = seconds
		
	def get_control(self):
		return self.controller
		
	def get_table_results(self):
		return self.table_2
		
	def get_set_results(self):
		return self.set_results
		
	'''
		Método que retorna o objeto window
	'''
	def get_window(self):
		return self.window

#windowResult = WindowResultExperiment("../view/xml_windows/result_experiment.glade")

#windowResult.show_window()

