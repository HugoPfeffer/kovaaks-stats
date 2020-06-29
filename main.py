# To add a new cell, type '# %%'
import pandas as pd
import os
import shutil

dataDir = 'E:\SteamLibrary\steamapps\common\FPSAimTrainer\FPSAimTrainer\stats'
stats = pd.read_csv(dataDir + '\\stats\\stats.csv')
destination = dataDir + '\\old'
li = []
keys = []

for filename in os.listdir(dataDir):
    if filename.endswith(".csv"): 
        df = pd.read_csv(dataDir + '\\' + filename, error_bad_lines=False)
        score = df.loc[df[df.columns[0]].str.contains('Score')]['Timestamp'].reset_index(drop=True)
        scenario = df.loc[df[df.columns[0]].str.contains('Scenario')]['Timestamp'].reset_index(drop=True)
        dmgDone = df.loc[df[df.columns[0]].str.contains('Damage Done')]['Timestamp'].reset_index(drop=True)
        avgTTK = df.loc[df[df.columns[0]].str.contains('Avg TTK')]['Timestamp'].reset_index(drop=True)
        kills = df.loc[df[df.columns[0]].str.contains('Kills')]['Timestamp'].reset_index(drop=True)

        data = {
            'Score' : score,
            'Damage Done' : dmgDone,
            'Average TTK' : avgTTK,
            'Kills' : kills,
            'Scenario' : scenario
        }
        result = pd.DataFrame(data)
        li.append(result)

        shutil.move(dataDir + '\\' + filename, destination)



target = stats.append(li).reset_index(drop=True)
target.to_csv(dataDir + '\\stats\\stats.csv')





