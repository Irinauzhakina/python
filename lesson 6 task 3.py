class Work:
        def __init__ (self, name, surname, position, salary, bonus):
            self.name = name
            self.surname = surname
            self.position = position
            self.income = {"s":salary, "b":bonus}
#    self.salary = salary
   #         self.bonus = bonus

class Position(Work):

        def get_name_surname (self):
         #   print ()
          return       "{0} {1}".format  (self.name, self.surname)
        def get_incom (self):
     #       return self.salary+self.bonus
          return self.income ["s"]+self.income ["b"]

person = Position ("Irina", "Irina", "boss", 10000000, 100000000)

print (person.name)
print (person.surname)
print (person.get_name_surname())
