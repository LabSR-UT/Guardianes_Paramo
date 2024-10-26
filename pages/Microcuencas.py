# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:39:48 2024

@author: USUARIO
"""
import leafmap.foliumap as leafmap
import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium

import streamlit as st
import leafmap.foliumap as leafmap


st.set_page_config(layout="wide")   

with st.sidebar:
    "# Info"
    st.write("")
    st.write("Laboratorio de Sensores Remotos \n <email://labsr@ut.edu.co>\n <https://labsr_ut.github.com>")
    st.write("")
    
logo = "./data/Logo IATECH.png"
st.sidebar.image(logo)

# Customize page title
st.title("MICROCUENCAS")
# Customize page title

st.markdown(
    """
    Visualizacion de las microcuencas presentes en el paramo
    """
)

col1, col2 = st.columns((2,1))

with col1:
    width = 600
    height = 500
    
    m = leafmap.Map(center=[4.822, -75.289], zoom=12)
    
    in_geojson = "C:/github/streamlit-paramo/data/Subcuencas2.geojson"
    m.add_geojson(in_geojson, layer_name="Cuencas", fill_colors=["green"])
    m.to_streamlit(width, height)

with col2:
    #grayscale = original.convert('LA')
    st.subheader("Estadisticas:")
    
    gdf = gpd.read_file("C:/github/streamlit-paramo/data/Subcuencas2.gpkg")
    
    st.write("Numero de microcuencas:", gdf.shape[0])
    st.write("Area microcuenca mayor (has):", gdf['Area (has)'].max())
    st.write("Area microcuenca menor (has):", gdf['Area (has)'].min())
    st.write("Area promedio (has):", gdf['Area (has)'].mean().round(2))
    st.write("Area total (has):", gdf['Area (has)'].sum())
