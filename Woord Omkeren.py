# !/usr/bin/env python

"""
            ／￣￣￣￣￣￣￣￣
　　　　　　  |　Schrijf een script waarbij je om input vraagt achter een willekeurig woord en waarbij het script
　　　　　　  |　het woord achterstevoren weergeeft.
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


def omkeren(w):                                         # Functie om het opgegeven woord om te keren.
    omgekeerd = ""
    for letter in reversed(w):
        omgekeerd += letter

    return omgekeerd


def main():
    print("Geef een woord in.")
    woord = input()

    print(omkeren(woord))


if __name__ == '__main__':
    main()
