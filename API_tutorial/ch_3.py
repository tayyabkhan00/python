import requests

data = requests.get("https://jsonplaceholder.typicode.com/users").json()
# print(data)
# for user in data:
    # print(user["name"])
# print(len(data))

import pandas as pd
# pd.DataFrame(data).to_csv("users.csv", index=False)
df = pd.DataFrame(data)
print(df[df["address"].apply(lambda x: x["city"] == "South Christy")])
