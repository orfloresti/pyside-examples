class Madre:
    def __init__(self):
        print("Soy madre")

class Padre:
    def __init__(self):
        print("Soy padre")

class Hijo:
    def __init__(self):
        Padre.__init__(self)
        Madre.__init__(self)
        print("Soy hijo")

hijo = Hijo()