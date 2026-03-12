import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

#* Etiqueta LaTeX de la serie
latex_tag = r'$\displaystyle s_n=\sum_{k=1}^{n} \frac{(-1)^{k+1}}{k}$'

#* Función que define a_n
def func_a(x: int):
    return (-1)**(x+1)*(1/x)

#* Función para calcular las sumas parciales de la serie
@np.vectorize
def sum_a(x: int):
    ind = np.arange(1,x+1)
    suc =func_a(ind)
    return np.sum(suc)

def Draw_Sucesion_1D(n , intervalo_x = [-0.05,1.05], intervalo_y = [-0.125,0.125], solo_ultimo = False, ocultar_etiquetas = False, tam_fuentes = 12):
    indices_suc= np.arange(1,n+1)

    #! iniciar figura
    fig , ax = plt.subplots(figsize=(12,1))
    aux1=min(0.5,intervalo_x[0])
    aux2=max(1,intervalo_x[1])
    dif = aux2-aux1
    ax.set_xlim(aux1-0.05*dif,aux2+0.05*dif)
    ax.set_ylim(*intervalo_y)

    #* dibujar ejes coordenados
    ax.spines[["bottom"]].set_position(("data", 0))
    ax.spines[["left", "top", "right"]].set_visible(False)
    ax.plot(1, 0, ">", transform=ax.get_yaxis_transform(), clip_on=False, color = 'black')

    #* Graficar la función
    if solo_ultimo:
        sucesion = sum_a(n)
    else:
        sucesion = sum_a(indices_suc)

    ax.scatter(sucesion,np.zeros_like(sucesion) , color='blue', s=30)

    #* etiquetas de los puntos
    if not ocultar_etiquetas:
        if solo_ultimo:
            ax.text(sucesion, 0.025 , f'$s_{{{n}}}$', fontsize=tam_fuentes, ha='center', va='bottom')
        else:
            ax.plot([sucesion[-2],sucesion[-1]], [0.07, 0.07], color='blue')
            ax.text((sucesion[-2]+sucesion[-1])/2, 0.075 , f'$b_{{{n}}}$', fontsize=tam_fuentes, ha='center', va='bottom')
            for i in range(n):
                ax.text(sucesion[i], 0.025 , f'$s_{{{i+1}}}$', fontsize=tam_fuentes, ha='center', va='bottom')

    #* etiquetas de los valores en los ejes
    etiquetas_x = np.arange(aux1, aux2+0.1*(aux2-aux1), 0.1*(aux2-aux1))
    ax.set_xticks(etiquetas_x)
    ax.set_yticks([])

    #* tamaño de fuentes en los ejes
    ax.tick_params(axis='both', which='major', labelsize=tam_fuentes)

    return ax , fig


def main():
    tam_fuentes=12

    #* intervalos x e y
    intervalo_x = [0.5,1]

    #* cantidad numero de elementos de la sucesion
    n=9

    #! Configuración de la página de Streamlit
    st.set_page_config(page_title='Ejemplo serie alternante', layout='wide', initial_sidebar_state='expanded', page_icon=':material/line_axis:')

    #! Titulo
    st.title('Ejemplo de serie alternante')

    #! Checkboxes para opciones de visualización
    n = st.sidebar.number_input('indique el valor de $n$', min_value=2, value=n, step=1)
    ocultar_etiquetas = st.sidebar.toggle('Ocultar etiquetas sucesión', value=False)
    ocultar_valor_serie = st.sidebar.toggle('Ocultar valor de la serie', value=False)

    Suma_total = sum_a(n)
    latex_suma_total = rf'$\displaystyle s_{{{n}}}={Suma_total}, \quad b_{{{n}}}={np.abs(func_a(n))}, \quad R_n = {Suma_total - np.log(2)}$'
    latex_suma_serie = r'$\displaystyle s=\sum_{k=1}^{\infty} \frac{(-1)^{k+1}}{k} = \ln(2) \approx 0,6931471806$'
    #! Generar gráfico con spinner
    with st.spinner('Generando gráfico...'):
        ax, fig = Draw_Sucesion_1D(n , intervalo_x, solo_ultimo=False, ocultar_etiquetas=ocultar_etiquetas, tam_fuentes=tam_fuentes)
        if not ocultar_valor_serie:
            ax.scatter(np.log(2), 0, color='red', s=30)
        st.pyplot(fig)
        st.markdown(f'{latex_tag}')
        st.markdown(f'{latex_suma_total}')
        st.markdown(f'{latex_suma_serie}')

if __name__ == "__main__":
    main()