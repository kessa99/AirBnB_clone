#!/usr/bin/python3
from models.base_model import BaseModel

class Place(BaseModel):
    """Represents a place.

    Attributes:
        city_id: string-empty string
        user_id : atring-empty string
        name : name in string
        description : The description of the place in string
        number_rooms : The number of rooms type int
        number_bathrooms : The number of bathrooms is an int
        max_gest : number of guest int type
        price_by_night : the prix attribuate
        latitude :  coordonate of place
        longitude : second coordonne of place
    """
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
