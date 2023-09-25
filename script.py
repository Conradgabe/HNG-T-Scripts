from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def all_url_links():
    data = {
        "Github Repo": "https://github.com/Conradgabe/Token-Auth-with-FastAPI",   
        "Hosted Endpoint": "https://tkauth.onrender.com/",   
        " Documentation URL": "https://github.com/Conradgabe/Token-Auth-with-FastAPI/blob/main/DOCUMENTATION.md"
    }
    return data