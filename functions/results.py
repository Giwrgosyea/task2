import pandas as pd
import plotly.express as px
import sqlite3

# Create your connection.


def metrics(data):
	
	print(data)
	a = pd.DataFrame.from_dict(data)
	index=a.shape[0]
	a=a.groupby('fibonacci (int)').mean().reset_index()
	fig = px.scatter(a, x="fibonacci (int)", y="time (sec)", title='Time to calculate and report the sequences').update_traces(mode="lines+markers")
	fig.write_image("static/figure.png")
	return index

