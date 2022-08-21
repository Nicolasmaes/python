import csv

with open('coralieFollowersPtries.csv', 'r') as t1, open('coralieFollowingPtries.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('toUnfollow.csv', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(
                line + """
            """)
