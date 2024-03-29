from time import localtime
from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/api", status_code=200)
async def root(slack_name: str, track: str):
    current_day = localtime().tm_wday
    utc_time = datetime.utcnow()
    github_file_URL = "https://github.com/Conradgabe/HNG-T-Scripts/blob/main/main.py"
    github_repo_URL = "https://github.com/Conradgabe/HNG-T-Scripts"
    
    day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if current_day:
        current_day = day_of_week[current_day]

    data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "track": track,
        "github_file_url": github_file_URL,
        "github_repo_url": github_repo_URL,
        "status_code": 200,
    }

    return data
