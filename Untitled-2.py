@app.get("/ice cream")
def ice cream(m: str,p: str):
    return {"message":f"My name is {m},{p}"}