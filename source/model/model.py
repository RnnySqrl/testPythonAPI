import csv
import requests
import json
from concurrent.futures import ThreadPoolExecutor

class model(object):

    def __init__(self):
        self.__data = list()
        executor = ThreadPoolExecutor(max_workers=2)
        executor.submit(self.__get_data_from_csv)
        executor.submit(self.__get_data_from_json_url())

    def __get_data_from_csv(self):
        with open('products.csv', 'r') as f:
            reader = csv.reader(f)
            headers = list()
            for row in reader:
                if reader.line_num == 1:
                    #clean fields
                    for item in row:
                        item = item.lower()
                        item = item.replace(" ","")

                        headers.append(item)
                else:
                    dic_row = dict()
                    for value, key in zip(row, headers):
                        #clean values
                        value = value.lower()
                        value = value.replace(" ", "")
                        value = value.replace("\"", "")
                        dic_row[key] = value

                    self.__data.append(dic_row)

    def __get_data_from_json_url(self):
        url = "https://s3-eu-west-1.amazonaws.com/pricesearcher-code-tests/python-software-developer/products.json"
        response = requests.get(url)
        json_text = response.text
        json_w = json.loads(json_text)
        for item in json_w:
            print(item)
            self.__data.append(item)

    def get_data(self):
        return self.__data