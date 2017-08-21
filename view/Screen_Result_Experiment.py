#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import sys
sys.path.append("../")
from controller.Controller_Result_Experiment import ControllerScreenResultExperiment
from Window import Main, Gtk

controller = ControllerScreenResultExperiment()

			
class WindowResultExperiment:

	def __init__(self, path, set_results):
		
		self.set_results = set_results
		
		self.window = Main()
		
		self.window.set_handler(controller.get_handler())

		self.window.set_file_ui(path)
		
		self.window.connect_handles_ui()
		
		controller.set_screen_result_experiment(self)
		
		self.window.set_name_object("result_window")
		
		self.set_table(self.window.get_object_from_window("tabela_resultados"))
	
		self.set_tree_view(self.window.get_object_from_window("tree_view"))
	
		self.create_columns()
		
		self.index = 0
		
		#set_results.print_set_results()
		
		
		while (self.index < len(self.set_results.get_measurements())):
			self.data = self.set_results.get_specific_measurement(self.index).split(';')
			self.insert_data_table(self.data[0], self.data[1])
			self.index += 1
		
			
		'''
		#codigo teste preenchimento corpo texto
		self.set_value_volt(4.9)
		self.set_value_second(25)
		self.insert_data_table()
		'''
		
	def show_window(self):
		self.window.start_window()
		Gtk.main()

	def set_table(self, table):	 
		self.table = table
	
	def set_tree_view(self, treeView):
		self.treeView = treeView

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
		
		iter_tree = self.table.prepend([seconds,volt])
		
		'''
			self.table.row_changed(iter_tree,iter_tree)
			print "Until this moment there wasn't row in the table, but now there is and its values is: " \
			+ str(self.table[iter_tree][0]) + " and " + str(self.table[iter_tree][1])		
		'''
	def set_value_volt(self, volt):
		self.volt = volt
	
	def set_value_second(self, seconds):
		self.second = seconds

#windowResult = WindowResultExperiment("../view/xml_windows/result_experiment.glade")

#windowResult.show_window()

