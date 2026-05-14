from fastapi import FastAPI, Path, HTTPException,Query
import json
from pydantic import BaseModel,Field,computed_field
from typing import Annotated, Optional 
from fastapi.responses import JSONResponse



class Showcase(BaseModel):

    id:Annotated[str,Field(...,description="id of showcase",examples=["1"])]
    name:Annotated[str,Field(...,description="name of showcase")]
    model:Annotated[str,Field(...,description="model of showcase")]
    category:str
    price:Optional[float]=None

    @computed_field(return_type=str)
    @property
    
    def full_name(self):
        return f"{self.name}-{self.model}"


class ShowcaseUpdate(BaseModel):
    name:Annotated[Optional[str],Field(...,description="name of showcase")]
    model:Annotated[Optional[str],Field(...,description="model of showcase")]
    category:Optional[str]
    price:Optional[float]=None


# to load data from showcase.json
def load_data():
    with open("showcase.json","r") as f:
        data=json.load(f)
    return data


# to save data
def save_data(data):
    with open("showcase.json", "w") as f:
        json.dump(data, f, indent=4)



app=FastAPI()    #app object

# fdefine end point (retrieve endpoints)
@app.get("/")     #define routing:
def hello():
    return {"message": "Showcase Management system API"}

@app.get("/about")
def about():
    return {"message":"Fully funcional API to know about showcases"}

@app.get("/view")
def view():
    data=load_data()
    return data


@app.get("/showcase/{showcase_id}")
def view_showcase(showcase_id:int=Path(...,description="id of showcase", gt=0, examples=1)):
    
    #load all data
    data=load_data()
    showcases=data["showcase"]

    for item in showcases:
        if item["id"]==showcase_id:
            return item
    raise HTTPException(status_code=404,detail="showcase not found")


@app.get("/sort")

def sort_showcase(sort_by:str=Query(...,description="sort on basis of name, model and category"),order:str=Query("asc",description="sort in asc or desc order")):
    valid_fields=["name","model","category"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f"Invalid field select from {valid_fields}")
    
    if order not in ["asc","desc"]:
        raise HTTPException(status_code=400, detail="Invalid order select between asc and desc")
    
    data=load_data()
    showcases = data["showcase"]
    reverse = (order == "desc")

    sorted_data = sorted(
        showcases,
        key=lambda x: x.get(sort_by, ""),
        reverse=reverse
    )

    return sorted_data



# Post (Create) endpoints

@app.post("/create")

def create_showcase(showcase:Showcase):

    #load existing data
    data=load_data()
    

    # check showcase already exist.

    for item in data["showcase"]:
        if item["id"]==showcase.id:
            raise HTTPException(status_code=400,detail="id already exist")

    # New showcase to database
    
    data["showcase"].append(showcase.model_dump())   #model_dump() is a Pydantic method used to generate a dictionary representation of a Pydantic model instance.
    
    #save into the json file
    save_data(data)
    return JSONResponse(status_code=201, content={"message":"showcase created successfully"})



# PUT and DELETE Endpoints

@app.put("/edit/{showcase_id}")

def update_showcase(showcase_id:str, showcaseupdate:ShowcaseUpdate):    #  showcaseupdate variable brings info from client and we receive that info froom basemodel showcaseupdate

    data=load_data()

    showcases=data["showcase"]

    for item in showcases:
        if item["id"]==showcase_id:
            updated_showcase_info=showcaseupdate.model_dump(exclude_unset=True) #converts  Pydantic model into a dictionary.
            for key,value in updated_showcase_info.items():
                item[key]=value
        save_data(data)
        return JSONResponse(status_code=200,content={"message":"showcase updated"})

    raise HTTPException(status_code=404, detail="showcase not found")


@app.delete("/delete/{showcase_id}")

def delete_showcase(showcase_id:str):

    #load data
    data=load_data()

    showcases=data["showcase"]

    for index,item in enumerate(showcases):
        if item["id"]==showcase_id:
            del showcases[index]
            save_data(data)
            return JSONResponse(status_code=200, content={"message":"Showcase info deleted"})

    raise HTTPException(status_code=404, detail="Showcse not found")
    
