import pandas as pd
import numpy as np


# df = pd.read_csv(r"graph_this.csv")

# print(np.average(df["black_prop"].to_list()))
# print(np.average(df["white_prop"].to_list()))
# print("hi")

nums = [12, 11, 8, 4, 16, 13, 9, 7]
iqr = np.subtract(*np.percentile(nums, [75, 25]))
print(iqr)