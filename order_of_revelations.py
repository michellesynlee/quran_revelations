import sys
import pandas as pd

class OrderofRevelations():
    def __init__(self):
        df = pd.read_excel('Order_Revelations.xlsx', header=None)
        self.Atka = dict(zip(df[0], df[1]))
        self.AbuSalih_Yaqubi = dict(zip(df[0], df[2]))
        self.AbuSalih_Mabani = dict(zip(df[0], df[3]))
        self.Zuhri = dict(zip(df[0], df[4]))
        self.StdEgyptian = dict(zip(df[0], df[5]))

    def find_revelations(self, surah):
        revelations = []
        revelations.extend([key for key, val in self.Atka.items() if val == surah])
        revelations.extend([key for key, val in self.AbuSalih_Yaqubi.items() if val == surah])
        revelations.extend([key for key, val in self.AbuSalih_Mabani.items() if val == surah])
        revelations.extend([key for key, val in self.Zuhri.items() if val == surah])
        revelations.extend([key for key, val in self.StdEgyptian.items() if val == surah])
        #print("Surah: ", surah)
        #print("Revelations: ", revelations)
        return revelations
    def find_rev_range(self, surah):
        revelations = self.find_revelations(surah)
        smallest = min(revelations)
        largest = max(revelations)
        return(F"Surah {surah} : Range: {smallest} - {largest}")
    
if __name__ == "__main__": 
    text = OrderofRevelations()
    #text.find_revelations(76)
    print(text.find_rev_range(2))
   
