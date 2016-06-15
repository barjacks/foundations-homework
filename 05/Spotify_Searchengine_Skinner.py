import requests

#Finding the Artists
Favorite_Artists = input("What is your favorite artist or band on Spotify? ")
#print(Favorite_Artists)

response = requests.get("https://api.spotify.com/v1/search?query=" + Favorite_Artists + "&type=artist&limit=50&market=US")
Favorite_Artists = response.json()

#printing our the list
Favorite_Artists_List = Favorite_Artists['artists']['items']
#numbering the list
artist_number = 0
artist_list_numbered = []
for artist in Favorite_Artists_List:
    artist_number = artist_number + 1
    print(artist_number, artist['name'])
    artist_list_numbered.append(artist['name'])
#print(artist_list_numbered)

print('There are', Favorite_Artists['artists']['total'], 'Artists with that in their name.')
if Favorite_Artists['artists']['total'] > 50:
    print("Above we have printed the top 50 for you. If the artist you are looking for, is not among the data, please refine your search.")

#Which artist was the user looking for?
artist_number_input = input("Which artist were you looking for? Please enter the corresponding number? ")
artist_number_input = int(artist_number_input) - 1
#print(artist_list_numbered[artist_number_input])
artist = artist_list_numbered[artist_number_input]
print(artist)

#defining the aritsts ID
for n in Favorite_Artists_List:
    if n['name'] == artist:
        #print(n['name'], n['id'])
        artist_ID = n['id']

#importing the artist's data
response = requests.get("https://api.spotify.com/v1/artists/" + artist_ID + "/top-tracks?country=US")
Artist_data = response.json()

print("Here's a list of top tracks by", artist)
for tracks in Artist_data['tracks']:
    print(tracks['name'])

#looking up the artist's top album
response = requests.get("https://api.spotify.com/v1/artists/" + artist_ID + "/albums?country=US")
Artist_album_data = response.json()

#print(Artist_album_data['items']) and create a list of the ids
album_id_list = []
#print("Here's a list of", artist, "albums:")
for Album in Artist_album_data['items']:
    #print(Album['name'], Album['id'])
    album_id_list.append(Album['id'])
#print(album_id_list)
#type(album_id_list)

#Getting The popularity score of each album:
All_albums = []
for n in album_id_list:
    url = "https://api.spotify.com/v1/albums/" + n
    #print(url)
    All_albums_urls = requests.get(url)
    All_albums_urls = All_albums_urls.json()
    #print(All_albums_urls)
    All_albums.append(All_albums_urls)

#print(All_albums)
#print(type(All_albums))

#Getting the album names and popularity scores of the album
most_popular_album_name = ""
most_popular_album = 0
for n in All_albums:
    if n['popularity'] > most_popular_album:
        most_popular_album_name = n['name']
        most_popular_album = n['popularity']
print("The most popular album of", artist, "is", most_popular_album_name, "with a popularity score of:", most_popular_album)

least_popular_album_name = ""
least_popular_album = 100
for n in All_albums:
    if n['popularity'] < least_popular_album:
        least_popular_album_name = n['name']
        least_popular_album = n['popularity']

print("The least popular album of", artist, "is", least_popular_album_name, "with a popularity score of:", least_popular_album)
