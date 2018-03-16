# ERROR 1

year = int(input("Bienvenue, en quelle année êtes-vous né(e) ? "))

if year <= 1900:
    print ("Wouah ça c'est vieux")
elif year > 1900 and year < 2020:
    print ("Ca va")
else:
    print ("Dans le turfu")
    

# ERROR 2

class Person:
  def __init__(self, first_name, last_name):
    self.first = first_name
    self.last = last_name
  def speak(self):
    print("My name is " + self.first + " " + self.last)

me = Person("Brandon", "Walsh")
you = Person("Ethan", "Reed")

me.speak()
you.speak()
