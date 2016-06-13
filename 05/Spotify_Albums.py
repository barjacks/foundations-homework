import requests

All_albums = ['7eyQXxuf2nGj9d2367Gi5f', '47xaqCsJcYFWqD1gwujl1T', '1DBkJIEoeHrTX4WCBQGcCi', '1oW3v5Har9mvXnGk0x4fHm', '6svTt5o2lUgIrgYDKVmdnD', '6V9YnBmFjWmXCBaUVRCVXP', '19RUXBFyM4PpmrLRdtqWbp', '7dxKtc08dYeRVHt3p9CZJn', '500FEaUzn8lN9zWFyZG5C2', '6400dnyeDyD2mIFHfkwHXN', '6xEJ4AkNz1FFNmDT2rbEjM', '1i0PpHKaS8cB02bliAGl6B', '2DCzgO12HyMeGxoQlbtvQV', '2yepd22RxJzI9RiLFiUQOZ', '57Y0vXSekxJYg9NqBmVSQc', '3GnpYI7e3khTNdzqdOTsVB', '4LCtg39OFoNMBVKJuLRTJe', '2CldtvVMJMGeQueLcdujQD', '1boM6qZahyCaz6Hh5b7tih']
print(type(All_albums))

for n in All_albums:
    url = "https://api.spotify.com/v1/albums/" + n
    #print(url)
    All_albums_urls = requests.get(url)
    All_albums_urls = All_albums_urls.json()
    #print(All_albums_urls)
    #All_albums.append(All_albums_urls)

print(All_albums_urls['name'], All_albums_urls['popularity'])

#for n in All_albums_urls:
#    print(n['name'], n['popularity'])
