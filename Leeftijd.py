# !/usr/bin/env python

"""
            ／￣￣￣￣￣￣￣￣
　　　　　　  |　Een python script dat het volgende doet:
　　　　　　  |　1. vraagt achter je leeftijd
　　　　　　  |　2. berekent in welk jaar je geboren bent en dat ook als output meegeeft
　　　　　　  |　3. berekent in welk jaar je 50 jaar zal zijn en dat ook als output meegeeft
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
import datetime

# CONFIG
huidigJaar = datetime.datetime.now().year
leeftijd = 0

# AUTHOR INFORMATION
__author__ = "Tibo Smet"
__email__ = "tibo.smet@student.kdg.be"
__status__ = "Development"


def get_birthyear(age):  # Functie om het geboortejaar te berekenen.
    global huidigJaar
    geboortejaar = huidigJaar - age

    return geboortejaar


def get_year_when_50(age):  # Functie om het jaar waarin je 50 wordt te berekenen.
    birthyear = get_birthyear(age) + 50

    return birthyear


def main():
    global leeftijd
    print('Geef je leeftijd in:')
    try:
        leeftijd = int(input())
    except:
        print("Geef een geldige leeftijd in.")

    print('Je bent geboren in ' + str(get_birthyear(leeftijd)))
    print('Je zal 50 zijn in ' + str(get_year_when_50(leeftijd)))


if __name__ == '__main__':
    main()
