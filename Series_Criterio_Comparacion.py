import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

#* Etiquetas de las sucesiones en formato LaTeX para mostrar en el gráfico
texto_sucesion_a = r'$a_n = \dfrac{(\cos(n))^2}{n^2}$'
texto_sucesion_b = r'$b_n = \dfrac{1}{n^2}$'

#* Función que define la sucesión a_n
def func_a(x: float):
    return ((np.cos(x))**2)/(x**2)

#* Función para las sumas parciales de la sucesión a_n
@np.vectorize
def func_sum_a(x: float):
    ind = np.arange(1,x+1)
    suc = ((np.cos(ind))**2)/(ind**2)
    return np.sum(suc)

#* Función que define la sucesión b_n
def func_b(x: float):
    return 1/(x**2)

#* Función para las sumas parciales de la sucesión b_n
@np.vectorize
def func_sum_b(x: float):
    ind = np.arange(1,x+1)
    suc = 1/(ind**2)
    return np.sum(suc)

def Draw_Sucesion_2D(n , intervalo_x = [0,6], intervalo_y = [0,1], ocultar_numeros = False, ocultar_etiquetas = False, ocultar_a = False, ocultar_b = False, ocultar_sumas = True, ocultar_funciones = True, tam_fuentes = 12):
    indices_suc= np.arange(1,n+1)
    sucesion_f = func_a(indices_suc)
    suma_sucesion_f = func_sum_a(indices_suc)
    sucesion_g = func_b(indices_suc)
    suma_sucesion_g = func_sum_b(indices_suc)

    if not ocultar_sumas:
        min_suc = np.min([np.min(sucesion_f), np.min(sucesion_g), np.min(suma_sucesion_f), np.min(suma_sucesion_g)])
        max_suc = np.max([np.max(sucesion_f), np.max(sucesion_g), np.max(suma_sucesion_f), np.max(suma_sucesion_g)])
    else:
        min_suc = np.min([np.min(sucesion_f), np.min(sucesion_g)])
        max_suc = np.max([np.max(sucesion_f), np.max(sucesion_g)])

    #! iniciar figura
    fig , ax = plt.subplots(figsize=(10,5))

    aux1_x=min(0,intervalo_x[0])
    aux2_x=max(intervalo_x[1],n)
    dif_x = aux2_x-aux1_x
    rango_x = (aux1_x-0.05*dif_x,aux2_x+0.05*dif_x)
    ax.set_xlim(rango_x)

    aux1_y=np.min([min_suc,intervalo_y[0]])
    aux2_y=np.max([max_suc,intervalo_y[1]])
    dif_y = aux2_y-aux1_y
    rango_y = (aux1_y-0.05*dif_y,aux2_y+0.05*dif_y)
    ax.set_ylim(rango_y)

    #* dibujar ejes coordenados
    ax.spines[["left", "bottom"]].set_position(("data", 0))
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">", transform=ax.get_yaxis_transform(), clip_on=False, color = 'black')
    ax.plot(0, 1, "^", transform=ax.get_xaxis_transform(), clip_on=False, color = 'black')

    #* Graficar las sucesiones, sumas y funciones
    if not ocultar_a:
        ax.scatter(indices_suc, sucesion_f, color='blue', s=10)
        if not ocultar_sumas:
            ax.scatter(indices_suc, suma_sucesion_f, color='lightblue', s=10, marker='x')
        if not ocultar_funciones:
            x_func = np.linspace(rango_x[0], rango_x[1], 400)
            ax.plot(x_func, func_a(x_func), color='blue', linestyle=':')

    if not ocultar_b:
        ax.scatter(indices_suc, sucesion_g, color='red', s=10)
        if not ocultar_sumas:
            ax.scatter(indices_suc, suma_sucesion_g, color='coral', s=10, marker='x')
        if not ocultar_funciones:
            x_func = np.linspace(rango_x[0], rango_x[1], 400)
            ax.plot(x_func, func_b(x_func), color='red', linestyle=':')

    #* etiquetas de los puntos
    if not ocultar_etiquetas:
        desp = 0.04*(rango_y[1]-rango_y[0])
        for i in range(n):
            if not ocultar_a:
                ax.text(indices_suc[i]+0.05, sucesion_f[i]+0.02 if sucesion_f[i] >= 0 else sucesion_f[i]-desp, f'$a_{{{i+1}}}$', fontsize=tam_fuentes, ha='center', va='bottom')
                if not ocultar_sumas:
                    ax.text(indices_suc[i]+0.05, suma_sucesion_f[i]+0.02 if suma_sucesion_f[i] >= 0 else suma_sucesion_f[i]-desp, f'$Sa_{{{i+1}}}$', fontsize=tam_fuentes, ha='center', va='bottom')
            if not ocultar_b:
                ax.text(indices_suc[i]+0.05, sucesion_g[i]+0.02 if sucesion_g[i] >= 0 else sucesion_g[i]-desp, f'$b_{{{i+1}}}$', fontsize=tam_fuentes, ha='center', va='bottom')
                if not ocultar_sumas:
                    ax.text(indices_suc[i]+0.05, suma_sucesion_g[i]+0.02 if suma_sucesion_g[i] >= 0 else suma_sucesion_g[i]-desp, f'$Sb_{{{i+1}}}$', fontsize=tam_fuentes, ha='center', va='bottom')

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
    tam_fuentes=12

    #* intervalos x e y
    intervalo_x = [0,6]
    intervalo_y = [0,1]

    #* cantidad numero de elementos de la sucesion
    n=6

    #! Configuración de la página de Streamlit
    st.set_page_config(page_title="Visualización criterio de comparación", layout="wide", initial_sidebar_state='expanded', page_icon=':material/line_axis:')

    #! Titulo
    st.title('Visualización criterio de comparación')

    #! Checkboxes para opciones de visualización
    n = st.sidebar.number_input('indique el valor de $n$', min_value=1, value=n, step=1)
    ocultar_etiquetas = st.sidebar.toggle('Ocultar etiquetas sucesión', value=False)
    ocultar_numeros = st.sidebar.toggle('Ocultar etiquetas eje $x$', value=False)
    ocultar_a = st.sidebar.toggle('Ocultar sucesión $a_n$', value=False)
    ocultar_b = st.sidebar.toggle('Ocultar sucesión $b_n$', value=False)
    ocultar_sumas = st.sidebar.toggle('Ocultar sumas sucesiones', value=True)
    ocultar_funciones = st.sidebar.toggle('Ocultar funciones de $a_n$ y $b_n$', value=True)

    #! Generar gráfico con spinner
    with st.spinner('Generando gráfico...'):
        fig = Draw_Sucesion_2D(n , intervalo_x, intervalo_y, ocultar_numeros=ocultar_numeros, ocultar_etiquetas=ocultar_etiquetas, ocultar_a=ocultar_a, ocultar_b=ocultar_b, ocultar_sumas=ocultar_sumas, ocultar_funciones=ocultar_funciones, tam_fuentes=tam_fuentes)
        st.pyplot(fig)
        if not ocultar_a:
            st.markdown(rf"{texto_sucesion_a}")
        if not ocultar_b:
            st.markdown(rf"{texto_sucesion_b}")

if __name__ == "__main__":
    main()