# ClickCounter

Count number of clicks of the clicker repo button

To run:

```
python -m flask run or gunicorn --workers 2 --bind 0.0.0.0:5000  app:app
```

Example payload:

```
{
    "country": "US",
    "ip": "123.123.123.123"
}
```
