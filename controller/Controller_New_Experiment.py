#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import sys
import threading
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GObject
sys.path.append('../')
from DAO.New_Experiment_DAO import NewExperimentDAO
from view.Screen_Load_Results import WindowLoadResult
from model.Serial_Communication import SerialCommunication, time
from model.Wait_Screen import WaitScreen
from model.Set_Results import SetResults
from model.Experiment import Experiment
 
dao_new_experiment = NewExperimentDAO()

set_results = SetResults()

wait_screen = WaitScreen()

class ThreadMonitoring(threading.Thread):
	
	def __init__(self):	
		
		threading.Thread.__init__(self)	
		
	'''
		Método principal da thread responsável por iniciar o experimento
		e manter a tela de loading funcionando idependente das demais
	'''				
	def run(self):
		
		self.start_measurement_experiment()
		
		time.sleep(0.4)
		print "ESSE E O TIME DE DURACAO< FUNCIONA: " + wait_screen.get_duration_experiment()
		
		self.get_measurement_data()
	
	'''
		Método responsável por solicitar o tempo de duração do experimento
		e por repassar essa informção para a tela de espera			
	'''
	def	start_measurement_experiment(self):
		
		self.port_serial = SerialCommunication()

		self.port_serial.request_duration_experiment()
		
		# Verifica se o buffer contém dados, caso haja aguarda 0.3 segundos para lê-los 
		if(self.port_serial.get_channel().in_waiting == 0 ):
			time.sleep(0.3)
			
		self.qnt_byte = self.port_serial.get_channel().in_waiting

		self.duration_of_experiment = self.port_serial.receive(self.qnt_byte)
		
		self.port_serial.get_channel().flush()
		
		# Adiciona o tempo de duração à tela de Loading
		wait_screen.set_duration_experiment(self.duration_of_experiment)
		
	'''
		Método responsável por manter o polling na porta serial e pegar
		os dados enviados pelo arduino
	'''
	def get_measurement_data(self):
			
		self.port_serial.start_arduino()
		
		self.index = 0
				
		'''
			Quando o polling detecta dados no buffer, o sistema "dorme" por 1 segundo
			para depois coletar os dados no buffer. Esses dados são tratados para serem
			utilizados na tela de Loading e são armazenados numa tupla para uso posterior
			na tela de Resultados.
		'''		
		while True:
			
			if(self.port_serial.get_channel().in_waiting != 0):
				
				time.sleep(1)
				
				# Pega a quantidade de bytes presente no buffer
				self.qnt_bytes = self.port_serial.get_channel().in_waiting
				
				# Ler do buffer a quantidade exata de dados presentes nele
				self.data = self.port_serial.receive(self.qnt_bytes)
				
				# Limpa o buffer por segurança		
				self.port_serial.get_channel().flush()
				
				# Adiciona os dados lidos numa tupla
				set_results.add_measurement(self.data)
		
				#print set_results.get_measurements()[self.index]
				
				# Recupera a última tupla adicionada e remove o caractere separador entre as medidas enviadas
				self.split_data(set_results.get_measurements()[self.index])
								
				# Pega o último par tempo-tensão, separa-os e adiciona o tempo como novo valor da razão entre
				# tempo atual do experimento e o tempo total do experimento
				wait_screen.set_new_fraction(int(self.times_measureds[len(self.times_measureds)-2].split(';')[0]))
				
				# Index utilizado para recuperar a última tupla de pares tempo-tensão		
				self.index += 1
				
				# Verifica se o último par tempo-tensão foi recebido e, caso seja verdade encerrar o polling no buffer
				if(self.times_measureds[len(self.times_measureds)-2][0] == wait_screen.get_duration_experiment()):
					
					break
		
	def split_data(self, data):
	
		self.times_measureds = data.split('|')
		
	
class Handler:
	
	def __init__(self, controller):
		self.controller = controller
	
	def on_button_run_clicked(self, button):
		
		print("O Handle Funciona para button_run")
		
		self.controller.set_experiment()
		
		thread2 = ThreadMonitoring()
		
		thread2.start()
		
		# Inicializa a tela de espera, e passa o conjunto de dados monitorados
		self.screen_load_result = WindowLoadResult("../view/xml_windows/load_results.glade", wait_screen, set_results)
		
		self.screen_load_result.get_controller().set_controller_screen_new_experiment(self.controller)
		
		# Interrupção do sistema que atualizar a barra de loading no intervalo de 1 segundo
		GObject.timeout_add(4000, self.screen_load_result.get_controller().fill_progress_bar, None)	
		
		self.screen_load_result.show_window()	
	

class ControllerScreenExperiment:			
	
	def __init__(self):
	
		self.handler = Handler(self)
	
	
	def get_handler(self):
	
		return self.handler
	
	'''
		Método que recupera o último id do BD e adiciona a um campo do formulário
	'''					
	def set_id_experiment_view(self, entry):
	
		entry.set_text(dao_new_experiment.get_last_id())
	
	
	def get_screen_experiment(self):
		
		return self.screen_experiment
		
	'''
		Método que recebe o objeto tela de novo experimento
	'''	
	def set_screen_experiment(self, screen_experiment):
		
		self.screen_experiment = screen_experiment	
		
	'''
		Método que preenche as variaveis do objto com os dados extraídos do formulário
	'''
	def set_experiment(self):
		active_lamp_color = self.get_screen_experiment().get_window().get_object_from_window("combobox_lamp_color").get_active_iter()
		active_photocell = self.get_screen_experiment().get_window().get_object_from_window("combobox_photocell").get_active_iter()
		active_distance = self.get_screen_experiment().get_window().get_object_from_window("combobox_distance").get_active_iter()

		self.experiment = Experiment(\
			self.get_screen_experiment().get_window().get_object_from_window("institution").get_text(),\
			self.get_screen_experiment().get_window().get_object_from_window("course").get_text(),\
			self.get_screen_experiment().get_window().get_object_from_window("class").get_text(),\
			self.get_screen_experiment().get_window().get_object_from_window("teacher").get_text(),\
			self.get_screen_experiment().get_window().get_object_from_window("student").get_text(),\
			self.get_screen_experiment().get_window().get_object_from_window("experiment").get_text(),\
			self.get_screen_experiment().get_window().get_object_from_window("id_experiment").get_text(),\
			self.get_screen_experiment().convert_format_date_bd(self.get_screen_experiment().get_window().get_object_from_window("date").get_text()),\
			self.get_screen_experiment().get_window().get_object_from_window("time").get_text(),\
			self.get_screen_experiment().get_window().get_object_from_window("state_city").get_text(),\
			self.get_screen_experiment().get_window().get_object_from_window("combobox_lamp_color").get_model().get_value(active_lamp_color,0),\
			self.get_screen_experiment().get_window().get_object_from_window("combobox_photocell").get_model().get_value(active_photocell,0),\
			self.get_screen_experiment().get_window().get_object_from_window("combobox_distance").get_model().get_value(active_distance,0),\
			self.get_screen_experiment().get_window().get_object_from_window("lamps_power").get_text(),\
			self.get_screen_experiment().get_window().get_object_from_window("const_time").get_text(),\
			self.get_screen_experiment().get_window().get_object_from_window("volt_photocell").get_text(),\
			self.get_screen_experiment().get_textbuffer(self.get_screen_experiment().get_window().get_object_from_window("description").get_buffer()))

	'''
		Método que retorna o objeto experimento
	'''	
	def get_experiment(self):
		return self.experiment
		
