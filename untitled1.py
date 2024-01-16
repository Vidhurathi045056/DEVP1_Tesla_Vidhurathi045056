# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a5gRQ_HWwdv4wofsEpRs195jfZM-3fbx
"""

!pip install streamlit

import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import scipy.stats as sps
import statsmodels as sm
import statsmodels.formula.api as smf

# Define File Path : Replace xxxxx with appropriate File Path


# Import & Read Dataset
df = pd.read_csv('/content/issues.csv')

# Display Dataset Information
df.info()

df.head(10)

import streamlit as st
import pandas as pd

# Load the CSV file
filename = "/content/issues.csv"  # Replace with the actual file path
df = pd.read_csv(filename)

# Streamlit app
st.title("CSV Dashboard")

# Display the data table
st.write("## Data Table")
st.dataframe(df)

# Display some statistics
st.write("## Data Statistics")
st.write("Number of Rows:", df.shape[0])
st.write("Number of Columns:", df.shape[1])
st.write("Summary Statistics:", df.describe())

# Custom filtering
st.write("## Filter Data")

# Filter by name
selected_name = st.selectbox("Select Name:", df["name"].unique())
filtered_by_name = df[df["name"] == selected_name]
st.write(f"Filtered Data for Name: {selected_name}")
st.dataframe(filtered_by_name)

# Filter by year
selected_year = st.selectbox("Select Year:", df["year"].unique())
filtered_by_year = df[df["year"] == selected_year]
st.write(f"Filtered Data for Year: {selected_year}")
st.dataframe(filtered_by_year)

# Filter by quarter
selected_quarter = st.selectbox("Select Quarter:", df["quarter"].unique())
filtered_by_quarter = df[df["quarter"] == selected_quarter]
st.write(f"Filtered Data for Quarter: {selected_quarter}")
st.dataframe(filtered_by_quarter)

!streamlit run /usr/local/lib/python3.10/dist-packages/colab_kernel_launcher.py

!npx localtunnel --port 8501

import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Read the CSV file
filename = '/content/issues.csv'  # replace with your actual filename
df = pd.read_csv(filename)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    # Table component
    html.Div([
        dcc.Graph(
            id='table',
            figure=px.table(df)
        )
    ]),

    # Dropdown for selecting columns
    html.Div([
        dcc.Dropdown(
            id='column-dropdown',
            options=[{'label': col, 'value': col} for col in df.columns],
            value='name',  # default column
            multi=False
        )
    ]),

    # Bar chart based on selected column
    html.Div([
        dcc.Graph(id='bar-chart')
    ])
])

# Define callback to update bar chart based on column selection
@app.callback(
    Output('bar-chart', 'figure'),
    [Input('column-dropdown', 'value')]
)
def update_bar_chart(selected_column):
    fig = px.bar(df, x=selected_column, y='count', title=f'Bar Chart for {selected_column}')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)