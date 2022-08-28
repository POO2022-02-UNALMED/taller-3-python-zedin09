class Control:
    tv = None

    def __init__(self):
        self.tv = Control.tv

    def enlazar(self, tv):
        self.tv = tv
        self.tv.control = self

    def getTv(self):
        return self.tv

    def setTv(self, tv):
        self.tv = tv

    # Estado
    def turnOn(self):
        self.tv.turnOn()

    def turnOff(self):
        self.tv.turnOff()

    # Canal
    def canalUp(self):
        self.tv.canalUp()

    def canalDown(self):
        self.tv.canalDown()

    def setCanal(self, canal):
        self.tv.setCanal(canal)

    # Volumen
    def volumenUp(self):
        self.tv.volumenUp()

    def volumenDown(self):
        self.tv.volumenDown()