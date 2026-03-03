import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

tam_fuentes=12


def func_f(x: float):
    # return (-1)**x*(0.1+1/x)
    return ((np.cos(x))**2)/x

def Draw_Sucesion_2D(n , intervalo_x = [-0.5,6.5], intervalo_y = [-0.125,1.125], ocultar_numeros = False, ocultar_etiquetas = False):
    indices_suc= np.arange(1,n+1)
    sucesion = func_f(indices_suc)
    min_suc = np.min(sucesion)
    max_suc = np.max(sucesion)

    #! iniciar figura
    fig , ax = plt.subplots(figsize=(10,5))

    aux1_x=min(0,intervalo_x[0])
    aux2_x=max(5,max(intervalo_x[1],n))
    dif_x = aux2_x-aux1_x
    rango_x = (aux1_x-0.05*dif_x,aux2_x+0.05*dif_x)
    ax.set_xlim(rango_x)

    aux1_y=min(min_suc,intervalo_y[0])
    aux2_y=max(max_suc,intervalo_y[1])
    dif_y = aux2_y-aux1_y
    rango_y = (aux1_y-0.05*dif_y,aux2_y+0.05*dif_y)
    ax.set_ylim(rango_y)

    #* dibujar ejes coordenados
    ax.spines[["left", "bottom"]].set_position(("data", 0))
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

    # Graficar la función
    ax.scatter(indices_suc, sucesion, color='blue', s=10)

    # etiquetas de los puntos
    if not ocultar_etiquetas:
        desp = 0.04*(rango_y[1]-rango_y[0])
        for i in range(n):
            ax.text(indices_suc[i]+0.05, sucesion[i]+0.02 if sucesion[i] >= 0 else sucesion[i]-desp, f'$a_{{{i+1}}}$', fontsize=tam_fuentes, ha='center', va='bottom')

    # etiquetas de los valores en los ejes
    if ocultar_numeros:
        ax.set_xticks([])
    else:
        ax.set_xticks(indices_suc)
    ax.set_yticks(np.arange(aux1_y, aux2_y+0.1*(aux2_y-aux1_y), 0.1*(aux2_y-aux1_y)))

    # tamaño de fuentes en los ejes
    ax.tick_params(axis='both', which='major', labelsize=tam_fuentes)

    return fig


def main():
    # intervalos x e y
    intervalo_x = [0,6]
    intervalo_y = [0,0.5]

    # cantidad numero de elementos de la sucesion
    n=6

    #! Configuración de la página de Streamlit
    st.set_page_config(page_title="Visualización 2D de una sucesión", layout="wide", initial_sidebar_state='expanded', page_icon=':material/line_axis:')

    #! Titulo
    st.title('Visualización 2D de una sucesión')

    #! Checkboxes para opciones de visualización
    n = st.sidebar.number_input('indique el valor de $n$', min_value=1, value=n, step=1)
    ocultar_etiquetas = st.sidebar.toggle('Ocultar etiquetas sucesión', value=False)
    ocultar_numeros = st.sidebar.toggle('Ocultar etiquetas eje $x$', value=False)

    #! Generar gráfico con spinner
    with st.spinner('Generando gráfico...'):
        fig = Draw_Sucesion_2D(n , intervalo_x, intervalo_y, ocultar_numeros=ocultar_numeros, ocultar_etiquetas=ocultar_etiquetas)
    st.pyplot(fig)
    st.markdown(r'Grafico sucesión $a_n = \dfrac{\cos^2(n)}{n}$')

if __name__ == "__main__":
    main()