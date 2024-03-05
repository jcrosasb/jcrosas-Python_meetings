from typing import Any
import time

# # DECORATORS 
# def logger_on(afunction):
#     def wrapper(*args, **kwargs):
#         print(f'executing function {afunction.__name__}')
#         print(f'The parameters are args = {args} and kwargs = {kwargs}')
#         result = afunction(*args, **kwargs)
#         return result
#     return wrapper

# @logger_on
# def addition_funny(num1, num2):
#     return num1 + num2

# print(addition_funny(num1=2,num2=3))
# #print(logger_on(addition_funny)(num1=2, num2=3))  # Without decorator

# def monitor(afunction: Any):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = afunction(*args, **kwargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(f'Function {afunction.__name__} takes {execution_time} seconds to execute')
#         return result
#     return wrapper

# @monitor
# def sleeping(timer):
#     time.sleep(timer)
#     print('3 seconds passed')
#     return None

# sleeping(2)
# #monitor(sleeping)(2)  # Without decorator


# CLOSURES
