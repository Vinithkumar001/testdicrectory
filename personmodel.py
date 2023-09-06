import json

class Person(object):
   def __init__(self, first_name = None, last_name = None):
      self.first_name = first_name
      self.last_name = last_name
   #returns Person name, ex: John Doe
   def name(self):
      return ("%s %s" % (self.first_name,self.last_name))
		
   @classmethod
   #returns all people inside db.txt as list of Person objects
   def getAll(self):
      database = open('db.txt', 'r')
      result = []
      json_list = json.loads(database.read())
      print(json_list)
      for item in json_list:
         item = json.loads(item)
         person = Person(item['first_name'], item['last_name'])
         result.append(person)
      return result
# Create an instance of the Person class
a = Person()

# Call the getAll method on the instance
people_in_db = a.getAll()

# Print the names of all people in the database
for person in people_in_db:
   print(person.name())
