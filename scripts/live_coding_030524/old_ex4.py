import pandas as pd

data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35], 
        'salary': ['$50,000', '$60,000', '$70,000']}

data_df = pd.DataFrame(data)


#lambda_salary = lambda string: 
string = '$50,000'

# for char in string:
#     if char == '$' or ',':
        
lambda_salary = lambda string: int(string.replace('$',''))

#age = 25
lambda_age = lambda x: 'young' if x < 30 else 'middle-aged'

#print(lambda_age(age))

#data_df['age'] = 

# data_df['new_age'] = 4#lambda_age(data_df['age'])

# print(data_df)
