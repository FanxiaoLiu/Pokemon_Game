class Pokemon:

     def __init__(self, name, typ, id):
          self.pokeid = id
          self.name = name
          self.type = typ
          self.CP = 0
          self.stats = [0, 0, 0] ## [attack, defense, hp] - max 15
          self.IV = 0
          self.moveset = []

     def get_ID(self):
          return self.pokeid

     def get_name(self):
          return self.name

     def get_type(self):
          return self.type

     def get_CP(self):
          return self.CP

     def get_stats(self):
          return self.stats

     def get_IV(self):
          return self.IV

     def display_details(self):
          print("Name:\t",self.get_name())
          print("Type:\t",self.get_type())
          print("CP:\t",self.get_CP())
          stats = self.get_stats()
          print("Attack:\t",stats[0])
          print("Defense:",stats[1])
          print("Stamina:",stats[2])
          print("IV:\t",self.get_IV())

     def set_CP(self, value):
          self.CP = value
          return self.CP

     def power_up(self, value):
          self.CP += value
          return self.CP

     def set_stats(self, attack, defense, stamina):
          if attack > 15 or defense > 15 or stamina > 15:
               print("Sorry, values cannot exceed 15.")
          else:
               self.stats = [attack, defense, stamina]
               self.IV = sum(self.stats)/45*100
          return self.IV
     
     def set_moveset(self,moveset):
          self.moveset = moveset
          
     
