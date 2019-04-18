'''
    verification/add_restaurant.py
    This file holds methods for the purpose of server-side validation of the 
    info sent by the user from add-restaurant.html
'''

import re

MIN_INPUT_LENGTH = 0
MAX_INPUT_LENGTH = 200
PHONE_NUMBER_FORMAT = "(\d{3}) \w{3}-\w{4}"
LOCATION_FORMAT = "\w{1+} \w{1+} \w*, \w{1+}, \w{2}" #Subject to change

class Verify():

    ''' MIN_INPUT_LENGTH = 0
    MAX_INPUT_LENGTH = 200
    PHONE_NUMBER_FORMAT = "(\d{3}) \w{3}-\w{4}"
    LOCATION_FORMAT = "\w{1+} \w{1+} \w*, \w{1+}, \w{2}" #Subject to change'''
  
    def preliminary_info(name, location, phone_number):
        name_length = len(name)
        location_length = len(location)
        
        phone_number_regex = re.compile(phone_number)
        is_phone_number_correct = phone_number_regex.match(PHONE_NUMBER_FORMAT)
        #is_location_correct = ...
        
        if (not is_phone_number_correct):
            return "PHONE_NUMBER"

        if (MIN_INPUT_LENGTH < name_length <= MAX_INPUT_LENGTH):
            return "NAME_LENGTH"

        if not (MIN_INPUT_LENGTH < location_length <= MAX_INPUT_LENGTH):
            return "LOCATION_LENGTH"

        return "SUCCESS"
    
