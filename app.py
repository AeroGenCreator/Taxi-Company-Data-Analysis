"""Librerias"""
import streamlit as st
import pandas as pd
import plotly.express as px
import duckdb

st.set_page_config(
    page_icon='🚖',
    layout='wide'
)
st.title(':material/local_taxi: Statistics test for a taxi company')

def load_data():
    df1 = pd.read_csv('project_sql_result_01.csv')
    df2 = pd.read_csv('project_sql_result_04.csv')
    df3 = pd.read_csv('project_sql_result_07.csv')

    return df1, df2, df3

def top_10_locations():
    query_1 = duckdb.sql(f"""
    SELECT
        dropoff_location_name,
        average_trips
    FROM
        df2
    ORDER BY
        average_trips DESC
    LIMIT
        10;
    """).df()

    total = query_1['average_trips'].sum()
    query_1['percentage'] = query_1['average_trips'] / total

    with st.expander('Data Preview'):
        st.dataframe(query_1,column_config={'average_trips':st.column_config.NumberColumn(format='%d'),'percentage':st.column_config.NumberColumn(format='percent',step=0.01)})

    fig = px.pie(query_1,values='percentage',names='dropoff_location_name',color_discrete_sequence= px.colors.sequential.Reds)
    fig.update_layout(title_text='Top 10 Locations',legend=dict(orientation="h",y=-0.25,x=0.5,xanchor="center"))
    st.plotly_chart(fig)

def top_10_taxi_companies():
    query_1 = duckdb.sql(f"""
    SELECT
        company_name,
        trips_amount
    FROM
        df1
    ORDER BY
        trips_amount DESC
    LIMIT
        10;
    """).df()

    with st.expander('Data Preview'):
        st.dataframe(query_1)

    fig = px.bar(query_1,x='trips_amount',y='company_name',color='company_name',color_discrete_sequence= px.colors.sequential.Reds_r)
    fig.update_layout(title_text='Top 10 Taxi Companies',legend=dict(orientation="h",y=-0.25,x=0.5,xanchor="center"))
    st.plotly_chart(fig)

def histogram(df:pd.DataFrame):
    fig = px.histogram(df3,x='duration_seconds',color='weather_conditions',nbins=250,opacity=1,color_discrete_sequence= px.colors.sequential.Brwnyl)
    fig.update_layout(title_text='Distribution (Weather Data)',legend=dict(orientation="h",y=-0.25,x=0.5,xanchor="center"))
    st.plotly_chart(fig)

# Interfaz:

df1, df2, df3 = load_data()

col_1, col_2, col_3 = st.columns(3)
with col_1:
    with st.expander('Preview'):
        st.dataframe(df1)
with col_2:
    with st.expander('Preview'):
        st.dataframe(df2)
with col_3:
    with st.expander('Preview'):
        st.dataframe(df3)

col_4, col_5 = st.columns([2.3,1.7])
with col_4:
    
    histogram(df=df3)

    st.divider()
    col_6, col_7 = st.columns(2)
    with col_6:
        st.subheader('Levene Test')
        st.markdown('$H_0$: The population variances of trip duration are equal $(\sigma^2$ rain $= \sigma^2$ no rain$)$')
        st.markdown('$H_a$: The population variances of trip duration are not equal $(\sigma^2$ rain $\\neq$ $\sigma^2$ no rain$)$')
    with col_7:
        st.empty()
        st.markdown(':green[P-Value (Levene Test)]')
        st.metric(label='Levene',border=1,value=0.53,label_visibility='hidden')
    
    st.divider()

    col_8, col_9 = st.columns(2)
    with col_8:
        st.subheader('Student Test')
        st.markdown('$H_0$: The population means of trip duration are equal $(\mu$ rain $= \mu$ no rain$)$')
        st.markdown('$H_a$: The population means of trip duration are not equal $(\mu$ rain $\\neq$ no rain $)$')
    with col_9:
        st.empty()
        st.markdown(':green[P-Value (Student\'s Test)]')
        st.metric(label='Student\'s',label_visibility='hidden',value=0.00000000000651,border=1)
    st.divider()
    st.subheader('**Conclusion:** :red[The means are different. Weather has  influence over the service.]')
with col_5:
    top_10_locations()
    top_10_taxi_companies()