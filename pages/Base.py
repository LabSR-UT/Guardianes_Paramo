import streamlit as st
#from streamlit_folium import folium_static
import folium
import rasterio
import numpy as np
from PIL import Image
import os
import leafmap.foliumap as leafmap
from streamlit_folium import st_folium

st.set_page_config(layout="wide")   

with st.sidebar:
    "# Info"
    st.write("")
    st.write("Laboratorio de Sensores Remotos \n <email://labsr@ut.edu.co>\n <https://labsr_ut.github.com>")
    st.write("")
logo = "./data/Logo IATECH.png"
st.sidebar.image(logo)

# Customize page title
st.title("PARAMO DEL PARQUE NACIONAL LOS NEVADOS")
st.subheader("Murillo, Tolima, Colombia")

st.markdown(
    """
    Delimitacion del area de interes
    """
)

bordersStyle={
'color': 'red',
'weight': 2,
'fillColor': 'red',
'fillOpacity': 0.0
} 

col1, col2 = st.columns((2,1))

with col1:
    in_geojson = "C:/github/streamlit-paramo/data/ROI_corregido2.geojson"
    
    width = 600
    height = 500
    
    m = leafmap.Map(center=[4.822, -75.289], zoom=12, google_map="HYBRID",  name="Paramo")
    m.add_geojson(in_geojson, layer_name="ROI",  style_function=lambda x:bordersStyle)
    
    m.to_streamlit(width, height)
    # call to render Folium map in Streamlit
    #st_data = st_folium(m, width=725)
    
with col2:
    st.image("C:/github/streamlit-paramo/data/paramo_murillo.jpg", caption="Vista del paramo desde Murillo", width=500)# use_column_width="always")
    st.write("**Creditos Imagen: <https://www.livingcol.com>**")
