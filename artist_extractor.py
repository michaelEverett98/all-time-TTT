import pandas as pd
import numpy as np
import re
# import matplotlib.pyplot as plt
# import matplotlib.patheffects as pe
# import warnings

# pd.set_option("display.max_rows", None)
# pd.set_option("display.max_columns", None)
# pd.set_option("display.width", None)

print("Loading csv file...")

rateCsv = pd.read_csv("song_stats_sheet.csv", header = 0, sep = ",")
rateCsvTrim = rateCsv.drop(["Artist", "Year", "Unnamed: 4", "Controv.", "P#","Unnamed: 10", "11s", "≥10", "≥9", "<5", "<3", "0s","Unnamed: 18", "11%", "≥10%", "≥9%", "<5%", "<3%", "0%", "Unnamed: 25", "Bonus", "Date", "CU", "Win"], axis = 1)
rateCsvColumn = rateCsvTrim.rename(columns = {"Unnamed: 0": "Placement"})
rateCsvColumn.loc[rateCsvColumn["MainArtist"] == "2:00 PM", "MainArtist"] = "2PM"
rateCsvColumn.loc[rateCsvColumn["MainArtist"] == "2:00 AM", "MainArtist"] = "2AM"
#rateCsvColumn.loc[rateCsvColumn["Placement"] != "", "Placement"] = ""

print("Csv file successfully loaded.")

# print(rateCsvColumn.columns)

artistList = rateCsvColumn["ArtistList"]
# print(rateCsvColumn["ArtistList"])

def extractArtists(artists) :

    artistArray = []

    print(f"Extracting artists...")

    for x in range(len(artists)) :

        if re.search(r'\b; ' + ';', rateCsvColumn["ArtistList"][x]) not in artistArray :

            artistArray.append(re.search(r'\b; ' + ';', rateCsvColumn["ArtistList"][x]))

        elif rateCsvColumn["MainArtist"][x] not in artistArray :

            artistArray.append(rateCsvColumn["MainArtist"][x])

        else :

            pass

    return(artistArray)

artistTemp = sorted([x for x in extractArtists(artistList) if x is not None], key = str.casefold)
# #artistTemp.sort()
# print(artistTemp)

df = pd.DataFrame(artistTemp)
df.to_csv("rated_artists_2.csv", index = True, header = False, encoding = "utf-8-sig")