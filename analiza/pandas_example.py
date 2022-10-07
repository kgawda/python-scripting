import pandas

df = pandas.read_csv(r"C:\Users\kurs\Documents\temp\mlb_players1.csv")
print(df)
print(df.describe())


print(df[df[' "Age"'] > 30 & (df[' "Team"'] == ' "BAL"')])