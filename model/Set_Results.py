class SetResults(object):
	
	measurement =[]
	
	def add_measurement(self, data):
		
		self.measurement.append(data)
		
		
	def get_measurements(self):
		
		return self.measurement
		
		
	def get_specific_measurement(self, index):
		
		return self.measurement[index]	
		
	
	def print_set_results(self):
		print self.measurement	
