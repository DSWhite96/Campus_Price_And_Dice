'''
    verification/verify_compare.py
    This file holds methods for the purpose of server-side validation of the 
    info sent by the user from compare-restaurants.html
'''

def restaurant_names(first_name, second_name):
    if first_name == second_name:
        return 'DUPLICATE_NAME'
    
    if first_name == '' or second_name == '':
        return 'EMPTY_NAME'

    return 'SUCCESS'