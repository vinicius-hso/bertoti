class Subject:
		
	"""Representa o que está sendo observado"""
	def __init__(self):

		"""cria uma lista de observers vazia"""
		self._observers = []

	def notify(self, modifier = None):

		"""alerta os observers"""
		for observer in self._observers:
			if modifier != observer:
				observer.update(self)

	def attach(self, observer):
	
		'''Se o observer não está na lista,
		adiciona à lista'''
		if observer not in self._observers:
			self._observers.append(observer)

	def detach(self, observer):

		"""Remove o observer da lista de observers"""
		try:
			self._observers.remove(observer)
		except ValueError:
			pass

class Observer(Subject):
    
	"""monitora o objeto"""
	def __init__(self, name =''):
		Subject.__init__(self)
		self.name = name
		self._data = 0

	@property
	def data(self):
		return self._data

	@data.setter
	def data(self, value):
		self._data = value
		self.notify()
  
class FahrenheitViewer:
    
	"""atualiza o Fahrenheit Viewer"""
	def update(self, subject):
		to_fahrenheit = ((subject.data * (9/5)) + 32)
		print(f'Fahrenheit Viewer:\n\tSubject: {subject.name}\n\tTemperatura: {round(to_fahrenheit, 2)}°F\n')
  
class KelvinViewer:
    
	"""atualiza o Kelvin viewer"""
	def update(self, subject):
		to_kelvin = subject.data + 273.15
		print(f'Kelvin Viewer:\n\tSubject: {subject.name}\n\tTemperatura: {round(to_kelvin, 2)}°K\n')
  
if __name__ == "__main__":
    
	"""fornece os dados"""
	obj1 = Observer('Temperatura 1')
	obj2 = Observer('Temperatura 2')

	view1 = FahrenheitViewer()
	view2 = KelvinViewer()

	obj1.attach(view1)
	obj1.attach(view2)

	obj2.attach(view1)
	obj2.attach(view2)

	obj1.data = 37
	obj2.data = 39