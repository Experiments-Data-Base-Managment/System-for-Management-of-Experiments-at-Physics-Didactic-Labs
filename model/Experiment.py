import math

class Experiment(object):
		
	def __init__(self, institution, course, student_class, \
				teacher_name, student_name, experiment_name, \
				code_experiment, date, time, \
				city, lamps_color, type_photocell, \
				distance_lamp_photocell, lamps_power, \
				volt_photocell, resistor, capacitor, \
				 description):	
		self.institution = institution
		self.course = course
		self.student_class = student_class
		self.teacher_name = teacher_name
		self.student_name = student_name
		self.experiment_name = experiment_name
		self.code_experiment = code_experiment
		self.date = date
		self.time = time
		self.city = city
		self.lamps_color = lamps_color
		self.type_photocell = type_photocell
		self.distance_lamp_photocell = distance_lamp_photocell
		self.lamps_power = lamps_power
		self.volt_photocell = volt_photocell
		self.resistor = resistor
		self.capacitor = capacitor
		self.description = description
		self.calc_tau()
		
	def set_institution(self, institution):
		self.institution = institution

	def get_institution(self):
		return self.institution
		
	def set_course(self, course):
		self.course = course

	def get_course(self):
		return self.course

	def set_student_class(self, student_class):
		self.student_class = student_class
	
	def get_student_class(self):
		return self.student_class

	def set_teacher_name(self, teacher_name):
		self.teacher_name = teacher_name
		
	def get_teacher_name(self):
		return self.teacher_name

	def set_student_name(self, student_name):
		self.student_name = student_name

	def get_student_name(self):
		return self.student_name	

	def set_experiment_name(self, experiment_name):
		self.experiment_name = experiment_name

	def get_experiment_name(self):
		return self.experiment_name

	def set_code_experiment(self, code_experiment):
		self.code_experiment = code_experiment
		
	def get_code_experiment(self):
		return self.code_experiment

	def set_date(self, date):
		self.date = date		

	def get_date(self):
		return self.date
	
	def set_time(self, time):
		self.time = time

	def get_time(self):
		return self.time
			
	def set_city(self, city):
		self.city = city
		
	def get_city(self):
		return self.city		
		
	def set_lamps_color(self, lamps_color):
		self.lamps_color = lamps_color
		
	def get_lamps_color(self):
		return self.lamps_color
	
	def set_type_photocell(self, type_photocell):
		self.type_photocell = type_photocell
	
	def get_type_photocell(self):
		return self.type_photocell
	
	def set_distance_lamp_photocell(self, distance_lamp_photocell):
		self.distance_lamp_photocell = distance_lamp_photocell
	
	def get_distance_lamp_photocell(self):
		return self.distance_lamp_photocell
		
	def set_lamp_power(self, lamps_power):	
		self.lamps_power = lamps_power
	
	def get_lamp_power(self):
		return self.lamps_power
		
	def set_tau(self, tau):
		self.tau = tau
		
	def get_tau(self):
		return self.tau
		
	def set_volt_photocell(self, volt_photocell):		
		self.volt_photocell = volt_photocell
		
	def get_volt_photocell(self):
		return self.volt_photocell

	def set_description(self, description):
		self.description = description
	
	def get_description(self):
		return self.description		
	
	def set_resisot(self, resistor):
		self.resistor = resistor
		
	def get_resistor(self):
		return self.resistor
		
	def set_capacitor(self, capacitor):
		self.capacitor = capacitor
		
	def get_capacitor(self):
		return self.capacitor
	
	def calc_tau(self):
		self.tau = float(self.get_resistor()) * float(self.get_capacitor())
	
	def set_voltage_capacitor_tau(self, voltage):
		self.volt_capacitor = voltage
		
	def get_voltage_capacitor_tau(self):
		return float(self.volt_capacitor)
		
	def calc_energy_capacitor(self):
		self.energy_capacitor = (float(self.get_capacitor()) * math.pow(float(self.get_voltage_capacitor_tau()),2) * 0.5)
		
	def get_energy_capacitor(self):
		return self.energy_capacitor
	
	def set_duration(self, duration):
		self.duration = duration
		
	def get_duration(self):
		return duration
