import pandas as pd


def arrest_rate(df, race, year):
    count = 0
    year_total = 0
    for index, row in df.iterrows():
        if type(row["arrest_date"]) == str:
            df_year = row["arrest_date"].split()[0][:4]
        if df_year == str(year):
            year_total += 1
            if row["race"] == race:
                count += 1
    return count/year_total


arrests = pd.read_csv(r"Arrests_2020-08-01.csv")
demographics = pd.read_csv("btv_demographics.csv")

races = ["Black or African American - B"]
years = demographics["year"].to_list()
black_pop_prop = demographics["black"].to_list()
black_rates = {}
i = 0
for year in years:
    for race in races:
        data = [year, race, arrest_rate(arrests, race, year)]
        black_arrest_rate = round(data[2], 3)
        curr_black_pop_prop = round(black_pop_prop[i], 3)
        # print("Year: " + str(year) + " black proportion in btv: " + str(curr_black_pop_prop) + ", black arrest rate in btv: " + str(black_arrest_rate))
        black_rates[year] = round(black_arrest_rate/curr_black_pop_prop, 3)
    i += 1
print("-------------------------------------------------------------------------")
races = ["White - W"]
years = demographics["year"].to_list()
white_pop_prop = demographics["white"].to_list()
white_rates = {}
i = 0
for year in years:
    for race in races:
        data = [year, race, arrest_rate(arrests, race, year)]
        white_arrest_rate = round(data[2], 3)
        curr_white_pop_prop = round(white_pop_prop[i], 3)
        # print("Year: " + str(year) + " white proportion in btv: " + str(curr_white_pop_prop) + ", white arrest rate in btv: " + str(white_arrest_rate))
        white_rates[year] = round(white_arrest_rate/curr_white_pop_prop, 3)
    i += 1

print("ratio of black arrests over total black population in btv")
print(black_rates)
print("-------------------------------------------------------------------------")
print("ratio of white arrests over total white population in btv")
print(white_rates)
