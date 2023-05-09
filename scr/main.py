
import fastapi
import uvicorn
import pytest
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import httpx



app = FastAPI()
templates = Jinja2Templates(directory="public")
css_template = {}


@app.get("/", response_class=HTMLResponse)
def openweathermap(request: Request):
    city = "Moscow,ru"
    appid = '1fcf42d437cb6f743996878fc373bfcf'

    response = httpx.get("http://api.openweathermap.org/data/2.5/forecast",
                            params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = response.json()

    tmax = data['list'][0]['main']['temp_max']
    tmin = data['list'][0]['main']['temp_min']
    flike = data['list'][0]['main']['feels_like']
    press = data['list'][0]['main']['pressure']

    return templates.TemplateResponse("css_changeable.html", {'request':request, 'tmax': tmax, 'tmin': tmin, 'flike':flike, 'press':press, **css_template})


@app.post("/")
def post(content: dict):
    css_template.update(content)
    return {"message": "color is set successfully"}


@app.put("/{h1_color}")
def put(h1_color: str):
    css_template.update({"h1_color": h1_color})
    return {"message": "color is changed successfully"}


@app.delete("/")
def delete():
    css_template.pop("h1_color")
    return {"message": "color is deleted successfully"}
