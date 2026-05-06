import pandas as pd
import numpy as np
from ast import literal_eval
from collections import Counter
import warnings

print(f"Disabling warning messages... (I'm not hacking your shit dw)")
warnings.filterwarnings("ignore")

pd.set_option("display.max_columns", None)

def linebreak() :

    print("====================")

# ==================================================
# Arrays for final results
# ==================================================

songArray = []
scoreArray = []
individualSongsArray = []
overallArray = []
scoreDict = {}
scoreDictSort = {}

responsesCsv = pd.read_csv("responses_array.csv")
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

def placementCheck(length, total, user) :

    if length == 100 and total == 5050 :

        print("No errors on song placements.")

    elif length != 100 and total == (length*(length + 1))/2 :

        print("No error on song placements, less than 100 songs.")

    else :

        print(f"ERROR: Ballot {user} has errors with song placements.")

arrayCheck = [1,2,3,4,5,6,7,8,9,10,15.5,15.5,15.5,15.5,15.5,15.5,15.5,15.5,15.5,15.5,21,22,23,26,26,26,26,26,29]
arrayNoDupe = [1,2,3,4,5,6,7,8,9,10,21,22,23,29]
evilArray = [1,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,50.5,100]
evilArray2 = [1,100]

def tiersCheck(rankList, nonDupeList, fullTierList) :

    #z = 1
    upperBound = ()
    lowerBound = ()
    # print("length",len(nonDupeList))
    # print(nonDupeList)

    if len(nonDupeList) == 0 :

        print("TIERING: List is fully tiered.")

        #print("nd1",nonDupeList)
        nonDupeList = fullTierList
        #print("nd2",nonDupeList)
        #z = -0.5

        for i in range(0, len(nonDupeList) - 1) :

            lowerBound = nonDupeList[i]
            upperBound = nonDupeList[i + 1]

            difference = upperBound - lowerBound 
            #print("diff",difference)

            listCount = Counter(rankList)[lowerBound]

            #print(f"occurences of diff {listCount}")

            if listCount == difference :

                print(f"Tier {i + 1} is good.")

            else :

                #print(f"ERROR: Issue with tier {i + 1}.")
                raise Exception(f"ERROR: Issue with tier {i + 1}.")
                return

    else :

        print("TIERING: List is partially tiered.")

        for i in range(0, len(nonDupeList) - 1) :

            if nonDupeList[i] + 2 > nonDupeList[i + 1] :

                pass

            else :

                #print(i)
                sum = nonDupeList[i] + nonDupeList[i + 1]

                lowerBound = nonDupeList[i]
                upperBound = nonDupeList[i + 1]

                difference = upperBound - lowerBound - 1
                #print("diff",difference)

                mean = (sum) / 2
                #print("mean",mean)

                listCount = Counter(rankList)[mean]

                #print(f"occurences of diff {listCount}")

                if listCount == difference :

                    print(f"Tier {i + 1} is good.")

                else :

                    print(f"ERROR: Issue with tier {i + 1}.")
                    return
            
#tiersCheck(evilArray,evilArray2)

def songArrayAppend(songs, scores) :

    scores.sort(reverse = True)

    for x in range(len(scores)) :

        scoreArray.append(scores[x])

        songArray.append(songs[x])

# ==================================================

def calculateResults(songs, scores) :

    if len(songs) != len(scores) :

        raise Exception("Song and score arrays do not match.")
    
    else :

        songsLower = [x.lower() for x in songs]

        combined = list(zip(songsLower, scores))

        for x, i in combined :

            scoreDict[x] = scoreDict.get(x, 0) + i

        scoreDictSort = {k : v for k, v in sorted(scoreDict.items(), key = lambda item : item[1], reverse = True)}

        alphabetDictSort = {k : v for k, v in sorted(scoreDict.items(), key = lambda item : item[0])}

    return(scoreDictSort, alphabetDictSort)


linebreak()

for i, row in responses.iterrows() :

# ==================================================
#               VALIDATING RESPONSES
# ==================================================

    listLength = len(responses["song_list_full"][i])
    user = responses['discord_user'][i]
    placementTotal = np.sum(responses["song_placements"][i])
    songNameArtist = responses["song_artist_and_name"][i]

    #responseRow = responses.iloc[i]
    #print(responseRow)

    print(f"NOW PROCESSING: {user}'s ballot.")

    if len(responses["song_artist_and_name"][i]) == len(responses["song_placements"][i]) == len(responses["song_list_full"][i]) == len(responses["song_names"][i]) == len(responses["song_artists"][i]) :

        print("No splitting errors.")

        placementCheck(listLength, placementTotal, user)

    else :

        print(f"ERROR: Ballot {user} has a splitting error.")

    responsesPlacements = responses["song_placements"][i]
    dupeCheckSet = set(responses["song_placements"][i])
    dupeCheckList = sorted(dupeCheckSet)
    dupeCheck = len(set(responses["song_placements"][i]))

    if dupeCheck == listLength :

        print("TIERING: No tiers detected.")

    elif 50.5 in dupeCheckSet and len(dupeCheckSet) == 1 :

        print("All the same.")

    else :

        allDupeReserve = dupeCheckList

        noDupesArray = []

        for x in dupeCheckList :

            #print(x,"counter",Counter(responsesPlacements)[x])

            if Counter(responsesPlacements)[x] == 1 :

                noDupesArray.append(x)

            else :

                #print(x,"counter error",Counter(responsesPlacements)[x])

                pass

        #print("done")

        tiersCheck(responsesPlacements, noDupesArray, allDupeReserve)

    linebreak()

    linebreak()
    print("Finished validating response. Appending scores to the ballot.")
    linebreak()

    songArrayAppend(songNameArtist,responsesPlacements)

    # elif any(type(x) == int for x in dupeCheckSet) :

    #     print(f"ERROR: Ballot {user} has duplicate integers")

# print(responses)
# print(responses["song_list_full"][0])
# print(len(responses["song_list_full"][0]))
# print(responses.dtypes)

print(songArray)
print(scoreArray)

finalScores, finalScoresAlphabet = calculateResults(songArray, scoreArray)

print(finalScores,"\n",finalScoresAlphabet)

outputScores = pd.Series(finalScores)
outputAlphabet = pd.Series(finalScoresAlphabet)

# Output the list of artists and the list of songs as csv to scan through and check for any weird things

outputScores.to_csv("final_results.csv")
outputAlphabet.to_csv("results_alphabetical.csv")

class response :
    def __init__(self, discord_user):
        pass

#responsesCsv.astype("list")

'''testArrayStr = responsesCsv["song_placements"][0]
testArray = testArrayStr.split(",")
print(testArray)
print(type(testArray))'''

# def shred(resList) :
#     pass

# # import pandas as pd
# # from ast import literal_eval

# df = pd.read_csv("responses_array.csv", header = 0, sep = ",")

# df["song_artists"] = df["song_artists"].apply(literal_eval)
# df["nickname"] = df["nickname"].apply(literal_eval)

# def gatekeep(resList, nickname) :

#     cfList = [x.casefold() for x in resList]

#     if "itzy" in cfList :

#         print(f"{nickname}'s list has been approved.")
#         #pass

#     else :

#         print(f"{nickname}'s list has been gatekept. Shredding list...")
#         shred(resList)

# def listAppend(resList) :

#     initList = []

#     for x in resList :

#         initList.append(x)

#     return(initList)

# for i, row in df.iterrows() :

#     responseArtists = df["song_artists"][i]
#     userNick = df["nickname"][i]
#     artistList = listAppend(responseArtists)

#     gatekeep(artistList, userNick)