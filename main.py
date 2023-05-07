from datetime import datetime
import pytz

from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def read_root():
    time_gmt_minus_3 = datetime.now(pytz.timezone("Etc/gmt+3"))
    time_gmt_minus_5 = datetime.now(pytz.timezone("Etc/gmt+5"))
    return {
        "time_gmt-3" : time_gmt_minus_3,
        "time_gmt-5" : time_gmt_minus_5
    }

@app.get("/time/{zone}")
def read_time(zone: str):
    try:
        _zone = zone.replace('+', '-') if '+' in zone else zone.replace('-', '+')
        gmt_zone = pytz.timezone("Etc/" + _zone)
        current_time = datetime.now(gmt_zone)
    except pytz.UnknownTimeZoneError:
        raise HTTPException(status_code=400, detail="Invalid GMT timezone")
    
    return {
        "time" : current_time
    }