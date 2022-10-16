###############################################################################################################################
# This code accesses census data and returns the county code (fips) based on address from user input                          #
#                                                                                                                             #
# Code is adapted from Mike Silva[1] at The Budding Data Scientist[2]. The Census Data API User Guide[3] was also referenced. #
#                                                                                                                             #
# [1] https://github.com/mikeasilva                                                                                           #
# [2] https://buddingdatascientist.wordpress.com/2019/01/10/using-census-geocoder-with-python/                                #
# [3] https://www.census.gov/content/dam/Census/data/developers/api-user-guide/api-guide.pdf                                  #
#                                                                                                                             #
###############################################################################################################################
---------------

import requests
import json
import urllib
import os

def get_url(address):
    # Convert spaces to plus signs
    address = address.replace(' ', '+')
    # Convert comma to %2C
    address = address.replace(',', '%2C')
    url = 'https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address='+address+'&benchmark=Public_AR_Current&format=json'
    return url

examp1 = 'Enter street number, Street, city, state, and zip code without punctuation.'
examp2 = 'Example: 1600 Pennsylvania Avenue NW Washington DC 20500'

cmd = "echo '{}\n{}'".format(examp1,examp2)
os.system(cmd)

address = input("Enter address: ")
 
response = requests.get(get_url(address))
 
data = requests.get(get_url(address)).text
 
data = json.loads(data)
 
coordinates = data['result']['addressMatches'][0]['coordinates']
 
lat = coordinates['y']
lng = coordinates['x']

#Encode Parameters
params = urllib.parse.urlencode({'latitude': lat, 'longitude':lng, 'format':'json'})

#Contruct request URL
url = 'https://geo.fcc.gov/api/census/block/find?' + params

#Get response from API
response = requests.get(url)

#Parse json in response
data = response.json()

#Print FIPS code
result = str(data['County']['FIPS'])
print("County code:", result[-3:])
