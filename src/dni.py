from src.CalculadoraLetraDNI import CalculadoraLetraDNI

class DNI(CalculadoraLetraDNI):

    def __init__(self, number):
        self.Dni = ""
        self.dniLetter = ""
        self.dniNumber = number
        self.calculadora = CalculadoraLetraDNI()



    def checkDniNumberIsInt(self):
        try:
            self.dniNumber = int(self.dniNumber)
        except:
            return False
        else:
            return True


    def checkLenghtDniNumber(self):

        if len(self.dniNumber) == 8:
            return True
        else:
            return False
    

    def checkDniNumberIsCorrect(self):

        if self.checkLenghtDniNumber() and self.checkDniNumberIsInt():
            return True
        else:
            return False



    def getDniNumber(self):


        if self.checkDniNumberIsCorrect():

            try:
                letterPosition = self.calculadora.getLetterPositionInTable(self.dniNumber)

            except:
                return 'No es posible obtener la letra de la Tabla'

            else:

                self.dniLetter = self.calculadora.getletter(letterPosition)
                
                self.Dni = str(self.dniNumber) + self.dniLetter
                
                return self.Dni

        else:
            return 'El numero que has introducido no es correcto'

