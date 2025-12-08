import plotly.express as px
import pandas as pd

df = px.data.iris()
df.head(1)

# px.violin(df, x="species", y="petal_length", box=True, points="all").show() 

# px.density_heatmap(df, x="sepal_width", y="sepal_length").show()

# px.scatter_matrix(df, dimensions=df.columns[:4], color="species").show()

# px.scatter_3d(df, x="sepal_length", y="sepal_width", z="petal_length", color="species").show()

