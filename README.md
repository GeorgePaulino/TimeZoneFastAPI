
# TimeZone - FastAPI

API to get time from a certain GMT timezone.

This project has deployed at: https://gtimezone.onrender.com/

You can pass as parameter the GMT timezone as the sample:

https://gtimezone.onrender.com/time/gmt-3
https://gtimezone.onrender.com/time/gmt+7

## Run Locally

Clone the project:

```bash
  git clone https://github.com/GeorgePaulino/TimeZoneFastAPI
  cd TimeZoneFastAPI
```

Install dependencies and run the server:

```bash
  pip install -r requirements.txt
  uvicorn main:app --reload
```

After access http://localhost:8000/