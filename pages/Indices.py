# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 09:10:24 2024

@author: USUARIO
"""
import streamlit as st
from streamlit_folium import folium_static
import folium
import rasterio
import numpy as np
import time
import cv2
import geopandas as gpd
import leafmap.foliumap as leafmap
import rioxarray
import branca
import branca.colormap as cm
from skimage import exposure
from skimage import img_as_ubyte

st.set_page_config(layout="wide")   

with st.sidebar:
    "# Info"
    st.write("")
    st.write("Laboratorio de Sensores Remotos \n <email://labsr@ut.edu.co>\n <https://labsr_ut.github.com>")
    st.write("")
    
logo = "./data/Logo IATECH.png"
st.sidebar.image(logo)

# Customize page title
st.title("INDICES DE VEGETACION")
# Customize page title
markdown = """
Los índices de vegetación (IV) son combinaciones de reflectancia de la superficie 
en dos o más longitudes de onda diseñadas para resaltar una propiedad particular 
de la vegetación. Cada indice está diseñado para acentuar una propiedad particular 
de la vegetación. Se obtuvieron a partir de bandas espectrales de imagenes Sentinel-2.
"""
st.markdown(markdown)

def normalize_to_range(image, new_min, new_max):
      min_val = np.min(image)
      max_val = np.max(image)
      normalized_image = (image - min_val) / (max_val - min_val)
      normalized_image = normalized_image * (new_max - new_min) + new_min
      return normalized_image
  
@st.cache_data(persist="disk")
def imagen(img):
    src = rasterio.open(img)
    array = src.read().squeeze()
    bounds = src.bounds
    return array,bounds  

option = st.selectbox(
    "Indices:",
    ("NDVI", "SAVI", "EVI", "CI-green", "CI-red"),
)

if option == "NDVI":
    # A dummy Sentinel 2 COG I had laying around
    tif = "C:/github/streamlit-paramo/data/ndvi_geo.tif"
if option == "SAVI":
    # A dummy Sentinel 2 COG I had laying around
    tif = "C:/github/streamlit-paramo/data/savi_geo.tif"
if option == "EVI":
    # A dummy Sentinel 2 COG I had laying around
    tif = "C:/github/streamlit-paramo/data/evi_geo.tif"  
if option == "CI-green":
    # A dummy Sentinel 2 COG I had laying around
    tif = "C:/github/streamlit-paramo/data/cigreen_geo.tif"  
if option == "CI-red":
    # A dummy Sentinel 2 COG I had laying around
    tif = "C:/github/streamlit-paramo/data/CIred_geo.tif"  
if option == None:
    # A dummy Sentinel 2 COG I had laying around
    st.write("Debe seleccionar una opcion.")
    
#src = rasterio.open(tif)
#array = src.read()  
#vmin = array.min() #0.0
#vmax = array.max() #1.0  
t1 = time.time()
array, bounds = imagen(tif)
vmin = array.min() #0.0
vmax = array.max() #1.0

#img8 = cv2.normalize(m,m,0,255,NORM_MINMAX)
#img8 = cv2.normalize(array, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
#mean, std_dev = cv2.meanStdDev(array)
#img8 = (((array - mean) / std_dev)*255).astype('uint8')
#st.write(array.dtype)
#img8 = normalize_to_range(array, new_min=0, new_max=255)
#p2, p98 = np.percentile(array, (10, 90))
#img8 = ((exposure.rescale_intensity(array, in_range=(p2, p98)))*255).astype('uint8')
#img8 = ((exposure.equalize_adapthist(array, clip_limit=0.03))*255).astype('uint8')
#st.write(img8.dtype)

col1, col2 = st.columns((2,1))
with col1:   
    # This is probably hugely inefficient, but it works. Opens the COG as a numpy array
    #src = rasterio.open(tif)
    #array = src.read()
    #bounds = src.bounds
        
    x1,y1,x2,y2 = bounds
    bbox = [(bounds.bottom, bounds.left), (bounds.top, bounds.right)]
        
    # Centro del Paramo
    m = folium.Map(location=[4.822, -75.289], zoom_start=12)
        
    # Define a Branca colormap for the colorbar
    
    palette = ['red', 'orange', 'yellow', 'cyan', 'blue', 'darkblue'][::-1]  
    cmap = cm.LinearColormap(colors=palette,
                                 vmin=vmin,
                                 vmax=vmax,
                                 caption=option)
        
    img = folium.raster_layers.ImageOverlay(
            name=option,
            #image=np.moveaxis(array, 0, -1),
            image=np.moveaxis(array, 0, -1),
            bounds=bbox,
            opacity=0.9,
            interactive=True,
            colormap=cmap,
            cross_origin=False,
            zindex=1,
    )
        
    # folium.Popup("I am an image").add_to(img)
    img.add_to(m) 
    folium.LayerControl().add_to(m)
    
    t2 = time.time()    
        
    # call to render Folium map in Streamlit
    folium_static(m)
    
    t3 = t2-t1
    st.write("Tiempo (segs):", t3)
    
with col2:

    if option == "NDVI":
        # A dummy Sentinel 2 COG I had laying around
        st.write("En términos muy simples, el índice de vegetación de diferencia normalizada (NDVI) mide el verdor y la densidad de la vegetación captada en una imagen satelital. La vegetación sana tiene una curva de reflectancia espectral muy característica de la que podemos sacar provecho calculando la diferencia entre dos bandas: la roja visible y la infrarroja cercana. El NDVI es esa diferencia expresada en forma de número, que va de -1 a 1.")
        st.write("NDVI = ((NIR - Rojo) / (NIR + Rojo)")
        st.write("Minimo: ", vmin)
        st.write("Maximo: ", vmax)
    if option == "SAVI":
        # A dummy Sentinel 2 COG I had laying around
        st.write("El índice de vegetación ajustado al suelo (SAVI) es un índice de vegetación que intenta minimizar las influencias del brillo del suelo utilizando un factor de corrección del brillo del suelo. Esto se utiliza a menudo en regiones áridas donde la cobertura vegetal es baja.")
        st.write("SAVI = ((NIR - Rojo) / (NIR + Rojo + L)) x (1 + L)")
        st.write("Minimo: ", vmin)
        st.write("Maximo: ", vmax)
    if option == "EVI":
        # A dummy Sentinel 2 COG I had laying around
        st.write("Este índice de vegetación mejorado (optimizado) esta diseñado para mejorar la señal de la vegetación con una sensibilidad mejorada en regiones de alta biomasa y un mejor monitoreo de la vegetación a través de un desacoplamiento de la señal de fondo del dosel y una reducción en las influencias atmosféricas.")
        st.write("EVI = 2.5 * (NIR - Rojo) / ((NIR + (6 x Rojo) - (7.5 x Azul)) + 1")
        st.write("Minimo: ", vmin)
        st.write("Maximo: ", vmax)
    if option == "CI-green":
        # A dummy Sentinel 2 COG I had laying around
        st.write("CI-green = (NIR / Verde) − 1")
        st.write("El índice de clorofila (CI) se aplica para calcular la cantidad total de clorofila en las plantas. En general, este índice contiene dos bandas separadas: CIverde y CIborde rojo. Estas bandas responden a ligeras variaciones en el contenido de clorofila y son constantes para la mayoría de los tipos de plantas.")
        st.write("Minimo: ", vmin)
        st.write("Maximo: ", vmax)
    if option == "CI-red":
        # A dummy Sentinel 2 COG I had laying around
        st.write("CI-red = (NIR / Rojo-edge) − 1")
        st.write("El índice de clorofila de borde rojo es un índice de vegetación que permite estimar el contenido de clorofila en las hojas. Este índice se desarrolló para estimar el contenido de clorofila de las hojas, utilizando la relación de reflectividad en las bandas de infrarrojo cercano (NIR) y de borde rojo.")  
        st.write("Minimo: ", vmin)
        st.write("Maximo: ", vmax)

