import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

url = 'https://oreab.us.thentiacloud.net/rest/public/registrant/search/?keyword=all&skip=0&take=2000'
querystring = {"keyword":"all","skip":"0","take":"2000","lang":"en","type":"Dispensary","_":"1667739543013"}
payload = ""
response = requests.request("GET", url, data=payload, params=querystring)

data = response.json()
url_2 = f'https://oreab.us.thentiacloud.net/rest/public/registrant/get/?id={id}'


list_of_requests = []
for i in data['result']:
    id = i['id']
    url_2 = f'https://oreab.us.thentiacloud.net/rest/public/registrant/get/?id={id}'
    list_of_requests.append(url_2)



def get_data_dict(url):
    url_3 = url
    querystring = {"keyword":"all","skip":"0","take":"2000","lang":"en","type":"Dispensary","_":"1667739543013"}
    payload = ""
    response = requests.request("GET", url_3, data=payload, params=querystring)
    raw_data_dict = response.json()
    print(raw_data_dict)
    try:
        clean_data_dict = {'id': raw_data_dict['id'],
                           'firstName': raw_data_dict['firstName'],
                           'middleName': raw_data_dict['middleName'],
                           'lastName': raw_data_dict['lastName'],
                           'phone': raw_data_dict['phone'],
                           'email': raw_data_dict['email'],
                           'licenseNumber': raw_data_dict['licenseNumber'],
                           'licenseCategory': raw_data_dict['licenseCategory'],
                           'licenseStatus': raw_data_dict['licenseStatus'],
                           'initialLicenseDate': raw_data_dict['registrationRecords'][0]['initialRegistrationDate']
                           }


    except:
        clean_data_dict = {'id': raw_data_dict['id'],
                           'firstName': raw_data_dict['firstName'],
                           'middleName': raw_data_dict['middleName'],
                           'lastName': raw_data_dict['lastName'],
                           'phone': raw_data_dict['phone'],
                           'email': raw_data_dict['email'],
                           'licenseNumber': raw_data_dict['licenseNumber'],
                           'licenseCategory': raw_data_dict['licenseCategory'],
                           'licenseStatus': raw_data_dict['licenseStatus'],
                           'initialLicenseDate': raw_data_dict['initialLicenseDate'],
                           }

    return clean_data_dict


clean_list_of_data_dict = []

for r in list_of_requests:
    clean_list_of_data_dict.append(get_data_dict(r))

a = clean_list_of_data_dict[0].keys()

fieldnames1 = list(a)

with open('Appraiser.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames1)
    writer.writeheader()
    for dict in clean_list_of_data_dict:
        writer.writerow(dict)
