class TV:
    numTV = 0
    control = None

    def __init__(self, marca, estado):
        self.canal = 1
        self.volumen = 1
        self.precio = 500
        self.marca = marca
        self.estado = estado
        TV.numTV += 1

    # Marca
    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    # Control
    def getControl(self):
        return self.control

    def setControl(self, control):
        self.control = control

    # Precio
    def getPrecio(self):
        return self.precio

    def setPrecio(self, precio):
        self.precio = precio

    # Volumen
    def getVolumen(self):
        return self.volumen

    def setVolumen(self, volumen):
        if self.estado:
            if 0 <= volumen <= 7:
                self.volumen = volumen

    def volumenUp(self):
        if self.estado:
            if self.volumen < 7:
                self.volumen += 1

    def volumenDown(self):
        if self.estado:
            if self.volumen > 0:
                self.volumen -= 1

    # Canal
    def getCanal(self):
        return self.canal

    def setCanal(self, canal):
        if self.estado:
            if 1 <= canal <= 120:
                self.canal = canal

    def canalUp(self):
        if self.estado:
            if self.canal < 120:
                self.canal += 1

    def canalDown(self):
        if self.estado:
            if self.canal > 1:
                self.canal -= 1

    # Contador
    def getNumTV(self):
        return TV.numTV

    def setNumTV(self, numTV):
        TV.numTV = numTV

    # Estado
    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def getEstado(self):
        return self.estado
