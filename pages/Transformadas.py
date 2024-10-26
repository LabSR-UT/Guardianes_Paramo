# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 15:54:10 2024

@author: USUARIO
"""
import streamlit as st
from streamlit_folium import folium_static
import folium
import rasterio
import numpy as np
import geopandas as gpd
import leafmap.foliumap as leafmap
import rioxarray
import branca
import branca.colormap as cm

st.set_page_config(layout="wide")   

with st.sidebar:
    "# Info"
    st.write("")
    st.write("Laboratorio de Sensores Remotos \n <email://labsr@ut.edu.co>\n <https://labsr_ut.github.com>")
    st.write("")
    
logo = "./data/Logo IATECH.png"
st.sidebar.image(logo)

# Customize page title
st.title("TRANFORMADAS")
# Customize page title
markdown = """Las transformaciones de imágenes suelen implicar la manipulación 
de múltiples bandas de datos, ya sea de una única imagen multiespectral o de 
dos o más imágenes de la misma zona adquiridas en diferentes momentos (es decir, 
datos de imágenes multitemporales). De cualquier manera, las transformaciones 
de imágenes generan imágenes "nuevas" a partir de dos o más fuentes que resaltan 
características o propiedades particulares de interés, mejor que las imágenes de 
entrada originales.
"""
st.markdown(markdown)

@st.cache_data(persist="disk")
def imagen(img):
    src = rasterio.open(img)
    array = src.read()
    bounds = src.bounds
    return array,bounds    

option = st.selectbox(
        "Transformada:",
        ("Kauth-Thomas", "Karhunen-Loeve"),
)
if option == "Kauth-Thomas":
    # A dummy Sentinel 2 COG I had laying around
    tif = "./data/KT_geo.tif"
if option == "Karhunen-Loeve":
    # A dummy Sentinel 2 COG I had laying around
    tif = "./data/KL_geo2.tif"
if option == None:
    # A dummy Sentinel 2 COG I had laying around
    st.write("Debe seleccionar una opcion.")

col1, col2 = st.columns((2,1))

with col1:    
    # This is probably hugely inefficient, but it works. Opens the COG as a numpy array
    #src = rasterio.open(tif)
    #array = src.read()
    #bounds = src.bounds
    
    array, bounds = imagen(tif)
    
    x1,y1,x2,y2 = bounds
    bbox = [(bounds.bottom, bounds.left), (bounds.top, bounds.right)]
    
    # Centro del Paramo
    m = folium.Map(location=[4.822, -75.289], zoom_start=12)
    
    
    img = folium.raster_layers.ImageOverlay(
        name=option, #"RGB",
        image=np.moveaxis(array, 0, -1),
        bounds=bbox,
        opacity=0.9,
        interactive=True,
        cross_origin=False,
        zindex=1,
    )
    
    # folium.Popup("I am an image").add_to(img)
    img.add_to(m)
    
    folium.LayerControl().add_to(m)
    
    # call to render Folium map in Streamlit
    folium_static(m)
    
with col2:

    if option == "Kauth-Thomas":
        # A dummy Sentinel 2 COG I had laying around
        st.write("Bandas [Brillo,Verdosidad,Humedad]")
        st.write("La transformación K-T es una mejora espectral ampliamente utilizada que emplea un conjunto de vectores propios que transforman el espacio espectral dado en un espacio de características definido. Este espacio de características ofrece al usuario una coordenada basada en la física que ayuda a describir la firma espectral de los píxeles individuales. Las dos alineaciones más frecuentes en el espacio de características son los ejes de coordenadas de brillo y verdor. Estos ejes de coordenadas de la primera transformación K-T se han vuelto muy conocidos y forman el primer plano del espacio de características definido, conocido como la tapa con borlas.")
    if option == "Karhunen-Loeve":
        # A dummy Sentinel 2 COG I had laying around
        st.write("Bandas [CP1,CP2,CP3]")
        st.write("La transformada KL también se conoce como transformada de Hoteling o transformada de vector propio. La transformada KL se basa en las propiedades estadísticas de la imagen y tiene varias propiedades importantes que la hacen útil para el procesamiento de imágenes, en particular para la compresión de imágenes.")

