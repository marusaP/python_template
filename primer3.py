#! /usr/bin/python2

class Kvader(object):

    kajjeto = "geometrijski objekt"
    
    def __init__(self, a, b):
        self.a = a 
        self.b = b

    def ploscina(self):
        return self.a * self.b
    
    def mojafunkcija(*args, **kwargs):
        print(repr(args[0]))
        print(repr(kwargs))
        
    
class Kvadrat(Kvader):   #razred kvadrat deduje iz razreda kvader
    def __init__(self, a):
        super(Kvadrat, self).__init__(a, a)

def main():
    kv = Kvader(1.0, 2.0)
    print(repr(kv.ploscina()))
    kvadrat = Kvadrat (2.0)
    print(repr(kvadrat.ploscina()))

    kvadrat.mojafunkcija("lsdkjf", "dfjs")


if __name__ == "__main__":
    main()
