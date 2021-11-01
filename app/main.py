import json

from fastapi import FastAPI,Request
from fastapi.response import HTMLResponse
from fastapi.templating import jinja2Templates
 
app = FastAPI()

@app.get("/",response_class=HTMLResponse)
def home_view(request: Request):
    return

@app.post("/")
def home_detail_view():
    return{"hello":"world"}