import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

#* Función que define la sucesión a_n
def func_a(x: int):
    return ((-1)**x)*(1/x)

def Draw_Sucesion_1D(n , intervalo_x = [-1,1], intervalo_y = [-1,1],solo_ultimo = False, ocultar_etiquetas = False, tam_fuentes = 12):
    #* calcular valores de la sucesión
    indices_suc= np.arange(1,n+1)
    if solo_ultimo:
        sucesion = func_a(n)
    else:
        sucesion = func_a(indices_suc)

    #* iniciar figura
    fig , ax = plt.subplots(figsize=(10,1))
    aux1=min(intervalo_x[0], np.min(sucesion))
    aux2=max(intervalo_x[1], np.max(sucesion))
    dif = aux2-aux1
    ax.set_xlim(aux1-0.05*dif,aux2+0.05*dif)
    ax.set_ylim(*intervalo_y)
    indices_suc= np.arange(1,n+1)
    if solo_ultimo:
        sucesion = func_a(n)
    else:
        sucesion = func_a(indices_suc)

    #* iniciar figura
    fig , ax = plt.subplots(figsize=(10,1))
    aux1=min(intervalo_x[0], np.min(sucesion))
    aux2=max(intervalo_x[1], np.max(sucesion))
    dif = aux2-aux1
    ax.set_xlim(aux1-0.05*dif,aux2+0.05*dif)
    ax.set_ylim(*intervalo_y)

    #* dibujar ejes coordenados
    ax.spines[["bottom"]].set_position(("data", 0))
    ax.spines[["left", "top", "right"]].set_visible(False)
    ax.plot(1, 0, ">", transform=ax.get_yaxis_transform(), clip_on=False, color='black')

    #* Graficar la sucesión
    ax.scatter(sucesion,np.zeros_like(sucesion) , color='blue', s=30)

    #* etiquetas de los puntos
    if not ocultar_etiquetas:
        if solo_ultimo:
            ax.text(sucesion, 0.025 , f'$a_{{{n}}}$', fontsize=tam_fuentes, ha='center', va='bottom')
        else:
            for i in range(n):
                ax.text(sucesion[i], 0.025 , f'$a_{{{i+1}}}$', fontsize=tam_fuentes, ha='center', va='bottom')

    #* etiquetas de los valores en los ejes
    etiquetas_x = np.arange(aux1, aux2+0.1*(aux2-aux1), 0.1*(aux2-aux1))
    ax.set_xticks(etiquetas_x)
    ax.set_yticks([])

    #* tamaño de fuentes en los ejes
    ax.tick_params(axis='both', which='major', labelsize=tam_fuentes)

    return fig , ax


def main():
    #! Configuración de la página de Streamlit
    st.set_page_config(page_title="Visualización 1D de una sucesión", layout="wide", initial_sidebar_state='expanded', page_icon=':material/line_axis:')

    #! Titulo
    st.title('Visualización 1D de una sucesión')

    #! Checkboxes para opciones de visualización
    n = st.sidebar.number_input('indique el valor de $n$', min_value=1, value=6, step=1)
    ocultar_etiquetas = st.sidebar.toggle('Ocultar etiquetas sucesión', value=False)
    solo_ultimo = st.sidebar.toggle('Mostrar solo el término actual', value=False)

    #! Generar gráfico con spinner
    with st.spinner('Generando gráfico...'):
        fig , _ = Draw_Sucesion_1D(n, solo_ultimo=solo_ultimo, ocultar_etiquetas=ocultar_etiquetas)
        st.pyplot(fig)
        st.markdown(f'Grafico sucesión $a_n = \\dfrac{{(-1)^{{n}}}}{{n}}$')

if __name__ == "__main__":
    main()
