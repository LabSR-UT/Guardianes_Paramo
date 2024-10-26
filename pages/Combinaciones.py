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
st.title("COMBINACIONES")
# Customize page title
markdown = """Se puede obtener información valiosa de las imágenes satelitales, aprovechando
 el poder de los sensores multiespectrales para ver información nueva 
y única del espectro electromagnético, normalmente no visible para los seres humanos. 
Estan disponibles algunas combinaciones de bandas útiles con imagenes Sentinel-2 con 
su aplicacion mas importante.
"""
st.markdown(markdown)

@st.cache_data(persist="disk")
def imagen(img):
    src = rasterio.open(img)
    array = src.read()
    bounds = src.bounds
    return array,bounds    

option = st.selectbox(
        "Combinacion:",
        ("Color natural", "Composicion Infrarroja", "Agricultura", "Vegetacion", "Urbano"),
)
if option == "Color natural":
    # A dummy Sentinel 2 COG I had laying around
    tif = "./data/RGB_geo2.tif"
if option == "Composicion Infrarroja":
    # A dummy Sentinel 2 COG I had laying around
    tif = "./data/CIR_geo2.tif"
if option == "Agricultura":
    # A dummy Sentinel 2 COG I had laying around
    tif = "./data/AGRI_geo.tif"  
if option == "Vegetacion":
    # A dummy Sentinel 2 COG I had laying around
    tif = "./data/ANA_geo.tif"  
if option == "Urbano":
    # A dummy Sentinel 2 COG I had laying around
    tif = "./data/SUE_geo.tif"  
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

    if option == "Color natural":
        # A dummy Sentinel 2 COG I had laying around
        st.write("Bandas [4,3,2]")
        st.write("Esta combinacion replica la visión natural de los seres humanos, donde la vegetación saludable presenta un color verde.")
    if option == "Composicion Infrarroja":
        # A dummy Sentinel 2 COG I had laying around
        st.write("Bandas [8,4,3]")
        st.write("Combinacion util para analizar la vegetación. La clorofila en la vegetación verde sana refleja la banda del infrarrojo cercano. La vegetación verde sana aparece de un rojo brillante, mientras que la vegetación muerta o dañada aparece de un gris o verde.")
    if option == "Agricultura":
        # A dummy Sentinel 2 COG I had laying around
        st.write("Bandas [11,8A,2]")
        st.write("Combinacion util análisis para la detección de zonas de uso agrícola, los cuales aparecerán representados en una tonalidad verde brillante.")
    if option == "Vegetacion":
        # A dummy Sentinel 2 COG I had laying around
        st.write("Bandas [8A,11,2]")
    if option == "Urbano":
        # A dummy Sentinel 2 COG I had laying around
        st.write("Bandas [12,11,4]")
        st.write("Combinacion util en estudios de vegetación de alguna área de interés, ya que la reflectancia en la zona infrarroja de onda corta (SWIR) se debe principalmente al contenido de humedad en las hojas o el suelo.")
    


