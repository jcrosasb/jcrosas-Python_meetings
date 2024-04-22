import pandas as pd

data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35], 
        'salary': ['$50,000', '$60,000', '$70,000']}

data_df = pd.DataFrame(data)

# Clean salary column
data_df['salary'] = data_df['salary'].apply(lambda string: int(string.replace('$','').replace(',','')))

# Add 'tax' column
data_df['tax'] = data_df['salary'].apply(lambda salary: salary*0.20 if salary > 50_000 else salary*0.15)

# Add age range
data_df['age_range'] = data_df['age'].apply(lambda x: 'young' if x < 30 else 'middle-aged')

print(data_df)
