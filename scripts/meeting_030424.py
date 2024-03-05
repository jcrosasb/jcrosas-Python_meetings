import logging

# logging.basicConfig(level=logging.CRITICAL)

# logger = logging.getLogger(__name__)

# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')

logging.basicConfig(#filename='new_file.log', 
                    level=logging.DEBUG, 
                    format='%(module)s:%(funcName)s - %(levelname)s - %(message)s')
# format='[PID:%(process)d][TID:%(thread)d] %(levelname)s - %(message)s')
# format='%(module)s:%(funcName)s - %(levelname)s - %(message)s')
# format='[%(asctime)s] %(filename)s:%(lineno)d: %(message)s')

file_handler = logging.FileHandler('new_file_2.log')
file_handler.setLevel(logging.DEBUG)

# Create console handler and set level to INFO
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the root logger
logging.getLogger('').addHandler(file_handler)
logging.getLogger('').addHandler(console_handler)


logger = logging.getLogger(__name__)

def division(x, y):
    try:
        z = x/y
        logger.info(f'The division is {x}/{y}')
        return z
    except ZeroDivisionError as e:
        logger.error(e)
        return None
    finally:
        logger.debug('testing...')
    

print(division(6,4))