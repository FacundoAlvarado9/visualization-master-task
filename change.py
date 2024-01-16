import pandas as pd

df = pd.read_csv("messi_dataset.csv")


for ind in df.index:
    if(df['Venue'][ind] == "A"):
        df['Opponent_result'][ind] = df['Result'][ind][0]
        df['MT_Result'][ind] = df['Result'][ind][-1]

        df['Opponent_At_Score'][ind] = df['At_score'][ind][0]
        df['MT_At_Score'][ind] = df['At_score'][ind][-1]
    else:
        df['MT_Result'][ind] = df['Result'][ind][0]
        df['Opponent_result'][ind] = df['Result'][ind][-1]

        df['MT_At_Score'][ind] = df['At_score'][ind][0]
        df['Opponent_At_Score'][ind] = df['At_score'][ind][-1]
    print(df['Venue'][ind], df['Date'][ind], df['Opponent'][ind], df['Result'][ind], df['MT_Result'][ind])

df.drop(['Result', 'At_score'], axis=1, inplace=True)

df.to_csv("output.csv", encoding='utf-8', index=False)