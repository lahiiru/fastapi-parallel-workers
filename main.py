from fastapi import FastAPI
import random
app = FastAPI()
class Context:
    active = True

@app.get("/rotate")
def rotate():
    Context.active = True
    x = 0
    while Context.active:
        x = random.randrange(10)
    return x
    
@app.get("/stop")
def stop():
    Context.active = False
    return "Wheel running job stopped. See the rotate request output now to see the lucky number."