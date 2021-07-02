from Helper import Helper as h
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def handler():
  print(h.halko())
  return {'message': 'halkocentralko'}