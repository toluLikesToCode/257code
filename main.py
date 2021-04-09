# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time
# from w1thermsensor import W1ThermSensor
from datetime import datetime
import csv

voltage = ["0.3", "0.5", "0.7", "0.9", "2.1", "2.5", "2.2"]


# function to initialize temp
def initialize():
    if read_voltage() < 0:
        temp = 0
    else:
        temp = read_voltage()

    return temp

#tolu

# function to convert voltage to celsius
def volt_to_celsius(vin):
    t = (((694.42) * ((2.7882 - float(vin)) / (6.2118 - float(vin)))) - 100) * (1 / 0.385)
    return t


# function to read voltage uses volt to celsius function and returns temp in celsius
def read_voltage():
    # supposed to mimic reading from resistance temp but we included voltage parameter to get a value
    v = voltage[4]
    return v



# tolu

# function to send alert to console probably
def send_initial_alert(temp):
    log(temp)
    print("WARNING: Storage unit is close to reaching critical temperature!, dry ice refill is required!")


# function to read temp for an hour to check near critical temp
def read_for_hour():
    alert_sent = False
    times = time.time()
    t = times
    while t <= (times + 3600):
        temp = read_voltage()
        if (-80 > temp > -60) and not alert_sent:
            send_below_critical_alert(temp)
            alert_sent = True
        else:
            log(temp)
        t = time.time()
        time.sleep(60)


# tolu

# Send warning function
def send_below_critical_alert(temp):
    log(temp)
    print("STORAGE UNIT IS BELOW CRITICAL TEMPERATURE! REFILL IS REQUIRED!")

# tolu

# Write down into log (txt) file
def log(temp):
    f = open("data.csv", "a")
    now = datetime.now()
    is_critical = "N"

    if temp >= -60 or temp <= -80:
        is_critical = "Y"

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    f.write(f'{dt_string} ,{temp},{is_critical}\n')
    f.close()


def hourly_read():
    critical_temp = (-60, -80)
    if initialize() >= 0:
        while True:
            v = read_voltage()
            temp = volt_to_celsius(v)

            if (critical_temp[0] >= temp >= critical_temp[0] - 3) or (
                    temp <= critical_temp[1] + 3 and temp <= critical_temp[1]):
                send_initial_alert(temp)
                read_for_hour()
            elif temp > critical_temp[0] or temp < critical_temp[1]:
                send_below_critical_alert(temp)
                read_for_hour()
            else:
                log(temp)
            time.sleep(3600)


if __name__ == '__main__':
    initialize()
    hourly_read()
