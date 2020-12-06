# !/usr/bin/env python

"""
            ／￣￣￣￣￣￣￣￣
　　　　　　  |　Maak een python script waarin je een Class definieert genaamd Liedje, die Class zal de tekst van een
　　　　　　  |　liedje laten zien. De __init__() methode zou twee argumenten moeten hebben nl.: 'self' en 'tekst'.
　　　　　　  |　'tekst' is een lijst. Maak binnen je Class een method/function genaamd 'zingen' die elk element van de
　　　　　　  |　songtekst op zijn eigen regel afdrukt. Definieer een variabele: 'verjaardagslied' die een object
　　　　　　  |　instantiëert van de Class.
　　　　　　  ＼＿＿　＿＿＿＿＿＿＿
　　　　　　　　　  ∨
            ██████████  ████
        ████▒▒░░░░░░░░██▒▒░░██
      ██▒▒░░░░██░░██░░░░██░░░░██
    ██▒▒░░░░░░██░░██░░░░░░▒▒░░██
    ██░░░░░░░░██░░██░░░░░░▒▒▒▒██
  ██░░░░░░▒▒▒▒░░░░░░▒▒▒▒░░░░▒▒██
██▒▒░░░░░░░░░░░░██░░░░░░░░░░░░██
██░░░░▒▒░░░░░░░░██░░░░░░░░░░▒▒██
██░░░░▒▒░░░░░░░░░░░░░░░░░░░░██  
  ██████░░░░░░░░░░░░░░░░░░▒▒██  
██▒▒▒▒▒▒██░░░░░░░░░░░░░░░░▒▒██  
██▒▒▒▒▒▒▒▒██░░░░░░░░░░░░▒▒██    
██▒▒▒▒▒▒▒▒██░░░░░░░░░░▒▒████    
  ██▒▒▒▒▒▒▒▒██▒▒▒▒▒▒████▒▒▒▒██  
    ██▒▒▒▒██████████▒▒▒▒▒▒▒▒▒▒██
      ██████      ████████████  
"""

# IMPORTS


# CONFIG


# AUTHOR INFORMATION
__author__ = "Tibo Smet"
__email__ = "tibo.smet@student.kdg.be"
__status__ = "Development"


class Liedje:
    def __init__(self, tekst):
        self.tekst = tekst

    def zingen(self):
        i = 0
        while i < len(self.tekst):
            print(self.tekst[i])
            i += 1


def main():
    liedjes_tekst = ["Lang zal ze leven", "Lang zal ze leven", "Lang zal ze leven in de gloria", "In de glo-ri-a",
                     "In de glo-ri-a"]
    verjaardagsliedje = Liedje(liedjes_tekst)
    verjaardagsliedje.zingen()


if __name__ == '__main__':
    main()
