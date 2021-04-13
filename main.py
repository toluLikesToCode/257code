# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time
# from w1thermsensor import W1ThermSensor
from datetime import datetime
import csv



# function to initialize temp
def initialize():
    """
    Initializes voltage reading to not return negative values
    :return:
        v - voltage read from Arduino or 0 to initialize voltage
    """
    v = float(read_voltage())
    if v < 0:
        v = 0

    return v

#tolu

# function to convert voltage to celsius
def volt_to_celsius(vin):
    t = (((694.42) * ((2.7882 - float(vin)) / (6.2118 - float(vin)))) - 100) * (1 / 0.385)
    return t


# function to read voltage uses volt to celsius function and returns temp in celsius
def read_voltage():
    """
    Mimics an arduino voltage reading, using an assigned voltage value from a list
    that can be changed for testing.
    :return:
        v - voltage read from arduino
    """
    voltage = ["-0.3", "2.4", "2.365", "2.3", "2.415", "2.408"]
    #negative value of voltage
    #v = voltage[0]

    #within ideal temp ~ -76 C
    #v = voltage[1]

    #within -60 C and -63 C should send intial alert
    #v = voltage[2]

    # ~ -34 C should send below critical alert
    #v = voltage[3]

    #below critical ~ -82 C should send below critical
    #v = voltage[4]

    #near critical ~79 C should send initial alert
    #v = voltage[5]

    v = voltage[4]
    return v



# tolu

# function to send alert to console probably
def send_initial_alert(temp):
    log(temp)
    print("WARNING: Storage unit is close to reaching critical temperature!, dry ice refill is required!")


# function to read temp for an hour to check near critical temp
def read_for_hour():
    """
    Function to read and log temperature every minute for an hour.
    If temperature reaches below critical temperature a critical alert is
    sent the first time, then not repeated. Uses time module to track time.
    """
    alert_sent = False
    times = time.time()
    t = times
    while t <= (times + 3600):
        v = read_voltage()
        temp = volt_to_celsius(v)
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
    """
    Function that reads and logs temperature every hour.
    It makes the necessary checks to see if the sensor returns values
    near critical temperature and sends initial alert, below critical
    temperature alert, or simply logs the temperature. It is an infinite
    loop that runs whenever program is on.

    """
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
    hourly_read()
