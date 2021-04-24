#By: Cristian Camilo Vargas Morales

class AlertOrangeSalmon(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2019, 3, 30)  #Last two Years
        self.SetEndDate(2021, 3, 30)
        
        #NVIDIA
        self.nvda = self.AddEquity("NVDA", Resolution.Daily)
        self.nvda.SetDataNormalizationMode(DataNormalizationMode.Raw)  
        self.nvda.SetLeverage(1)      #Configuramos Apalancamiento Normal (STD)
        
        #Aramco
        self.aramco = self.AddEquity("2222.SR", Resolution.Daily)
        self.aramco.SetDataNormalizationMode(DataNormalizationMode.Raw)
        self.aramco.SetLeverage(1)
        
        #JPMorgan Chase & Co.
        self.JPM = self.AddEquity("JPM", Resolution.Daily)
        self.JPM.SetDataNormalizationMode(DataNormalizationMode.Raw)
        self.JPM.SetLeverage(1)
        
        #Alibaba Group Holding Limited
        self.BABA = self.AddEquity("BABA", Resolution.Daily)
        self.BABA.SetDataNormalizationMode(DataNormalizationMode.Raw)
        self.BABA.SetLeverage(1)
        
        #Alphabet Inc. (Google)
        self.GOOG = self.AddEquity("GOOG", Resolution.Daily)
        self.GOOG.SetDataNormalizationMode(DataNormalizationMode.Raw)
        self.GOOG.SetLeverage(1)
        
        # 1. Set Starting Cash 
        self.SetCash(1000000)       #Portafolio Inicial de inversión de 1000000

    def OnData(self, data):
        if not self.Portfolio.Invested:
            self.MarketOrder("NVDA", 80)   #Vamos a intentar por 100 acciones de NVDA
            self.Debug(str(self.Portfolio["NVDA"].AveragePrice))
            self.MarketOrder("2222.SR", 100)   #Vamos a intentar por 100 acciones de Aramco
            self.Debug(str(self.Portfolio["2222.SR"].AveragePrice))
            self.MarketOrder("JPM", 200)   #Vamos a intentar por 100 acciones de JPM
            self.Debug(str(self.Portfolio["JPM"].AveragePrice))
            self.MarketOrder("BABA", 50)   #Vamos a intentar por 100 acciones de BABA
            self.Debug(str(self.Portfolio["BABA"].AveragePrice))
            self.MarketOrder("GOOG", 200)   #Vamos a intentar por 100 acciones de GOOG
            self.Debug(str(self.Portfolio["GOOG"].AveragePrice))