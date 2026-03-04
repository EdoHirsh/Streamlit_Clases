import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

tam_fuentes=12

#* Etiqueta de las sucesiones en formato LaTeX para mostrar en el gráfico
latex_tag_funcion_a=r'$a_n = 1-\dfrac{1}{n}$'
latex_tag_funcion_b=r'$b_n = 1+\dfrac{\sin(n)}{n}$'
latex_tag_funcion_c=r'$c_n = 1+\dfrac{1}{n}$'

#* Función que define la sucesión a representar
def func_a(x: float):
    return 1-1/x

def func_b(x: float):
    return 1+np.sin(x)/x

def func_c(x: float):
    return 1+1/x

#* Función para dibujar la sucesión
def Draw_Sucesion_2D(n , intervalo_x = [0,6], intervalo_y = [0,1], ocultar_numeros = False, ocultar_etiquetas = False, ocultar_funciones = False):
    indices_suc= np.arange(1,n+1)
    sucesion_a = func_a(indices_suc)
    sucesion_b = func_b(indices_suc)
    sucesion_c = func_c(indices_suc)
    min_suc = np.min([np.min(sucesion_a), np.min(sucesion_b), np.min(sucesion_c)])
    max_suc = np.max([np.max(sucesion_a), np.max(sucesion_b), np.max(sucesion_c)])

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

    #* Graficar las sucesiones
    ax.scatter(indices_suc, sucesion_a, color='blue', s=10, label=latex_tag_funcion_a)
    ax.scatter(indices_suc, sucesion_b, color='red', s=10, label=latex_tag_funcion_b)
    ax.scatter(indices_suc, sucesion_c, color='green', s=10, label=latex_tag_funcion_c)

    #* Grafico de las funciones continuas
    if not ocultar_funciones:
        x_continuo = np.linspace(1, n, 1000)
        ax.plot(x_continuo, func_a(x_continuo), color='blue', linestyle=':')
        ax.plot(x_continuo, func_b(x_continuo), color='red', linestyle=':')
        ax.plot(x_continuo, func_c(x_continuo), color='green', linestyle=':')

    #* etiquetas de los puntos
    if not ocultar_etiquetas:
        desp = 0.04*(rango_y[1]-rango_y[0])
        for i in range(n):
            ax.text(indices_suc[i]+0.05, sucesion_a[i]+0.02 if sucesion_a[i] >= 0 else sucesion_a[i]-desp, f'$a_{{{i+1}}}$', fontsize=tam_fuentes, ha='center', va='bottom')
            ax.text(indices_suc[i]+0.05, sucesion_b[i]+0.02 if sucesion_b[i] >= 0 else sucesion_b[i]-desp, f'$b_{{{i+1}}}$', fontsize=tam_fuentes, ha='center', va='bottom')
            ax.text(indices_suc[i]+0.05, sucesion_c[i]+0.02 if sucesion_c[i] >= 0 else sucesion_c[i]-desp, f'$c_{{{i+1}}}$', fontsize=tam_fuentes, ha='center', va='bottom')

    #* etiquetas de los valores en los ejes
    if ocultar_numeros:
        ax.set_xticks([])
    else:
        ax.set_xticks(indices_suc)
    ax.set_yticks(np.arange(aux1_y, aux2_y+0.1*(aux2_y-aux1_y), 0.1*(aux2_y-aux1_y)))

    #* tamaño de fuentes en los ejes
    ax.tick_params(axis='both', which='major', labelsize=tam_fuentes)

    return fig


def main():
    #* intervalos x e y
    intervalo_x = [0,10]
    intervalo_y = [0,2]

    #* cantidad numero de elementos de la sucesion
    n=10

    #! Configuración de la página de Streamlit
    st.set_page_config(page_title="Teorema del Sándwich para sucesiones", layout="wide", initial_sidebar_state='expanded', page_icon=':material/line_axis:')

    #! Titulo
    st.title('Teorema del Sándwich para sucesiones')

    #! Checkboxes para opciones de visualización
    n = st.sidebar.number_input('indique el valor de $n$', min_value=1, value=n, step=1)
    ocultar_etiquetas = st.sidebar.toggle('Ocultar etiquetas sucesión', value=False)
    ocultar_numeros = st.sidebar.toggle('Ocultar etiquetas eje $x$', value=False)
    ocultar_funciones = st.sidebar.toggle('Ocultar funciones continuas', value=True)

    #! Generar gráfico con spinner
    with st.spinner('Generando gráfico...'):
        fig = Draw_Sucesion_2D(n , intervalo_x, intervalo_y, ocultar_numeros=ocultar_numeros, ocultar_etiquetas=ocultar_etiquetas, ocultar_funciones=ocultar_funciones)
        st.pyplot(fig)
        st.markdown(f'{latex_tag_funcion_a}')
        st.markdown(f'{latex_tag_funcion_b}')
        st.markdown(f'{latex_tag_funcion_c}')

if __name__ == "__main__":
    main()