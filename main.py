from datagovscraper import DGS
import csv

path = input('Enter the API GET URL (ex: /resource/...): ')
inp_format = input('Enter the format of data (default is JSON): ')
lim = input('Enter the entry size (default is 10, leave blank for all): ')

if len(lim) == 0:
    query = DGS(path, get_format=inp_format)
else:
    query = DGS(path, get_format=inp_format, limit=lim)

print('Data has been queried. Converting to csv...')

decoded_content = query.json()
decoded_records = decoded_content['records']

filename = decoded_content['title'] + '.csv'
keys = decoded_records[0].keys()

with open(filename, mode='w', newline='') as file:
    dict_writer = csv.DictWriter(file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(decoded_records)

print(f'Output file "{filename}" is ready.')
