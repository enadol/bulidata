#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

col1=st.columns(5)

# In[3]:


df = pd.read_csv("results2022-2023201_overall.csv")
df.Attendance = df.Attendance.str.replace(',', '').astype(int)

with st.sidebar:
    #col1.header("Visualizations")
    plot_options = ["Posiciones", "Puntos", "Público", "Goles", "Diff. Goles", "Partidos", "xG", "Goleadores"]
    selected_plot = st.selectbox("Seleccione un gráfico", plot_options)

# In[4]:
def graphPositions(df):

# Bar chat of the League Positions
    fig = px.bar(df, 
                 x=df.Squad, 
                 y=df.Pts,
                 title="Total Puntos : Bundesliga 2022 - 2023",
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
                 title='Partidos jugados (MP) y Puntos (Pts) : Bundesliga 2022 - 2023',
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
                 title="Público promedio en el estadio : Bundesliga 2022 - 2023",
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
                 title='Goles a favor, Goles en contra : Bundesliga 2022 - 2023',
                 height=600
                )
    st.plotly_chart(fig)


# In[7]:

def goalDiff(df):
# Chart for Goal Difference
    fig = px.bar(df, 
                 x=df.Squad, 
                 y=df.GD,
                 title="Diferencia de goles : Bundesliga 2022 - 2023",
                 text=df.GD,
                 color=df.GD,
                 color_continuous_scale="ylgn",
                 height=600
                )
    st.plotly_chart(fig)


# In[8]:

def graphWLD(df):
# Bar chart of Wins, Draws, Losses
    fig = px.bar(df, 
                 x='Squad', 
                 y=['W', 'D', 'L'], 
                 barmode='group',
                 title='Ganados, empatados, perdidos : Bundesliga 2022 - 2023',
                 color_discrete_sequence=["green","gold","tomato"],
                 text_auto=True,
                 height=600
                )
    st.plotly_chart(fig)


# In[9]:

def graphBubble(df):
# Bubble chart of Expected Goals For and Against
    fig = px.scatter(df, 
                     x='xG', 
                     y='xGA', 
                     size='xG', 
                     color='Squad',
                     title="Eficiencia de clubes: oportunidades creadas Vs oportunidades concedidas: Bundesliga 2022 - 2023",
                     text=df['Squad'].str[:4],
                     height=600,
                    )

    fig.update_layout(
        xaxis=dict(title='Expected Goals (xG): Ocasiones de gol y probabilidad de convertir'),
        yaxis=dict(title='Expected Goals del rival: (xGA)')
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
                     title='Máximo goleador por club : Bundesliga 2022 - 2023',
                     height=600,
                     width=920
                )

    st.plotly_chart(fig)


# In[ ]:
with col1:
    st.title("VISUAL DATA BUNDESLIGA 2022/2023")
    if selected_plot == "Posiciones":
        #st.write("Gráfico de posiciones:")
        graphPositions(df)

    elif selected_plot == "Puntos":
        #st.write("Gráfico de puntos:")
        graphPuntos(df)

    elif selected_plot == "Público":
       #st.write("Público en el estadio:")
       graphStadiums(df)

    elif selected_plot == "Goles":
        #st.write("Goles a favor y en contra:")
        graphGoals(df)

    elif selected_plot == "Diff. Goles":
        #st.write("Diferencia de goles:")
        goalDiff(df)

    elif selected_plot == "Partidos":
        #st.write("Partidos:")
        graphWLD(df)

    elif selected_plot == "xG":
        #st.write("Expected Goals:")
        graphBubble(df)

    else:
        #selected_plot == "Diff. Goles":
        #st.write("Máximo goleador:")
        graphTopScorer(df)
