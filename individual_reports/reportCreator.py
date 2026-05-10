# Want to keep the file to generate the reports separately, so I don't have to do it every time I want to check new submissions

import pandas as pd
import numpy as np
from ast import literal_eval
from collections import Counter
import warnings

print(f"Disabling warning messages...")
warnings.filterwarnings("ignore")

pd.set_option("display.max_columns", None)

def linebreak() :

    print("====================")

# ==================================================
# Company artist arrays
# ==================================================

ygSoloists = ["B.I", "CL", "Daesung", "G-Dragon", "Jennie", "Jeon Somi", "Jisoo", "Lisa", "Rosé", "Taeyang"]

ygGroups = ["2NE1", "AKMU", "Allday Project", "Babymonster", "BIGBANG", "Blackpink", "Epik High", "GD x Taeyang", "iKon", "izna", "Jus2", "MEOVV", "miss A", "Treasure", "Winner"]

smSoloists = ["Baekhyun", "BoA", "Chen", "Doyoung", "Irene", "Jaehyun", "Jonghyun", "Joy", "Kai", "Key", "Mark", "Max Changmin", "Minho", "Onew", "Seulgi", "Sulli", "Taemin", "Taeyeon", "Taeyong", "Ten", "Wendy", "Yuta"]

smGroups = ["aespa", "EXO", "EXO-CBX", "f(x)", "Girls' Generation", "GOT the beat", "H.O.T.", "Hearts2Hearts", "NCT 127", "NCT Dojaejung", "NCT Dream", "NCT U", "NCT Wish", "Red Velvet", "Red Velvet I&S", "RIIZE", "SHINee", "Super Junior", "SuperM", "TVXQ", "WayV"]

jypeSoloists = ["J.Y. Park", "Jihyo", "Nayeon", "Park Jiyoon", "Rain", "Sunmi", "Tzuyu", "Yeji"]

jypeGroups = ["2AM", "2PM", "DAY6", "GOT7", "ITZY", "NMIXX", "Stray Kids", "Twice", "Twice/MISAMO", "Wonder Girls", "Xdinary Heroes"]

hybeSoloists = ["Agust D", "Beomgyu", "j-hope", "Huh Yunjin", "Jimin", "Jin", "Jungkook", "RM", "V", "Yeonjun"]

hybeGroups = ["BOYNEXTDOOR", "BTS", "Enhypen", "ILLIT", "Katseye", "LE SSERAFIM", "NewJeans","NU'EST", "NU'EST W", "Seventeen", "TWS", "TXT"]

ygArtists = ygSoloists + ygGroups
smArtists = smSoloists + smGroups
jypeArtists = jypeSoloists + jypeGroups
hybeArtists = hybeSoloists + hybeGroups

# ==================================================
# Loading rate file CSV
# ==================================================

print("Loading csv file...")
rateCsv = pd.read_csv("data/song_stats_sheet.csv", header = 0, sep = ",")
rateCsv["Company alignment"] = ""
# rateCsv["Num songs"] = "" # For calculating number of songs in rate
rateCsv = rateCsv.drop(["Year", "Unnamed: 4", "Controv.", "/","P#","Unnamed: 10", "11s", "≥10", "≥9", "<5", "<3", "0s","Unnamed: 18", "11%", "≥10%", "≥9%", "<5%", "<3%", "0%", "Unnamed: 25", "Bonus", "Date", "CU"], axis = 1)
rateCsv = rateCsv.rename(columns = {"#": "Placement"})
rateCsv.loc[rateCsv["MainArtist"] == "2:00 PM", "MainArtist"] = "2PM"
rateCsv.loc[rateCsv["MainArtist"] == "2:00 AM", "MainArtist"] = "2AM"
# rateCsvColumn.loc[rateCsvColumn["Placement"] != "", "Placement"] = ""
print("Csv file successfully loaded.")

# ==================================================
# Loading responses array
# ==================================================

responsesCsv = pd.read_csv("data/responses_array.csv")
# print(responsesCsv)
# print(responsesCsv["song_list_full"][0])
# print(len(responsesCsv["song_list_full"][0]))
# print(responsesCsv.dtypes)

responses = responsesCsv[responsesCsv["discord_user"] != '""']
responses["song_list_full"] = responses["song_list_full"].apply(literal_eval)
responses["song_artist_and_name"] = responses["song_artist_and_name"].apply(literal_eval)
responses["song_placements"] = responses["song_placements"].apply(literal_eval)
responses["song_artists"] = responses["song_artists"].apply(literal_eval)
responses["song_names"] = responses["song_names"].apply(literal_eval)
responses["nickname"] = responses["nickname"].apply(literal_eval)
responses["discord_user"] = responses["discord_user"].apply(literal_eval)

for i, row in responses.iterrows() :

    if responses["nickname"][i] != "" :

        report = open(f"individual_reports/output/{responses["nickname"][i].rstrip()}.txt", "w")

    else :

        report = open(f"{responses["discord_user"][i]}.txt", "w")