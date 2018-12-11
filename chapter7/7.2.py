class stock:
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    def getName(self):
        return self.__name

    def getSymbol(self):
        return self.__symbol

    def setPreviousClosingPrice(self, previousClosingPrice):
        previousClosingPrice = self.__previousClosingPrice
        return previousClosingPrice

    def setCurrentPrice(self, currentPrice):
        currentPrice = self.__currentPrice
        return currentPrice

    def getChangePercent(self):
        return (currentPrice - previousClosingPrice) / 100

Stock = stock()
Stock.name = input("Enter the stock name: ")
Stock.symbol = input("Enter the symbol: ")
Stock.previousClosingPrice = eval(input("Enter previousClosingPrice: "))
Stock.currentPrice = eval(input("Enter current price: "))
