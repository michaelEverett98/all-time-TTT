def shred(resList) :
    pass

import pandas as pd
from ast import literal_eval

df = pd.read_csv("responses_array.csv", header = 0, sep = ",")

df["song_artists"] = df["song_artists"].apply(literal_eval)
df["nickname"] = df["nickname"].apply(literal_eval)

def gatekeep(resList, nickname) :

    cfList = [x.casefold() for x in resList]

    if "itzy" in cfList :

        print(f"{nickname}'s list has been approved.")
        #pass

    else :

        print(f"{nickname}'s list has been gatekept. Shredding list...")
        shred(resList)

def listAppend(resList) :

    initList = []

    for x in resList :

        initList.append(x)

    return(initList)

for i, row in df.iterrows() :

    responseArtists = df["song_artists"][i]
    userNick = df["nickname"][i]
    artistList = listAppend(responseArtists)

    gatekeep(artistList, userNick)