import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

#* función a aproximar
def func_f(x):
    return np.log(1+x)

#* polinomio de Taylor de la función func_f en x=0
@np.vectorize
def Taylor(x, n):
    return np.sum([((-1)**(i+1))*(x**i)/i for i in range(1,n+1)])

#* Función para dibujar la función y su polinomio de Taylor
def Draw_Taylor(n, intervalo_x=[-0.99,10.1], intervalo_x_graf = [-2.01,6.1], intervalo_y_graf = [-2.1,2.1], tam_fuentes=12):
    Res_EjeX=1000

    fig = plt.figure(figsize=(20,10))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlim(*intervalo_x_graf)
    ax.set_ylim(*intervalo_y_graf)

    x=np.linspace(*intervalo_x,Res_EjeX)
    y=func_f(x[x>-1])

    #* dibujar ejes coordenados
    ax.spines[["left", "bottom"]].set_position(("data", 0))
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">", transform=ax.get_yaxis_transform(), clip_on=False, color = 'black')
    ax.plot(0, 1, "^", transform=ax.get_xaxis_transform(), clip_on=False, color = 'black')
    ax.set_xlabel(f'$x$', fontsize=tam_fuentes,loc='right')
    ax.set_ylabel(f'$y$', fontsize=tam_fuentes,loc='top',rotation='horizontal')

    #* Grafico de la función
    ax.plot(x,y,color='blue')

    #* Grafico el polinomio de Taylor
    x_T = np.linspace(*intervalo_x_graf,Res_EjeX)
    y_T = Taylor(x_T,n)
    ax.plot(x_T,y_T,color='red')

    ax.text(intervalo_x_graf[0],intervalo_y_graf[1],f'$n = {n}$', fontsize=tam_fuentes, color= 'black',horizontalalignment='left',verticalalignment='center')

    return fig , ax

def main():
    #! Configuración de la página de Streamlit
    st.set_page_config(page_title="Serie de Taylor de la función ln(1+x)", layout="wide", initial_sidebar_state='expanded', page_icon=':material/line_axis:')

    #! Titulo
    st.title(r'Serie de Taylor de la función $\ln(1+x)$')

    #! Checkboxes para opciones de visualización
    n = st.sidebar.number_input('indique el valor de $n$', min_value=0, value=6, step=1)

    #! Generar gráfico con spinner
    with st.spinner('Generando gráfico...'):
        fig , _ = Draw_Taylor(n)
        st.pyplot(fig)

if __name__ == "__main__":
    main()