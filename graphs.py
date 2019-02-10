### ETHNICITY - HIRED ###

import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/hiring-patterns.csv')

df['Hired'].replace('NO', 'No', inplace=True)
df['Gender'].replace('Female ', 'Female', inplace=True)
df['Gender'].replace(' N/A', 'N/A', inplace=True)
df['Gender'].replace('   N/A', 'N/A', inplace=True)

trace1 = go.Bar(
    x=['White','BME'],
    y=[white.shape[0], bme.shape[0]],
    name='Applied'
)
trace2 = go.Bar(
    x=['White','BME'],
    y=[white[white.Interviewed == 'Yes'].shape[0], bme[bme.Interviewed == 'Yes'].shape[0]],
    name='Interviewed'
)
trace3 = go.Bar(
    x=['White','BME'],
    y=[white[white.Hired == 'Yes'].shape[0], bme[bme.Hired == 'Yes'].shape[0]],
    name='Hired'
)

data = [trace1, trace2, trace3]
layout = go.Layout(
    barmode='group'
)

### GENDER - RACE ###

import plotly.plotly as py
import plotly.graph_objs as go

white = df[df.Ethnicity == 'White']
bme = df[df.Ethnicity == 'BME']

trace1 = go.Bar(
    x=['Male', 'Female'],
    y=[white[white.Gender == 'Male'].shape[0], white[white.Gender == 'Female'].shape[0]],
    name='White'
)
trace2 = go.Bar(
    x=['Male', 'Female'],
    y=[bme[bme.Gender == 'Male'].shape[0], bme[bme.Gender == 'Female'].shape[0]],
    name='BME'
)

data = [trace1, trace2]
layout = go.Layout(
    barmode='stack'
)

### GENDER - INTERNSHIPS ###

import plotly.plotly as py
import plotly.graph_objs as go

male = df[df.Gender == 'Male']
female = df[df.Gender == 'Female']

trace1 = go.Bar(
    x=['1', '2', '3', '4', '5'],
    y=[male[male.Internships == 1].shape[0], 
	   male[male.Internships == 2].shape[0], 
	   male[male.Internships == 3].shape[0], 
	   male[male.Internships == 4].shape[0], 
	   male[male.Internships == 5].shape[0]], name='Male'
)
trace2 = go.Bar(
    x=['1', '2', '3', '4', '5'],
    y=[female[female.Internships == 1].shape[0], 
	   female[female.Internships == 2].shape[0], 
	   female[female.Internships == 3].shape[0], 
	   female[female.Internships == 4].shape[0], 
	   female[female.Internships == 5].shape[0]], name='Female'
)

data = [trace1, trace2]
layout = go.Layout(
    barmode='stack'
)
