class WaitScreen(object):
	
	def __init__(self):

		self.fraction = 0.0
		
		self.duration_experiment = 0


	def set_new_fraction(self, fraction):

		#print("ESSA E A NOVA FRACTION " + fraction)
		self.fraction = float(fraction)/float(self.duration_experiment)
		

	def get_actual_fraction(self):

		return self.fraction
	
	
	def set_duration_experiment(self, duration_experiment):
		
		self.duration_experiment = duration_experiment


	def get_duration_experiment(self):
		
		return self.duration_experiment
		
	def calc_new_fraction_value(self):
		return 2

'''
w = WaitScreen()

print w.get_duration_experiment()
'''
