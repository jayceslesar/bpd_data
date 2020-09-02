import pandas as pd

# from census
white_2012 = 0.8894
black_2012 = 0.039
asian_2012 = 0.0356
mixed_2012 = 0.026
hispanic_2012 = 0.027

# estimated
white_2013 = 0.87752
black_2013 = 0.0418
asian_2013 = 0.0433
mixed_2013 =  0.026
hispanic_2013 = 0.027

# estimated
white_2014 = 0.85872
black_2014 = 0.0446
asian_2014 = 0.051
mixed_2014 =  0.026
hispanic_2014 = 0.027

# estimated
white_2015 = 0.83992
black_2015 = 0.0474
asian_2015 = 0.05864
mixed_2015 =  0.026
hispanic_2015 = 0.027

# estimated
white_2016 = 0.8355
black_2016 = 0.0502
asian_2016 = 0.0663
mixed_2016 =  0.026
hispanic_2016 = 0.027

# from btv city data
white_2017 = 0.83
black_2017 = 0.053
asian_2017 = 0.074
mixed_2017 = 0.026
hispanic_2017 = 0.026

# estimated
white_2018 = 0.84
black_2018 = 0.053
asian_2018 = 0.0685
mixed_2018 = 0.0265
hispanic_2018 = 0.027

# from btv city data
white_2019 = 0.85
black_2019 = 0.053
asian_2019 = 0.063
mixed_2019 = 0.027
hispanic_2019 = 0.028

years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
white = [white_2012, white_2013, white_2014, white_2015, white_2016, white_2017, white_2018, white_2019]
black = [black_2012, black_2013, black_2014, black_2015, black_2016, black_2017, black_2018, black_2019]
asian = [asian_2012, asian_2013, asian_2014, asian_2015, asian_2016, asian_2017, asian_2018, asian_2019]
mixed = [mixed_2012, mixed_2013, mixed_2014, mixed_2015, asian_2016, asian_2017, asian_2018, asian_2019]
hispanic = [hispanic_2012, hispanic_2013, hispanic_2014, hispanic_2015, hispanic_2016, hispanic_2017, hispanic_2018, hispanic_2019]

df = pd.DataFrame()
df["year"] = years
df["white"] = white
df["black"] = black
df["asian"] = asian
df["mixed"] = mixed
df["hispanic"] = hispanic

df.to_csv("btv_demographics.csv")