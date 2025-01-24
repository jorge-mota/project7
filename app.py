import streamlit as st
import pandas as pd
import plotly_express as px


vehicles_df = pd.read_csv('vehicles_us.csv')
print(vehicles_df)
hist_button = st.button('Construir Histograma')

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(vehicles_df, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Gráfico de dispersión')

if disp_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear el gráfico
    fig = px.scatter(
        vehicles_df,
        x='x',
        y='y',
        title='Gráfico de dispersión'
    )

    # mostrar el gráfico
    fig.show()
