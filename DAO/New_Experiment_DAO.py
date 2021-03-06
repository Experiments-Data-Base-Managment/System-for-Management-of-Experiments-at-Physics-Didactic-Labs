#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os
import sqlite3
class NewExperimentDAO(object):
	
		
	def connection(self):
			if(os.path.isfile("../BD/sistemaGestor.db")):
				self.conn = sqlite3.connect("../BD/sistemaGestor.db")		
				self.cursor = self.conn.cursor()
			else :
				print "Database not found!" 	
		
			
	def create_table_experiments(self):
		self.cursor.execute("""
			CREATE TABLE experiments (
			id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			institution TEXT NOT NULL,
			course TEXT NOT NULL,
			class TEXT NOT NULL,
			teacher TEXT NOT NULL,
			student TEXT NOT NULL,
			experiment TEXT NOT NULL,
			id_experiment TEXT NOT NULL,
			date DATE NOT NULL,
			time TEXT NOT NULL,
			state_city TEXT NOT NULL,
			lamps_color TEXT NOT NULL,
			type_photocell TEXT NOT NULL,
			distance_lamp_photocell TEXT NOT NULL,
			lamps_power TEXT NOT NULL,
			tau TEXT NOT NULL,
			volt_photocell TEXT NOT NULL,
			resistor TEXT NOT NULL,
			capacitor TEXT NOT NULL,
			description TEXT NOT NULL
		);
		""")
	
	def get_last_id(self):
		self.connection()
		self.cursor.execute('SELECT max(id) FROM experiments')
		max_id = self.cursor.fetchone()[0]
		self.close_connection()
		return "EXP_" + str(max_id+1)
		

	def	 insert_table_experiments(self, experiment):
		self.connection()
		self.cursor.execute("""
			INSERT INTO experiments (institution,
										course,
										class,
										teacher,
										student,
										experiment,
										id_experiment,
										date,
										time,
										state_city,
										lamps_color,
										type_photocell,
										distance_lamp_photocell,
										lamps_power,
										tau,
										volt_photocell,
										resistor,
										capacitor,
										description)
			VALUES ("""'\''+ experiment.get_institution() + "\'," + '\'' + experiment.get_course() + "\'," + '\'' + experiment.get_student_class() \
			+ "\'," + '\'' + experiment.get_teacher_name() + "\'," + '\'' + experiment.get_student_name() + "\'," + '\'' + experiment.get_experiment_name() \
			+ "\'," + '\'' + experiment.get_code_experiment() + "\'," + '\'' + experiment.get_date() + "\'," + '\'' + experiment.get_time() \
			+ "\'," + '\'' + experiment.get_city()+ "\'," + '\'' + experiment.get_lamps_color()+ "\'," + '\'' + experiment.get_type_photocell() \
			+ "\'," + '\'' + experiment.get_distance_lamp_photocell()+ "\'," + '\'' + experiment.get_lamps_power()+ "\'," + '\'' + experiment.get_tau() \
			+ "\'," + '\'' + experiment.get_volt_photocell()+ "\'," + '\'' + experiment.get_resistor()+ "\'," + '\'' + experiment.get_capacitor() \
			+ "\'," + '\'' + experiment.get_description() + '\''""");
			""")	
		self.conn.commit()
		self.close_connection()
		
	def busca(self):
		self.cursor.execute("""SELECT * FROM experiments;""")
		print self.cursor.fetchall()
			
		
	def	 close_connection(self):
			self.conn.close()
