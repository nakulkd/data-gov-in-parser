from datagovscraper import DGS
import csv

path = input('Enter the API GET URL (ex: /resource/...): ')
inp_format = input('Enter the format of data (default is JSON): ')
lim = input('Enter the entry size (default is 10, leave blank for all): ')

if len(lim) == 0: # This is to speed up the query process.
    query = DGS(path, get_format=inp_format)
else:
    query = DGS(path, get_format=inp_format, limit=lim)

print('Data has been queried. Converting to csv...')

decoded_content = query.json()
decoded_records = decoded_content['records'] # hard-coded based on observed output

filename = decoded_content['title'] + '.csv' # output file will be named the same as the dataset
keys = decoded_records[0].keys()

with open(filename, mode='w', newline='') as file: # currently only works for JSON output and WILL THROW AN ERROR for all other types
    dict_writer = csv.DictWriter(file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(decoded_records)

print(f'Output file "{filename}" is ready.')
