import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

#* Función que define la sucesión a representar
def func_a(x: float):
    return 1-1/x

#* Función para dibujar la sucesión
def Draw_Sucesion_2D(n , intervalo_x = [0,10], intervalo_y = [0,1], ocultar_numeros = False, ocultar_etiquetas = False, ocultar_funciones = False, ocultar_cota = False, tam_fuentes = 12):
    indices_suc= np.arange(1,n+1)
    sucesion = func_a(indices_suc)
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
    ax.plot(1, 0, ">", transform=ax.get_yaxis_transform(), clip_on=False, color = 'black')
    ax.plot(0, 1, "^", transform=ax.get_xaxis_transform(), clip_on=False, color = 'black')

    #* Graficar la función
    ax.scatter(indices_suc, sucesion, color='blue', s=10)

    #* Graficar la función continua
    if not ocultar_funciones:
        x_continuo = np.linspace(1, n, 1000)
        ax.plot(x_continuo, func_a(x_continuo), color='blue', linestyle=':')

    #* líneas horizontales para mostrar acotación
    if not ocultar_cota:
        ax.hlines(1,0,n+10, color='red', linestyle=':')

    #* etiquetas de los puntos
    if not ocultar_etiquetas:
        desp = 0.04*(rango_y[1]-rango_y[0])
        for i in range(n):
            ax.text(indices_suc[i]+0.05, sucesion[i]+0.02 if sucesion[i] >= 0 else sucesion[i]-desp, f'$a_{{{i+1}}}$', fontsize=tam_fuentes, ha='center', va='bottom')

    #* etiquetas de los valores en los ejes
    if ocultar_numeros:
        ax.set_xticks([])
    else:
        ax.set_xticks(indices_suc)
    ax.set_yticks(np.arange(aux1_y, aux2_y+0.1*(aux2_y-aux1_y), 0.1*(aux2_y-aux1_y)))

    #* tamaño de fuentes en los ejes
    ax.tick_params(axis='both', which='major', labelsize=tam_fuentes)

    return fig , ax


def main():
    #! Configuración de la página de Streamlit
    st.set_page_config(page_title="Sucesión Monótona Acotada", layout="wide", initial_sidebar_state='expanded', page_icon=':material/line_axis:')

    #! Titulo
    st.title('Sucesión Monótona Acotada')

    #! Checkboxes para opciones de visualización
    n = st.sidebar.number_input('indique el valor de $n$', min_value=1, value=10, step=1)
    ocultar_etiquetas = st.sidebar.toggle('Ocultar etiquetas sucesión', value=False)
    ocultar_numeros = st.sidebar.toggle('Ocultar etiquetas eje $x$', value=False)
    ocultar_funciones = st.sidebar.toggle('Ocultar funciones continuas', value=False)
    ocultar_cota = st.sidebar.toggle('Ocultar cota', value=False)

    #! Generar gráfico con spinner
    with st.spinner('Generando gráfico...'):
        fig , _ = Draw_Sucesion_2D(n, ocultar_numeros=ocultar_numeros, ocultar_etiquetas=ocultar_etiquetas, ocultar_funciones=ocultar_funciones, ocultar_cota=ocultar_cota)
        st.pyplot(fig)
        st.markdown(r'Gráfico sucesión: $\ a_n = 1-\dfrac{1}{n}$')

if __name__ == "__main__":
    main()