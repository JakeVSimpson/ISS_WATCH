# ISS Tracker

The ISS Tracker continuously monitors the position of the International Space Station (ISS) in relation to a specified location on Earth.

## How It Works?

The program fetches the current position of the ISS from the [Open Notify API](http://api.open-notify.org/iss-now.json) and checks whether it's within 5 degrees of latitude and 5 degrees of longitude of a specified location. If the ISS is nearby, the user will receive an email. Additionally, the program utilizes the [Sunrise and Sunset API](https://api.sunrise-sunset.org/json) to determine the sunrise and sunset times for the user's location.

### Components:

- **API Endpoint:** An API endpoint is used to fetch the live position of the ISS.
- **Python Time Module:** The python time module is used to loop at appropriate time intervals.

intervals.

- **SMTP Library:** The SMTP Library is used to notify the user when the ISS is close to their location.
- **PythonAnywhere:** The Python script is executed in the cloud through PythonAnywhere.

## Code Snippet

```python
from datetime import datetime
import requests
import smtplib
import time

# ... (rest of the code)

while again:
    try:
        check_if_iss_is_close_enough()
        time.sleep(60) # wait 60 seconds
    except KeyboardInterrupt:
        time.sleep(.2)
        print("\nStopped on KeyboardInterrupt!")
        again = False
```

## API Calls:

```python
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)

response = requests.get(url="http://api.open-notify.org/iss-now.json")
```
