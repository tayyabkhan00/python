import pandas as pd

data = {
    "Name": ["Ali", "Sara", "John"],
    "Age": [22, 25, 30]
}

df = pd.DataFrame(data)
df.index = ["a", "b", "c"]

df.loc["b"]
df.iloc[1]

# loc[] is label-based indexing, meaning it selects rows and columns using index names.
# iloc[] is integer position-based indexing, meaning it selects data using row numbers.
df.loc["a":"c"]     # includes c
df.iloc[0:2]        # excludes 2