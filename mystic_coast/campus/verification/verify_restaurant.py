'''
    verification/verify_restaurant.py
    This file holds methods for the purpose of server-side validation of the 
    info sent by the user from add-restaurant.html
'''

import re

MIN_INPUT_LENGTH = 0
MAX_INPUT_LENGTH = 200

MIN_PHONE_LENGTH = 0
MAX_PHONE_LENGTH = 14

'''
PHONE_NUMBER_FORMAT = "(\d{3}) \w{3}-\w{4}"
LOCATION_FORMAT = "\w{1+} \w{1+} \w*, \w{1+}, \w{2}"
'''

def preliminary_info(name, location, phone_number):
    name_length = len(name)
    location_length = len(location)
    phone_number_length = len(phone_number)
  
    if (name_length <= MIN_INPUT_LENGTH 
        or name_length > MAX_INPUT_LENGTH):
        return "NAME_LENGTH"

    if (location_length <= MIN_INPUT_LENGTH 
        or location_length > MAX_INPUT_LENGTH):
        return "LOCATION_LENGTH"

    if (phone_number_length <= MIN_PHONE_LENGTH 
        or phone_number_length > MAX_PHONE_LENGTH):
        return "PHONE_LENGTH"

    return "SUCCESS"

    
