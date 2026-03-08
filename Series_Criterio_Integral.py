import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

#! Ejecutar con: streamlit run Series_Criterio_Integral.py

Tam_fuentes=16

def func_f(x: float):
  return 1/x

def Draw_Criterio(n ,N, PuntosSubintervalos, intervalo_x_vent = [-0.5,10.5], intervalo_y_vent = [-0.075,1.075], intervalo_x_graf = [0,10.5], SumaSuperior = True, SumaInferior = True, mostrar_funcion = True, Mostrar_integral = False):
  #! iniciar figura
  fig , ax = plt.subplots(figsize=(20,10))
  ax.set_xlim(*intervalo_x_vent)
  ax.set_ylim(*intervalo_y_vent)

  #* Elegir las etiquetas de los ejes
  ax.set_yticks([])
  ax.set_yticklabels([])
  ax.set_xticks(PuntosSubintervalos)
  ax.set_xticklabels(PuntosSubintervalos)

  #* dibujar ejes coordenados
  ax.spines[["left", "bottom"]].set_position(("data", 0))
  ax.spines[["top", "right"]].set_visible(False)
  ax.plot(1, 0, ">", transform=ax.get_yaxis_transform(), clip_on=False, color='black')
  ax.plot(0, 1, "^", transform=ax.get_xaxis_transform(), clip_on=False, color='black')

  #* Graficar la función
  x = np.linspace(intervalo_x_graf[0],intervalo_x_graf[1], N)
  y = func_f(x)
  if mostrar_funcion:
    ax.plot(x, y, color='black', label=r'$f(x)$')
    ax.text(intervalo_x_graf[1],func_f(intervalo_x_graf[1]),r'$f(x)$', fontsize=Tam_fuentes, color='black', verticalalignment='top', horizontalalignment='right')

  #* Graficar los rectangulos izquierda
  if SumaSuperior:
    for i in range(n-1):
      ax.plot([PuntosSubintervalos[i],PuntosSubintervalos[i+1],PuntosSubintervalos[i+1],PuntosSubintervalos[i],PuntosSubintervalos[i]],[0,0,func_f(PuntosSubintervalos[i]),func_f(PuntosSubintervalos[i]),0],color='blue')
      ax.fill_between([PuntosSubintervalos[i],PuntosSubintervalos[i+1]],[func_f(PuntosSubintervalos[i]),func_f(PuntosSubintervalos[i])],color='lightblue')
      ax.text(PuntosSubintervalos[i]+0.15,func_f(PuntosSubintervalos[i])+0.02,r'$a_{'+str(i+1)+'}$', fontsize=Tam_fuentes, color='blue', verticalalignment='center', horizontalalignment='center')

  #* Graficar la integral
  if Mostrar_integral:
    x_integral = np.linspace(PuntosSubintervalos[0], PuntosSubintervalos[-1], N)
    ax.fill_between(x_integral, func_f(x_integral), color='gray', alpha=0.5, label=r'$\int_{1}^{10} f(x) dx$', edgecolor='black')
    ax.text(intervalo_x_graf[1],func_f(intervalo_x_graf[1])+0.05,r'$\int_{1}^{10} f(x) dx$', fontsize=Tam_fuentes, color='black', verticalalignment='bottom', horizontalalignment='right')

  #* Graficar los rectangulos derecha
  if SumaInferior:
    for i in range(n-1):
      ax.plot([PuntosSubintervalos[i],PuntosSubintervalos[i+1],PuntosSubintervalos[i+1],PuntosSubintervalos[i],PuntosSubintervalos[i]],[0,0,func_f(PuntosSubintervalos[i+1]),func_f(PuntosSubintervalos[i+1]),0],color='brown')
      ax.fill_between([PuntosSubintervalos[i],PuntosSubintervalos[i+1]],[func_f(PuntosSubintervalos[i+1]),func_f(PuntosSubintervalos[i+1])],color='orange')
      ax.text(PuntosSubintervalos[i+1]-0.15,func_f(PuntosSubintervalos[i+1])-0.02,r'$a_{'+str(i+2)+'}$', fontsize=Tam_fuentes, color='brown', verticalalignment='center', horizontalalignment='center')

  return fig


def main():
  #* intervalos x e y
  intervalo_x_vent = [-0.5,10.5]
  intervalo_y_vent = [-0.075,1.075]
  intervalo_x_graf = [0.01,10.5]

  #* cantidad numero de elementos de la sucesion
  n=10

  #* puntos en el dominio para la sucesion
  PuntosSubintervalos=np.arange(1,n+1,1)

  #* cantidad de puntos en el intervalo del grafico para la función
  N=100

  #! Configuración de la página de Streamlit
  st.set_page_config(page_title="Criterio de la integral", layout="wide", initial_sidebar_state='expanded', page_icon=':material/line_axis:')

  #! Titulo
  st.title('Visualización criterio de la integral')

  #! Checkboxes para opciones de visualización
  mostrar_funcion = st.sidebar.checkbox('Mostrar función', value=True)
  SumaSuperior = st.sidebar.checkbox(r'Mostrar $\{a_{n}\}_{n=1}^{9}$', value=True)
  SumaInferior = st.sidebar.checkbox(r'Mostrar $\{a_{n}\}_{n=2}^{10}$', value=True)
  Integral = st.sidebar.checkbox('Mostrar integral', value=False)

  #! Generar gráfico con spinner
  with st.spinner('Generando gráfico...'):
    fig = Draw_Criterio(n ,N, PuntosSubintervalos, intervalo_x_vent, intervalo_y_vent,intervalo_x_graf, SumaSuperior, SumaInferior, mostrar_funcion, Mostrar_integral=Integral)
    st.pyplot(fig)
    st.markdown(r'$a_{n}=f(n)$')

if __name__ == "__main__":
  main()