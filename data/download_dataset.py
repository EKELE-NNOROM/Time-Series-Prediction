# !wget https://raw.githubusercontent.com/jbrownlee/Datasets/master/shampoo.csv
# !wget https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv

# import copy
import os
from subprocess import call

#print("")+,,,

print("Downloading...")
if not os.path.exists("airline-passengers.csv"):
    print('Downloading Airline Dataset')
    call(
        "wget https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv",
        shell=True
    )
    print('Downloading Shampoo Dataset')
    call(
        "wget https://raw.githubusercontent.com/jbrownlee/Datasets/master/shampoo.csv",
        shell=True
    )
    print("Downloading done.\n")
else:
    print("Datasets already downloaded. Did not download twice.\n")
