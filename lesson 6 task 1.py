from time import sleep
class Svetofor:
    color = ("red", "yellow", "green")
    t = (1, 2, 3)
        def __init__ (self):
      #      self.color = color
            self.color = "green"

        def go (self):
            while True:
                for i in self.color:
                    self.color = i
                print (self.color)
                 sleep (self.t[self.color.index(self.color)])

    svetfr = Svetofor()
    svetfr.go()




  #      def go (self)
   ##        print (self.color)
     #       sleep (t)

