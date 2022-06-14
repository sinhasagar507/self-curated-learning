from pydantic import BaseModel, Field
from typing import Union


class HouseFeatures(BaseModel):
    overallQuality: Union[str, None] = Field(None, example="Excellent")
    # livingRoomArea: Union[int, None] = Field(None, example=1800, description="Measured in square feet. Enter a value between 334 and 5462 inclusive", ge=334, le=5462)
    # basementArea: Union[int, None] = Field(None, example=2000, description="Measured in square feet. Enter a value between 0 and 6110 inclusive", ge=0, le=6110)
    # firstFloorArea: Union[int, None] = Field(None, example=4000, description="Measured in square feet. Enter a value between 334 and 4692 inclusive", ge=334, le=4692)
    # firstFlrConsArea: Union[int, None] = Field(None, example=5000, description="Measured in square feet. Enter a value between 0 and 5664 inclusive", ge=0, le=5664)
    # secondFlrTotArea: Union[int, None] = Field(None, example=2000, description="Measured in square feet. Enter a value between 0 and 2065 inclusive", ge=0, le=2065)
    # lotArea: Union[int, None] = Field(None, example=3000, description="Measured in square feet. Enter a value between 1300 and 21500 inclusive", ge=1300, le=21500)
    # yrBlt: Union[int, None] = Field(None, example=2002, description="Year range between 1872 and 2010 inclusive", ge=1872, le=2010)
    # bathAboveGrade: Union[int, None] = Field(None, example=2, description="Enter a value between 0 and 3 inclusive", ge=0, le=3)
    # yrGarageBlt: Union[int, None] = Field(None, example=2002, description="Year range between 1895 and 2010 inclusive", ge=1895, le=2010)
    # porchArea: Union[int, None] = Field(None, example=500, description="Measured in square feet. Enter a value between 0 and 742 inclusive", ge=0, le=742)
    # garageArea: Union[int, None] = Field(None, example=700, description="Measured in square feet. Enter a value between 0 and 1448 inclusive", ge=0, le=1448)
    # garageCarCap: Union[int, None] = Field(None, example=2, description="Enter a value between 0 and 5 inclusive", ge=0, le=5)

    livingRoomArea: Union[str, None] = Field(None, example="1800", description="Measured in square feet. Enter a value between 334 and 5462 inclusive")
    basementArea: Union[str, None] = Field(None, example="2000", description="Measured in square feet. Enter a value between 0 and 6110 inclusive")
    firstFloorArea: Union[str, None] = Field(None, example="4000", description="Measured in square feet. Enter a value between 334 and 4692 inclusive")
    firstFlrConsArea: Union[str, None] = Field(None, example="5000", description="Measured in square feet. Enter a value between 0 and 5664 inclusive")
    secondFlrTotArea: Union[str, None] = Field(None, example="2000", description="Measured in square feet. Enter a value between 0 and 2065 inclusive")
    lotArea: Union[str, None] = Field(None, example="3000", description="Measured in square feet. Enter a value between 1300 and 21500 inclusive")
    yrBlt: Union[str, None] = Field(None, example="2002", description="Year range between 1872 and 2010 inclusive")
    bathAboveGrade: Union[str, None] = Field(None, example="2", description="Enter a value between 0 and 3 inclusive")
    yrGarageBlt: Union[str, None] = Field(None, example="2002", description="Year range between 1895 and 2010 inclusive")
    porchArea: Union[str, None] = Field(None, example="500", description="Measured in square feet. Enter a value between 0 and 742 inclusive")
    garageArea: Union[str, None] = Field(None, example="700", description="Measured in square feet. Enter a value between 0 and 1448 inclusive")
    garageCarCap: Union[str, None] = Field(None, example="2", description="Enter a value between 0 and 5 inclusive")
    overallCond: Union[str, None] = Field(None, example="Average")

    class Config:
        schema_extra = {
            "example": {
                "overallQuality": "Excellent",
                "livingRoomArea": "1800",
                "basementArea": "2000",
                "firstFloorArea": "8000",
                "firstFlrConsArea": "5000",
                "secondFlrTotArea": "7000",
                "lotArea": "3000",
                "yrBlt": "2002",
                "bathAboveGrade": "5",
                "yrGarageBlt": "2002",
                "porchArea": "1000",
                "garageArea": "700",
                "garageCarCap": "2",
                "overallCond": "Average"
            }
        }
