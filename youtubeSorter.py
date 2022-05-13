# Created on 11/05/22 by Nicolas Maes

import os
import requests
from datetime import datetime
import json
import csv
import pandas

# =============================================================================
# PARAMETRES A RENSEIGNER
# =============================================================================

playlistId = 'PLwLRwDvkU7GZCzjSVPq6m3QzEJ5xaIog4'

playlistName = "Shazam"

# =============================================================================
# VARIABLES
# =============================================================================

urlToFetchPlaylistData = "https://www.googleapis.com/youtube/v3/playlistItems"

urlToFetchVideotData = "https://www.googleapis.com/youtube/v3/videos"

key = 'AIzaSyCuQA9m0OeBZmMLXicw57vLarC20BKfrBs'

now = datetime.now().strftime("%d%m%Y")

querystringToFetchPlaylistData = {"part": "contentDetails", "maxResults": 50,
                                  "playlistId": playlistId, "key": key}

# =============================================================================
# CODE
# =============================================================================

# Appel à l'API de YouTube pour récupérer les infos de la playlist
# =============================================================================

payload = ""
response = requests.request(
    "GET", urlToFetchPlaylistData, data=payload, params=querystringToFetchPlaylistData)

playlistData = response.text

# Isolement des videoId
# =============================================================================

# Cette ligne est utile pour pouvoir bien boucler plus bas sur les données, mais pas pour écrire dans un fichier .json.
jsonLoadsPlaylist = json.loads(playlistData)

# On crée un tableau vide
videoIdArray = []
# On remplit ce tableau avec toutes les valeurs de videoId présentes dans le json reçu.
for x in jsonLoadsPlaylist["items"]:
    videoIdArray += [x["contentDetails"]["videoId"]]

jsonDumpsPlaylist = json.dumps(videoIdArray)

with open("listVideoId.json", 'w') as outfile:
    outfile.write(jsonDumpsPlaylist)

# Appel à l'API de YouTube pour récupérer les infos d'une vidéo
# =============================================================================

# On crée un tableau vide
result = []

# Pour chaque id d'une vidéo, on lance la requête à l'API de Youtube pour récupérer les données de cette vidéo.
for singleVideo in videoIdArray:
    querystringToFetchVideotData = {"id": singleVideo,
                                    "part": "contentDetails,snippet", "key": key}

    payload = ""
    response = requests.request(
        "GET", urlToFetchVideotData, data=payload, params=querystringToFetchVideotData)

    videoData = response.text

# Isolement des videoId
# =============================================================================

# Cette ligne est utile pour pouvoir bien boucler plus bas sur les données, mais pas pour écrire dans un fichier .json.
    jsonLoadsVideo = json.loads(videoData)

# TOUJORUS DANS CETTE BOUCLE
# =============================================================================

# On crée un tableau vide
    videoDataWanted = []
    # utiliser les dictionnaire Python
# On remplit ce tableau avec toutes les valeurs souhaitées depuis le json reçu.
    for x in jsonLoadsVideo["items"]:
        videoDataWanted += {x["id"]}
        videoDataWanted += {x["snippet"]["channelTitle"]}
        videoDataWanted += {x["snippet"]["title"]}
        videoDataWanted += {x["contentDetails"]["duration"]}
        videoDataWanted += {x["snippet"]["publishedAt"]}

    result += [videoDataWanted]

jsonDumpsVideo = json.dumps(result, indent=4)

with open("z.json", 'w') as outfile:
    outfile.write(jsonDumpsVideo)


# J'arrive à isoler les données que je veux (d'une vidéo) mais je dois ajouter les clés des valeurs
