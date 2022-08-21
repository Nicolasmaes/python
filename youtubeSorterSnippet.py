# Created on 27/05/22 by Nicolas Maes

from datetime import datetime

import pandas as pd

# on lit le csv final.
csvData = pd.read_csv("1.csv")

# on trie la liste selon l'index 0 (la durée).
csvData.sort_values(["duration"],
                    axis=0,
                    ascending=[True],
                    inplace=True)

# on écrit un nouveau fichier csv avec les données triées.
csvData.to_csv(r'final.csv', index=None)
