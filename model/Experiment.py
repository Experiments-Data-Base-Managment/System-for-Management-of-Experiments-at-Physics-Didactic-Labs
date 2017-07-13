class Experiment(object):
		
	def __init__(self, institution, course, student_class, teacher_name, student_name, experiment_name, code_experiment, date, time, city, description):	
		self.student_name = student_name
		self.teacher_name = teacher_name
		self.description = description
		self.institution = institution
		self.city = city
		self.date = date
		self.time = time
		self.code_experiment = code_experiment
		self.experiment_name = experiment_name
		self.course = course
		self.student_class = student_class
		
	def get_student_name(self):
		return self.student_name
		
	def get_teacher_name(self):
		return self.teacher_name

	def get_description(self):
		return self.description
		
	def get_institution(self):
		return self.institution

	def get_city(self):
		return self.city

	def get_date(self):
		return self.date
	
	def get_time(self):
		return self.time
		
	def get_code_experiment(self):
		return self.code_experiment
	
	def get_experiment_name(self):
		return self.experiment_name
		
	def get_course(self):
		return self.course
	
	def get_student_class(self):
		return self.student_class
	
	def set_student_name(self, student_name):
		self.student_name = student_name
	
	def set_teacher_name(self, teacher_name):
		self.teacher_name = teacher_name
		
	def set_description(self, description):
		self.description = description
	
	def set_institution(self, institution):
		self.institution = institution
		
	def set_city(self, city):
		self.city = city
	
	def set_date(self, date):
		self.date = date
		
	def set_time(self, time):
		self.time = time
		
	def set_code_experiment(self, code_experiment):
		self.code_experiment = code_experiment
		
	def set_experiment_name(self, experiment_name):
		self.experiment_name = experiment_name
	
	def set_course(self, course):
		self.course = course
	
	def set_student_class(self, student_class):
		self.student_class = student_class
