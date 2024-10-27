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
    st.write("Laboratorio de Sensores Remotos \n <email:labsr@ut.edu.co>\n <https://labsr_ut.github.com>")
    st.write("")
    
    st.image("./data/Logo IATECH.png", width=250)

# Customize page title
st.title("MODELO DE ELEVACION DIGITAL (DEM)")
# Customize page title
markdown = """Un modelo digital de elevación (DEM) es una representación de la superficie topográfica del suelo 
desnudo (tierra desnuda) que excluye árboles, edificios y cualquier otro objeto de la superficie. Los DEM se pueden crea
a partir de diferentes fuentes, este se obtuvo de datos ALOS-PALSAR, con una resolucion espacial de 12.5 metros.
"""
st.markdown(markdown)

@st.cache_data(persist="disk")
def imagen(img):
    src = rasterio.open(img)
    array = src.read()
    bounds = src.bounds
    return array,bounds  

# A dummy Sentinel 2 COG I had laying around
tif = "./data/DEM_Paramo.tif"
# This is probably hugely inefficient, but it works. Opens the COG as a numpy array
#src = rasterio.open(tif)
#array = src.read()
#bounds = src.bounds
array, bounds = imagen(tif)

col1, col2 = st.columns((2,1))

with col1:

    x1,y1,x2,y2 = bounds
    bbox = [(bounds.bottom, bounds.left), (bounds.top, bounds.right)]
    
    # Centro del Paramo
    m = folium.Map(location=[4.822, -75.289], zoom_start=12)
    
    # add marker for Liberty Bell
    tooltip = "Centroide"
    folium.Marker(
        [4.822, -75.289], popup="Centroide", tooltip=tooltip
    ).add_to(m)
    
    layer = folium.GeoJson(
    data=(open("./data/Paramo_contornos200m.geojson", "r").read()), name='Contornos 200m').add_to(m)
    
    layer = folium.GeoJson(
    data=(open("./data/ROI_corregido2.geojson", "r").read()), name='Limite').add_to(m)
    
    # Define a Branca colormap for the colorbar
    vmin = 3000 #0.2
    vmax = 6000 #0.8
    palette = ['red', 'orange', 'yellow', 'cyan', 'blue', 'darkblue'][::-1]  
    cmap = cm.LinearColormap(colors=palette,
                             vmin=vmin,
                             vmax=vmax,
                             caption='Altura sobre el nivel del mar')
    
    img = folium.raster_layers.ImageOverlay(
        name="ALOS DEM",
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
    
    # call to render Folium map in Streamlit
    folium_static(m)

with col2:
    #grayscale = original.convert('LA')
    st.subheader("Estadisticas:")
    
    hmax = np.max(array[np.nonzero(array)])
    hmin = np.min(array[np.nonzero(array)])
    
    st.write("Altura maxima (metros):", hmax)
    st.write("Altura minima (metros):", hmin)
    st.write("Rango de alturas (metros):", hmax- hmin)
    st.write("Centroide (lat,lon):", (4.822, -75.289))





