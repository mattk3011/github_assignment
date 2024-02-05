import streamlit as st
import pandas as pd

st.markdown("# Kart Configurations 🏎️")
st.sidebar.markdown("# Kart Configurations 🏎️")

st.write("What Kart Configuration is Best?")

df_mario_kart = pd.read_csv('data/kart_stats.csv')

#st.dataframe(df_kart)
# Limiting columns 
df_mario_kart = df_mario_kart[['Body', 'Weight', 'Acceleration', 'Ground Speed','Air Speed', 'Mini-Turbo']]
# Creating formatting on dataset to show green for most in column and red for least in column
st.dataframe(df_mario_kart.style.
             highlight_max(color='lightgreen', axis=0, subset=['Weight','Acceleration', 'Ground Speed','Air Speed', 'Mini-Turbo'])
             .highlight_min(color='red', axis=0, subset=['Weight','Acceleration', 'Ground Speed','Air Speed', 'Mini-Turbo'])
)

st.header("Kart Visualizations")
st.write("#### Top 10 Fastest Karts by Acceleration")
# Sort columns by Acceleration 
df_fastest = df_mario_kart[['Body', 'Acceleration', 'Ground Speed', 'Mini-Turbo', 'Air Speed']].sort_values("Acceleration", ascending=False)
# Store 10 fastest in variable
df_fast_ten = df_fastest.iloc[0:10]
# Bar Chart showing fastest karts
st.bar_chart(df_fast_ten, x='Body', y=['Ground Speed', 'Mini-Turbo', 'Air Speed'])

# area chart showing Acceleration and the corresponding Ground Speed
st.write("#### Acceleration vs Ground Speed")
st.area_chart(df_mario_kart, x='Acceleration', y='Ground Speed')

# A box to select single Karts
st.header("Single Karts")
chosen_kart = st.selectbox('Pick your Kart', df_mario_kart['Body'])

# Create variable that only contains data from chosen_kart and drop Body column
df_single = df_mario_kart.loc[df_mario_kart['Body'] == chosen_kart]
df_single = df_single.drop(columns=['Body'])

# unpivot data and create bar chart
df_unp_kart = df_single.unstack().rename_axis(['category', 'row number']).reset_index().drop(columns='row number').rename({0:'strength'},axis=1)
st.bar_chart(df_unp_kart, x='category', y= 'strength')

