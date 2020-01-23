import pandas as pd

df=pd.DataFrame(
    {
        'Age':[30,20,22],
        'color':['Blue','Green','Red'],
        'Food':['Steak','Fish','Lamb']
}

)
print(df.loc[df['Age']<30,['color','Food']])
print("*********************************************")
print(df.iloc[(df['Age']<30).values,[0,1]])
