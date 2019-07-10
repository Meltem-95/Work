Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class UAV:
	name = ""
	is_landing = False
	is_takeoff = False
	def takeoff():
		pass

	
>>> class Drone(UAV):
	def __init__(self, drone_name):
		self.name = drone_name
	def takeoff(self):
		if self.is_landing == True:
			return False
		if self.is_landing == False:
			self.is_takeoff = True
			return True

		
>>> 
