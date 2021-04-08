# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time
from w1thermsensor import W1ThermSensor


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#function to initialize temp
def initialize(self):

    if read_temp() < 0:
        temp = 0
    else:
        temp = read_temp()

    return temp
#function to convert voltage to celsius
def volt_to_celsius(self, vin):


#function to read voltage uses volt to celsius function and returns temp in celsius
def read_temp(self, voltage):
    #supposed to mimic reading from resistance temp but we included voltage parameter to get a value
    return volt_to_celsius(voltage)
#function to send alert to console probably
def send_initial_alert(self, temp):
    log(temp)
    print("WARNING: Storage unit is 3 degrees away from reaching critical temperature!, dry ice refill is required!")


#Send warning function
def send_below_critical_alert(self, temp):
    log(temp)
    print("STORAGE UNIT IS BELOW CRITICAL TEMPERATURE! REFILL IS REQUIRED!")

#Write down into log (txt) file
def log(self, temp):


