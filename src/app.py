
# your code here
from pickle import load
import streamlit as st


model = load(open('../models/decission_tree_regressor_42.sav', 'rb'))
pca = load(open('../models/pca_model2.sav', 'rb'))


st.markdown(
    """
    <style>
    .stApp {
        background-color: #f1f1f1; /* Color de fondo */
        font-family: "Roboto", serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#Título
st.markdown(
    """
    <style>
    .stApp 
        h1 {
        
        color: #231f20; /* Cambia este valor al color que desees */
        font-family: "Source Sans Pro", sans-serif;
        font-weight: bold; /* Opcional: pone el título en negrita */
        text-align: left; /* Opcional: centra el título */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título principal de la aplicación
with st.container():
    st.image("src/img.png",width=90)
st.title('Predice tu nota en el examen')

st.markdown(
    """
    <style>
    /* Cambiar el color y formato de los labels de los radios */
    .stRadio label {
        color: #231f20; /* Color del texto negro */
        font-size: 30px; /* Tamaño del texto */
        font-weight: bold; /* Negrita */
        font-family: "Roboto", serif; /* Fuente */
        text-align: left; /* Alineación */
    }

    /* Cambiar el color y formato de los labels de los sliders */
    .stSlider label {
        color: #231f20; /* Color del texto negro */
        font-size: 30px; /* Tamaño del texto */
        font-weight: bold; /* Negrita */
        font-family: "Roboto", serif; /* Fuente */
        text-align: center; /* Alineación */
    }

    /* Cambiar el color de fondo y texto de los labels */
    .stCheckbox label {
        background-color: #fff;
        color: #008080; /* Color del texto */
        font-size: 30px; /* Tamaño del texto */
        font-family: "Roboto", serif;
        font-weight: 400; /* Negrita */
        text-align: center; /* Alineación */
    }

    /* Cambiar el color de los botones seleccionados */
    .st-dt{
        background-color: #f2ca4b; /* Color de fondo de las opciones seleccionadas */
        border-radius: 10px;
    }

    /* Cambiar el color del texto al pasar el mouse por encima */
    .stRadio > div > div > div > label:hover {
        background-color: #231f20; /* Color cuando el cursor pasa por encima */
        color: white; /* Color del texto cuando se selecciona */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    /* Cambiar el color de fondo y el color del texto en el slider */
    .stSlider div {
        font-family: "Roboto", serif;
        color: #231f20; /* Color del texto */
        font-size: 16px; /* Tamaño del texto */
    }

    /* Personalizar el color del track y el botón del slider */
    .stSlider > div > div > div {
        background-color: #fffff; /* Color del track */
        height: 8px; /* Altura del track */
    }

    .stSlider > div > div > input {
        background-color: #f2ca4b; /* Color de la barra del slider */
        width: 20px; /* Ancho del slider */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.subheader("Horas de estudio")
horas_estudio = st.slider('Seleccione un número', min_value=0, max_value=44, step=1)

st.subheader("% Asistencia")
asistencia = st.slider('Seleccione un porcentaje', min_value=60, max_value=100, step=1)

st.subheader("Horas de sueño")
horas_sueño = st.slider('Seleccione un número', min_value=4, max_value=10, step=1)

st.subheader("Nota previa")
nota_previa = st.slider('Seleccione un número', min_value=50, max_value=100, step=5)

st.subheader("Tutoría")
tutoria = st.slider('Sesiones de tutoría', min_value=0, max_value=8, step=1)

st.subheader("Actividad física")
act_fisica = st.slider('Horas de actividad física', min_value=0, max_value=6, step=1)

st.subheader("Actividades extracurriculares")
act_extra = st.toggle('¿Realiza alguna?')

st.subheader("Involucramiento parental")
env_parental = st.radio(
    'Eliga uno:',
    ['Bajo', 'Medio', 'Alto'],
    index=None)

st.subheader("Tipo de escuela")
tipo_escuela = st.radio(
    'Eliga uno:',
    ['Publica', 'Privada'],
    index=None)

st.subheader("Nivel educacional de los padres")
neduc_padres = st.radio(
    'Eliga uno:',
    ['Enseñanza media', 'Universitaria', 'Postgrado'],
    index=None)

influencia=0
Family_Income_num=0
Access_to_Resources_num=0
Motivation_Level_num=0
Distance_from_Home_num=0
Teacher_Quality_num=0
Internet_Access_num=0
Learning_Disabilities_num=0

act_extra_dict= {'No': 0, 'Sí': 1}
env_parental_dict= {'Bajo': 0, 'Medio': 1, 'Alto': 2}
tipo_escuela_dict= {'Publica': 0, 'Privada': 1},
neduc_padres_dict= {'Enseñanza media': 0,
  'Universitaria': 1,
  'Postgrado': 2}

#Botón final
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #f2ca4b; /* Color de fondo del botón (Amarillo) */
        color: black; /* Color del texto */
        font-size: 45px; /* Tamaño de la fuente */
        font-weight: bold; /* Negrita */
        border-radius: 10px; /* Bordes redondeados */
        padding: 16px 24px; /* Espaciado interno */
        transition: background-color 0.3s ease; /* Efecto de transición para el color de fondo */
    }

    .stButton>button:hover {
        background-color: #f8c111; /* Color de fondo cuando se pasa el mouse*/
        color: #231f20;
        border: solid black 1px;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

if st.button('Predecir nota'):
    conversion_pca = pca.transform([horas_estudio, asistencia, horas_sueño, nota_previa, tutoria, 
                                    act_extra_dict[act_extra],env_parental_dict[env_parental], tipo_escuela_dict[tipo_escuela]], 
                                    neduc_padres_dict[neduc_padres],0,0,0,0,0,0,0,0,0)
    st.write('nota: ', model.predict(conversion_pca))