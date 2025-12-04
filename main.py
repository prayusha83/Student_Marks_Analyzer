import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"E:\python\python study advanced\projects\student marks analyzer\marks.csv")

# print(df)

subjects=df.columns[1:4]

#axis=1 is horizontal row
df["Average"]=df[subjects].mean(axis=1)
# df["Average"]=df.iloc[:,1:].mean(axis=1)

df["Total"]=df[subjects].sum(axis=1)

highestTot=0
highestName=""
lowestTot=float('inf')  #infinity, ie highest possible number
lowestName=""

for i in range(len(df)):

    # loc uses labels, iloc uses integer 
    # row then column
    this=df.loc[i, "Total"]
    # this=df.iloc[i, 3]

    if this>highestTot:
        highestTot=this
        highestName=df.loc[i, "Name"]
    
    if this<lowestTot:
        lowestTot=this
        lowestName=df.loc[i,"Name"]

    
print(df)
print(f"Highest Scorer : {highestName}, {highestTot}")
print(f"Lowest Scorer : {lowestName}, {lowestTot}")
print(df[subjects].describe())


# for bar chart of each student 
# marks with each subject

for i in range(len(df)):
    row=df.loc[i]
    plt.bar(subjects, row[subjects])
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.title(f"Marks of {row["Name"]}")
    plt.show()


