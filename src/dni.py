from src.CalculadoraLetraDNI import CalculadoraLetraDNI

class DNI(CalculadoraLetraDNI):

    def __init__(self, number):
        self.Dni = ""
        self.dniLetter = ""
        self.nif = number
        self.calculadora = CalculadoraLetraDNI()



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



    def getDniLetter(self):


        if self.checkNifNumberIsCorrect():

            try:
                letterPosition = self.calculadora.getLetterPositionInTable(self.nif)

            except:
                return 'No es posible obtener la letra de la Tabla'

            else:

                self.dniLetter = self.calculadora.getletter(letterPosition)
                
                self.Dni = str(self.nif) + self.dniLetter
                
                return self.Dni

        else:
            return 'El numero que has introducido no es correcto'

