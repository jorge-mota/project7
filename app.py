import streamlit as st
import pandas as pd
import plotly_express as px

st.title('Análisis de Vehículos')

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

disp_checkbox = st.checkbox('Gráfico de dispersión')

if disp_checkbox:  # al hacer clic en la caja
    # escribir un mensaje
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear el gráfico
    fig = px.scatter(
        vehicles_df,
        x='odometer',
        y='price',
        color='condition',
        title='Relación entre precio y Kilometraje',
        labels={'odometer': 'Kilometraje', 'price': 'Precio ($)'}
    )

    # mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)
