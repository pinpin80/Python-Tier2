from fastapi import FastAPI
from bangsue_codename import *
app = FastAPI()

arr_data = [1,2,3,4,5,6,7]


# Retrieve all data
@app.get("/")
async def get_data():
    return {"digits": arr_data}

@app.get("/tell-me-your-nume")
async def tell_me_your_nume(nume: str):
    return {"teo": arr_data}

@app.get("/tell-me-your-nay")
async def tell_me_your_nay(nume: str, nake: str,ding: str):
    return {"teo": nume,"you":nake,"popx":ding}

# Retrieve specific data by "digits"
@app.get("/ooooooo/{digits}")
async def specific_digits(digits: str):
    total=0
    for d in str(digits):
        total= int(total) * int(d)  + int(d)
    return {"digits": total}

# Add data
@app.post("/{digits}")
async def post_data(digits: int):
    arr_data.append(digits)
    return {"digits": arr_data}


# Update data by "index"
@app.put("/{from_digits}/{to_digits}")
async def put_data(from_digits: int, to_digits: int):
    arr_data[from_digits] = to_digits
    return {"digits": arr_data}


# Delete data by "digits"
@app.delete("/")
async def delete_data(digits: int):
    arr_data.remove(digits)
    return {"digits": arr_data}

# Delete data by "digits"
@app.get("/random")
async def random():
    pinpin=BangsueCodename.ThailandDistrict()
    codenaom=pinpin.get_code_name()
    return codenaom['province']