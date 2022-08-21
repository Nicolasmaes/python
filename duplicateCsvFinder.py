import pandas as pd

df_state = pd.read_csv("coralieFollowersPtries.csv")

Dup_Rows = df_state[df_state.duplicated()]

print("\n\nDuplicate Rows : \n {}".format(Dup_Rows))


Dup_Rows.to_csv(r'Zdoublon.csv', index=None)
