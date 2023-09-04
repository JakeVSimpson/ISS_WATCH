from datetime import datetime
import requests
import smtplib
import time
LAT = 45.457963  # latitude
LONG = -75.71777  # longitude
def check_if_iss_is_close_enough():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    time_now = datetime.now()
    time = str(time_now).split(" ")[1][0:8]
    if LONG - 5 <= iss_longitude <= LONG + 5 and LAT - 5 <= iss_latitude <= LAT + 5: # check location
        if int(time[0:2]) < 6 or int(time[0:2]) > 20: # check time of day
            my_email = "EMAIL_FROM"
            password = "PASSWORD"
            connection = smtplib.SMTP("smtp.gmail.com", 587)
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="EMAIL_SENT_TO",
                                msg=f"Subject: ISS Above! \n\nThe ISS is above you <name>!")
            connection.close()
            print("Sent an email!")
        else:
            print("The ISS is above but it is not dark enough!")
    else:
        print("ISS is not close enough!")

parameters = {
    "lat": LAT,
    "lng": LONG,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

again = True;

while again:
    try:
        check_if_iss_is_close_enough()
        time.sleep(60) # wait 60 seconds
    except KeyboardInterrupt:
        time.sleep(.2)
        print("\nStopped on KeyboardInterrupt!")
        again = False


