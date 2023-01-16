from src.DniLetterCalculator import DniLetterCalculator

class DNI(DniLetterCalculator):

    def __init__(self, number):
        self.dni = ""
        self.dniLetter = ""
        self.nif = number
        self.calculator = DniLetterCalculator()



    def checkNifIsANumberFormat(self):
        try:
            self.nif = int(self.nif)
        except:
            return False
        else:
            return True


    def checkNifLenght(self):

        if len(self.nif) == 8:
            return True
        else:
            return False
    

    def checkNifNumberIsCorrect(self):

        if self.checkNifLenght() and self.checkNifIsANumberFormat():
            return True
        else:
            return False



    def setDniLetter(self):

        if self.checkNifNumberIsCorrect():
            try:
                letterPosition = self.calculator.getLetterPositionInTable(self.nif)
            except:
                return False
            else:

                self.dniLetter = self.calculator.getletter(letterPosition)
                return True
        else:
            return False



    def setDni(self):

        if self.setDniLetter():
            self.dni = str(self.nif) + self.dniLetter
            return True
        else:
            self.dni = "No se ha podido obtener la letra"



    def __repr__(self):
        return f"DNI : {self.dni}"