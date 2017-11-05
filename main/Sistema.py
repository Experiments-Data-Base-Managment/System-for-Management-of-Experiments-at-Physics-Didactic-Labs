#!/usr/bin/env python-
# -*- coding: iso-8859-15 -*-

import sys
sys.path.append('../')

from view import Screen_New_Experiment

if __name__ == "__main__":		
	
	window = Screen_New_Experiment.WindowNewExperiment("../view/xml_windows/new_experiment.glade")
	
	window.show_window()
