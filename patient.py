#! /usr/bin/env python

__author__ = "Gene Blanchard"
__email__ = "me@geneblanchard.com"

'''
Patient Class

PatientID
-------------
DOB
RACE
GesationalAge
BirthWeight
WeightAppropriate
Delivery
Apgar
Resusc
ROM
MatHX
MatMed
Enviroment

'''

class Patient(object):
	# Initialize with patient id
	def __init__(self, patientid):
		self.patientid = patientid

	# Set other attributes
	def set_dob(self,attribute):
		self.dob = attribute
	def set_race(self,attribute):
		self.race = attribute
	def set_gestage(self,attribute):
		self.gestage = attribute
	def set_birthweight(self,attribute):
		self.birthweight = attribute
	def set_weightapprop(self,attribute):
		self.weightapprop = attribute
	def set_delivery(self,attribute):
		self.delivery = attribute
	def set_apgar(self,attribute):
		self.apgar = attribute
	def set_resusc(self,attribute):
		self.resusc = attribute
	def set_rom(self,attribute):
		self.rom = attribute
	def set_mathx(self,attribute):
		self.mathx = attribute
	def set_matmed(self,attribute):
		self.matmed = attribute

	# # Adding samples
	# def add_enviroment(self,sample):
	# 	if self.enviroment():
	# 		self.enviroment[sample.date] = sample
	# 	else:
	# 		self.enviroment = {sample.date:sample}
	# def add_stool(self, sample)
	# 	if self.en


	# Return attributes
	def get_patientid(self):
		return self.patientid
	def get_dob(self):
		return self.dob
	def get_race(self):
		return self.race
	def get_gestage(self):
		return self.gestage
	def get_birthweight(self):
		return self.birthweight
	def get_weightapprop(self):
		return self.weightapprop
	def get_delivery(self):
		return self.delivery
	def get_apgar(self):
		return self.apgar
	def get_resusc(self):
		return self.resusc
	def get_rom(self):
		return self.rom
	def get_mathx(self):
		return self.mathx
	def get_matmed(self):
		return self.matmed
	# def get_enviroment(self):
	# 	return self.enviroment


