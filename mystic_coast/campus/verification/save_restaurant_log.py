def log_restaurant(rest_name, rest_id, phone_num, loc):
    log = open(f'{rest_name}-{rest_id}.txt', 'w+')
    log.write(f'Name: {rest_name} \n')
    log.write(f'Phone #: {phone_num} \n')
    log.write(f'Location: {loc}')
    log.close()