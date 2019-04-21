'''
    verification/verify_item.py
    This file holds methods for the purpose of server-side validation of the 
    item fields sent by the user from restaurant-detail.html
'''

def preliminary_info(name, price):
    if len(name) <= 0 or len(name) > 50:
        return 'NAME_LENGTH'
    
    if float(price) < 0 or float(price) > 1000:
        return 'PRICE_VALUE'

    return 'SUCCESS'

        
