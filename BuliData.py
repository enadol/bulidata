#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st


# In[3]:


df = pd.read_csv("results2022-2023201_overall.csv")
df.Attendance = df.Attendance.str.replace(',', '').astype(int)


# In[4]:
def graphPositions(df):

# Bar chat of the League Positions
    fig = px.bar(df, 
                 x=df.Squad, 
                 y=df.Pts,
                 title="Total Puntos : BL 2022 - 2023",
                 color=df.Pts,
                 text=df.Pts,
                 color_continuous_scale="blues",
                 height=600
                )
    st.plotly_chart(fig)


# In[4]:

def graphPuntos(df):
  
# Bar Chat of Matches played and Points
    fig = px.bar(df, 
                 x='Squad', 
                 y=['MP', 'Pts'], 
                 barmode='group', 
                 labels={'value': 'Count'},
                 title='Matches Played (MP) and Points (Pts) : EPL 2022 - 2023',
                 text_auto=True,
                 color_discrete_sequence=["gray","deepskyblue"]
                )
    st.plotly_chart(fig)


# In[5]:

def graphStadiums(df):
# Chart of the Average Stadium Attendance
    fig = px.bar(df, 
                 x=df.Squad, 
                 y=df.Attendance,
                 title="Average Attendance : EPL 2022 - 2023",
                 text=df.Attendance,
                 color=df.Attendance,
                 color_continuous_scale="greens",
                 height=600
                )
    st.plotly_chart(fig)


# In[6]:

def graphGoals(df):
# Stacked bar graph of Goals For and Against
    fig = px.bar(df, 
             x='Squad', 
                 y=['GF', 'GA'],
                 color_discrete_sequence=["darkgreen","tomato"],
                 barmode='stack', 
                 text_auto=True,
                 labels={'value': 'Count'},
                 title='Goals For, Goals Against : EPL 2022 - 2023',
                 height=600
                )
    st.plotly_chart(fig)


# In[7]:

def goalDiff(df):
# Chart for Goal Difference
    fig = px.bar(df, 
                 x=df.Squad, 
                 y=df.GD,
                 title="Goal Difference : EPL 2022 - 2023",
                 text=df.GD,
                 color=df.GD,
                 color_continuous_scale="ylgn",
                 height=600
                )
    st.plotly_chart(fig)


# In[8]:

def grapgWLD(df):
# Bar chart of Wins, Draws, Losses
    fig = px.bar(df, 
                 x='Squad', 
                 y=['W', 'D', 'L'], 
                 barmode='group',
                 title='Wins, Draws, Losses : EPL 2022 - 2023',
                 color_discrete_sequence=["green","gold","tomato"],
                 text_auto=True,
                 height=600
                )
    st.plotly_chart(fig)


# In[9]:

def graphBubble(df)
# Bubble chart of Expected Goals For and Against
    fig = px.scatter(df, 
                     x='xG', 
                     y='xGA', 
                     size='xG', 
                     color='Squad',
                     title="Team Efficiency: Chances Created Vs Chanced Conceded : Bundesliga 2022 - 2023",
                     text=df['Squad'].str[:4],
                     height=600,
                    )

    fig.update_layout(
        xaxis=dict(title='Expected Goals (xG): Every goal-scoring chance, and the likelihood of scoring'),
        yaxis=dict(title='Expected Goals Against Team: (xGA)')
    )
    st.plotly_chart(fig)


# In[10]:

def graphTopScorer(df):
    df[['Player', 'Goals']] = df['Top Team Scorer'].str.split(' - ', expand=True)
    df.Goals = df.Goals.astype(int)

# Create a bar chart of top scorer for each team
    fig = px.bar(df, 
                     y='Squad', 
                     x='Goals',
                     color='Goals',
                     color_continuous_scale="ylorrd",
                     text='Top Team Scorer',
                     title='Máximo goleador por club : Bundesliga 2022 - 2023"',
                     height=600
                )

    st.plotly_chart(fig)


# In[ ]:




