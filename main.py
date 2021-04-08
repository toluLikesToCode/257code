# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time
#from w1thermsensor import W1ThermSensor
from datetime import datetime
import csv

voltage = [0.3, 0.5, 0.7, 0.9, 2.1, 2.5, 3.0]
power = True
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#function to initialize temp
def initialize():

    if read_voltage(voltage[2]) < 0:
        temp = 0
    else:
        temp = read_voltage(voltage[2])

    return temp
#function to convert voltage to celsius
def volt_to_celsius(vin):
    return 2.0


#function to read voltage uses volt to celsius function and returns temp in celsius
def read_voltage(voltage):
    #supposed to mimic reading from resistance temp but we included voltage parameter to get a value
    temp_in_celsius = volt_to_celsius(voltage[4])
    log(temp_in_celsius)
    return temp_in_celsius

#function to send alert to console probably
def send_initial_alert(temp):
    log(temp)
    print("WARNING: Storage unit is 3 degrees away from reaching critical temperature!, dry ice refill is required!")

#function to read temp for an hour to check near critical temp
def read_for_hour():
    alert_sent = False
    t = time.time()
    while t <= (t+3600):
        temp = read_voltage(voltage[1])
        if (-80 > temp > -60) and not alert_sent:
            send_below_critical_alert(temp)
            alert_sent = True
        else: 
            log(temp)
        time.sleep(5*60)

    
#Send warning function
def send_below_critical_alert(temp):
    log(temp)
    print("STORAGE UNIT IS BELOW CRITICAL TEMPERATURE! REFILL IS REQUIRED!")

#Write down into log (txt) file
def log(temp):
    f = open("data.csv", "a")
    now = datetime.now()
    is_critical = "N"

    if -80 > temp > -60:
        is_critical = "Y"

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    f.write(f'{dt_string},{temp},{is_critical}')
    f.close()


if __name__ == '__main__':
    critical_temp = (-60, -80)
    initialize()
    while power:
        temp = read_voltage(voltage[1])

        if temp >= (critical_temp[0] - 3) or temp <= (critical_temp[1] + 3):
            send_initial_alert(temp)
            read_for_hour()
        elif critical_temp[0] > temp > critical_temp[1]:
            send_below_critical_alert(temp)
            read_for_hour()
        else:
            log(temp)
        time.sleep(3600)
            




