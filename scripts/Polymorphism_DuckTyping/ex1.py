import csv
import json
from abc import ABC, abstractmethod


class DataSource(ABC):
    '''Abtsract class for DataSource objects. It has a single "read_data" abstarct method,
       which has to be present in all subclasses. Because it is an abstract class, it cannot
       be instantiated'''
    
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path


    @abstractmethod
    def read_data(self)->None:
        '''Method to read a data file. The method here only provides the signature for corresponding
           methods in subclasses'''
        pass
        

class CSVDataSource(DataSource):
    '''Class to create CSVDataSource objects. It inherits from DataSource class'''
    
    def read_data(self)->dict:
        '''Method to read CSV data file and return it as a dictionary
           Parameters:
                * file_path: (String) the path of the file to be read
           Returns:
                * A dictionary containing the values of the CSV file. 
                The keys correspond to the headers of the CSV file; 
                the values are the columns stored as a list'''
        with open(self.file_path, 'r') as file:
            dictionary = {}
            for row in csv.DictReader(file):
                for key, value in row.items():
                    dictionary.setdefault(key, []).append(value)
            return dictionary


class JSONDataSource(DataSource):
    '''Class to create JSONDataSource objects. It inherits from DataSource class'''

    def read_data(self) -> dict:
        '''Method to read JSON data file and return it as a dictionary
           Parameters:
                * file_path: (String) the path of the file to be read
           Returns:
                * A dictionary containing the values of the JSON file. 
                The keys correspond to the same keys on each individual dictionary
                from json.load(). The values are lists with the values from json.load()'''
        with open (self.file_path, 'r') as file:
            dictionary = {}
            for row in json.load(file):  # NOTE: json.load() is a dictionary
                for key, value in row.items():
                    dictionary.setdefault(key, []).append(value)
            return dictionary


class TextDataSource(DataSource):
    '''Class to create TextDataSource objects. It inherits from DataSource class'''

    def __init__(self, file_path: str, delimeter: str =None) -> None:
        super().__init__(file_path)
        self.delimeter = '|' if delimeter is None else delimeter

    def read_data(self) -> dict:
        '''Method to read TXT data file and return it as a dictionary
           Parameters:
                * file_path: (String) the path of the file to be read
           Returns:
                * A dictionary containing the values of the TXT file. 
                The keys correspond to the headers of the TXT file; 
                the values are the columns stored as a list
           NOTE: the txt file must be separated by a pipe (|)'''
        with open(self.file_path, 'r') as file:
            read_file = file.read()
            dictionary = {}
            for line in read_file.split('\n')[1::]:
                for i, item in enumerate(line.split(self.delimeter)):
                    dictionary.setdefault(read_file.split('\n')[0].split(self.delimeter)[i], []).append(item)
            return dictionary
        

def merge_dictionaries(*args):
    '''Function to merge dictionaries with same keys. The values are lists with
       the values from each individual dictionary'''
    merged_dict = {}
    for dict in args:
        for key, value in dict.items():
            merged_dict.setdefault(key, []).extend(value)
    return merged_dict


def main():
    '''Function to merge many different dictionaries with common keys.
       The values will be lists containing all values from each dictionary '''
    
    # Instantiate CSVDataSource and load data
    csv_data = CSVDataSource(file_path='data/polymorphism_data.csv').read_data()

    # Instantiate JSONDataSource and load data
    json_data = JSONDataSource(file_path='data/polymorphism_data.json').read_data()

    # Instantiate TextDataSource and load data
    txt_data = TextDataSource(file_path='data/polymorphism_data.txt').read_data()

    return merge_dictionaries(csv_data, json_data, txt_data)


if __name__ == '__main__':

    # Use main function to merge all data dictionaries into one
    results = main()
    
    for key, value in results.items():
        print(f'{key}: {value}')




    # txt_data_source = TextDataSource()
    # txt_data = txt_data_source.read_data(file_path='data/polymorphism_data.txt')

    # print(txt_data)

   

    #data = DataSource().read_data(file_path='data/polymorphism_data.csv')
    # for key, value in data.items():
    #     print(f'{key}: {value}')


    # csv_data_source = CSVDataSource()
    # csv_data = csv_data_source.read_data(file_path='data/polymorphism_data.csv')
    # for key, value in csv_data.items():
    #     print(f'{key}: {value}')

    # print()
    # json_data_source = JSONDataSource()
    # json_data = json_data_source.read_data(file_path='data/polymorphism_data.json')
    # for key, value in json_data.items():
    #     print(f'{key}: {value}')
    
   

    


    # print(data)

    




