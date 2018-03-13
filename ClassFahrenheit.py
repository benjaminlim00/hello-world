class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature
        
    def to_fahrenheit(self):
        return self._temperature * 9 / 5 + 32
        
    def get_temperature(self): #getter
        return self._temperature
        
#    def __str__(self):
#        return str(self._temperature)
    
    def set_temperature(self, value): #setter
        if value < -273:
            self._temperature = -273
        else:
            self._temperature = value
    
    temperature = property(get_temperature, set_temperature)
    

    
a = Celsius(30)
#b = a.to_fahrenheit()
#print(b)

#print(a._temperature) # not through getter, not good
print(a.get_temperature()) #using getter
a.temperature = 20 #using getter under property
print(a.temperature)