import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd


st.set_page_config(layout="wide")   

# Customize the sidebar
markdown = """
Semillero IATECH: <https://iatech.ut.app>
Laboratorio LabSR: <https://labsr_ut.github.com>
"""

with st.sidebar:
    "# Info"
    st.write("")
    st.write("Laboratorio de Sensores Remotos \n <email://labsr@ut.edu.co>\n <https://labsr_ut.github.com>")
    st.write("")
logo = "./data/Logo IATECH.png"
st.sidebar.image(logo)

# Customize page title
st.title("HIDROGRAFIA")
# Customize page title
    
st.markdown(
"""
Visualizacion de los drenajes del paramo
"""
)

col1, col2 = st.columns((2,1))

with col1:

    bordersStyle={
    'color': 'blue',
    'weight': 2,
    'fillColor': 'blue',
    'fillOpacity': 0.2
    } 
    
    bordersStyle2={
    'color': 'black',
    'weight': 2,
    'fillColor': 'black',
    'fillOpacity': 0.2
    } 
    width = 600
    height = 500
    
    m = leafmap.Map(center=[4.822, -75.289], zoom=12)
    
    in_geojson = "C:/github/streamlit-paramo/data/ROI_corregido2.geojson"
    m.add_geojson(in_geojson, layer_name="ROI", style_function=lambda x:bordersStyle2)
    in_geojson = "C:/github/streamlit-paramo/data/Drenajes2.geojson"
    m.add_geojson(in_geojson, layer_name="Drenajes", style_function=lambda x:bordersStyle)
    
    m.to_streamlit(width, height)

with col2:
    #grayscale = original.convert('LA')
    st.subheader("Estadisticas:")
    
    gdf = gpd.read_file("C:/github/streamlit-paramo/data/Drenajes2.gpkg")
    
    st.write("Numero de drenajes:", gdf.shape[0])
    st.write("Longitud maxima (Km):", gdf['Longitud (Km)'].max())
    st.write("Longitud minima (Km):", gdf['Longitud (Km)'].min())
    st.write("Longitud promedio (Km):", gdf['Longitud (Km)'].mean().round(2))
    st.write("Longitud total (Km):", gdf['Longitud (Km)'].sum())
