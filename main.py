from fastapi import FastAPI
import random

app = FastAPI()

class Context:
    """
    A class to hold job active flag amoung the application context
    """
    active = True

@app.get("/rotate")
def rotate():
    Context.active = True
    n = 0
    while Context.active:
        n = random.randrange(10)
    return f"Your lucky number is {n}!"
    
@app.get("/stop")
def stop():
    Context.active = False
    return "Wheel running job stopped. See the rotate request output now to see the lucky number."
