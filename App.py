import streamlit as st

st.set_page_config(layout="wide") 

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image:url("file:///C:/github/streamlit-paramo/data/Logo_guardianes.jpg") top left repeat;
                background-repeat: no-repeat;
                padding-top: 150px;
                background-position: 20px 20px;
            }            
        </style>
        """,
        unsafe_allow_html=True,
    )
    
add_logo()
    
with st.sidebar:
    "# Info"
    st.write("")
    st.write("Laboratorio de Sensores Remotos \n <email://labsr@ut.edu.co>\n <https://labsr_ut.github.com>")
    st.write("")
    
    st.image("./data/Logo IATECH.png", width=250)

st.image("./data/paramo_view.jpg", caption="Paramo",  width=1200)

# Customize page title
st.title("GUARDIANES DEL PARAMO")

st.subheader("Vision")
markdown = """Esta aplicacion busca convertirse en un referente para la manipulacion 
de geodatos, para apoyar la toma de decisiones a partir de analisis multicriterio,
incorporando procesamiento automatico de imagenes satelitales utilizando metodos
avanzados (machine learning y deep learning), que permitan reducir los tiempos 
y mejorar la eficiencia, y de esta forma, impactar positivamente en la proteccion 
de los paramos en los paises que poseen este ecosistema, como son Colombia (50%), 
Venezuela, Brasil, Perú, Colombia, Chile y Ecuador. 
"""
st.markdown(markdown)

st.subheader("Importancia")
markdown = """Los paramos, son considerados ecosistemas estratégicos por la variedad de servicios ecosistémicos que 
brindan, lo que resalta el interés de su conservación. Sin embargo, en Colombia, estos ecosistemas se ven amenazados 
por la rápida propagación de especies invasoras, entre las cuales destaca el Retamo Espinoso (Ulex europaeus), un 
hermoso arbusto de origen Europeo que esta catalogado como una de las 100 especies más invasoras del mundo que se 
ha convertido en una gran problemática ambiental. Esta planta, al colonizar rápidamente la zona, pone en peligro 
la vegetación nativa, incluyendo especies emblemáticas como los frailejones (subtribu Espeletiinae). El Retamo 
Espinoso no solo contribuye a la pérdida de biodiversidad y al deterioro ecológico, sino que también favorece 
la propagación de incendios forestales debido a las sustancias altamente volátiles que contiene. Además, presenta 
una alta capacidad de rebrote tras los incendios y produce semillas que presentan alta dormancia que pueden germinar 
después de décadas. Esto requiere la implementación de estrategias que permitan su control y manejo.
"""
st.markdown(markdown)

st.subheader("Tecnologías geoespaciales")
markdown = """La propuesta se apoyara en datos geoespaciales obtenidos a través de Copernicus Browser, las imágenes 
obtenidas por medio de la plataforma Sentinel 2 permitirán capturar datos satelitales actualizados de las áreas 
afectadas y se podrá gestionar oportunamente lo siguiente:

- Cobertura espacio-temporal de toda el área
- Análisis espectral de imagenes
- Detección de cambios en la vegetación
- Identificación de zonas críticas 
"""
st.markdown(markdown)

st.subheader("Aportes")
markdown = """    
- Procesamiento automático de los datos mediante herramientas de uso libre (Python, QGIS)
- Predecir y prepararse para futuros desastres    
- Preservar la biodiversidad y los hábitats en peligro    
"""
st.markdown(markdown)

st.subheader("Integrantes")
#st.image("C:/github/streamlit-paramo/data/estudiantes.jpg", caption="Paramo",  width=900)

markdown2 = """
Se cuenta con la participacion de un selecto grupo de personas incentivadas para aportar a la conservacion de los paramos del mundo).

- Ashley Rugeles Tellez (Restauracion ecologica)
- Cristian Cordoba Montenegro (Visualizacion web)
- Evelyn Pagote Hernandez (Modelacion hidrica)
- Diana Rodriguez Umba (Prediccion Incendios)
- Jaime Lopez Carvajal (Analisis geoespacial)

"""
st.markdown(markdown2)
