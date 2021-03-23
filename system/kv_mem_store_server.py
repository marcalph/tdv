""" implement simple server that use query param 
    to store key/value pairs with 
"""
# stdlib
from typing import Dict

import uvicorn
from fastapi import FastAPI
app = FastAPI()


mem = {}
@app.post('/memory/{key}')
def post_data_mem(key, data: Dict):
    print(f"POST request with query param {key}")
    mem[key]=data.get("data")
    return 


@app.get('/memory/{key}')
def get_datamem(key):
    print(f"GET request with query param {key}")
    if key in mem.keys():
        return mem[key]
    else: 
        return 


if __name__ == '__main__':
    uvicorn.run(app)