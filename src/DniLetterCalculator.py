class DniLetterCalculator:
    

    def __init__(self):
        self.letterTable = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
        self.tableLenght = len(self.letterTable)



    def getLetterPositionInTable(self, number):

        position = number % self.tableLenght
        return position


        
    def getletter(self, position):

        letter = self.letterTable[position]
        return letter


