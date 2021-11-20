class Doroga:
        def __init__ (self, dl,sh):
            self.dl = dl
            self.sh = sh

        def get_ves (self, grav, n):
            return (self.dl * self.sh * grav * n) / 1000

a = Doroga (100, 10)

print  (a.get_ves (20, 10))
