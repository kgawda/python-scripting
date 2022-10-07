import pandas

def csv():
    df = pandas.read_csv(
        r"C:\Users\kurs\Documents\temp\mlb_players1.csv",
        # parse_dates=['Hire Date']  # podajemy ktore kolumny zawieraja daty
    )

    print(df)
    print(df.describe())

    print(df[(df[' "Age"'] > 30) & (df[' "Team"'] == ' "BAL"')])

def excel():
    df = pandas.read_excel("C:\\Users\\kurs\\Documents\\temp\\dane1.xlsx", sheet_name=1)
    print(df)

    print(df[(df.data > pandas.to_datetime('2017-01-01')) & (df.moc > 11)])
    print(df.moc.mean())
    df['moc_per_temperatura'] = df.moc / df['temperatura powrotu']
    print(df)

    # writer = pandas.ExcelWriter('output.xlsx')
    # df.to_excel(writer, 'Sheet1')
    # writer.save()

if __name__ == '__main__':
    # csv()
    excel()