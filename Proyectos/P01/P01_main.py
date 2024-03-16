import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image as im

import proyecto, final

st.set_page_config(
    page_title="Proyecto 01",
    page_icon=':frog:',
    layout="wide"
)

class MultiApp:
    def __init__(self):
        self.apps = []
    def add_app(self, tittle, func):
        self.apps.append({
            "title": tittle,
            "function": func
        })
    def run():
        with st.sidebar: # Se hara una barra en donde estarán las diferentes páginas
            app = option_menu(
                menu_title='Páginas ',
                options=['Inicio', 'Proyecto', 'Conclusiones'], # Nombre de cada pestaña
                icons=['house-fill', 'bezier', 'body-text'], #Iconos de las pestañas
                menu_icon='alt',
                default_index=0, # En este se define la primera página en mostrarse
                styles={
                    "container": {"padding": "5!important", "background-color":'black'},
                    "icon":{"color":"white", "font-size":"16px"},
                    "nav-link":{"color":"white", "font-size": "13px", "text-align":"left", "margin":"0px","--hover-color":"sepia"},
                    "nav-link-selected":{"background-color":"darkolivegreen"}
                }
            )
        if app == "Inicio":
            st.title('Proyecto 01: Distribución binomial en lanzamiento de monedas')
            c1, c2 = st.columns([1,5])
            with c1:
                opt = st.radio("", ["Proyecto", "Referencias"], label_visibility="collapsed")
            with c2: 
                if opt == "Proyecto":
                    st.markdown("## Resumen del trabajo")
                    st.write("En la siguiente práctica se procedió a realizar una aplicación web encargada de graficar los datos obtenidos, tras 100 repeticiones, al lanzar un grupo de 10 fichas. Para ello, se emplearon las librerías de *NumPy*, *Pandas*, *Plotly.Express*, *MatPlotLib*, *StreamLit* y *SciPy*.")
                    st.write("")
                    st.write("Se realizarón 100 repeticiones para el lanzamiento de 10 fichas, en las cuales se contaron el número de caras obtenidas por cada repetición, registrandolas como *n*. A partir de los datos obtenidos, convirtiendo las *n* caras por cada repetición, se realizarón las tablas con la librería de **Pandas.DataFrame()** y a partir de estas se hicieron las graficas de **Plotly.Expres** y **PyPlot**. Para el fit se usa el arreglo de **Numpy**, además de utilizar la función **curve_fit** de la librería de **scipy.optimize**.")
                    st.write("")
                    st.write("Se lograron realizar buenos ajustes de la curva, a partir de la función binomial, obteniendo una gráfica identica tanto a partir de la importación de la función binomial a partir del modulo **stats** de la librería de **scipy**, como de la definición de la función binomial a partir de los parámetros *n*, *x* y *p*, empleando el comando **def**.")
                
                    st.markdown("## Marco Teórico")
                    # A partir de aquí se escribe para el marco teórico
                    st.write(
                        """
                        ### Distribución binomial
                    
                        Es una distribución de probabilidad discreta que cuenta la cantidad de éxitos en $$n$$ casos con una
                        probabilidad fija $$p$$. Se caracteriza porque únicamente existe dos casos: éxito y fracaso. Además la
                        probabilidad $$p$$ es fija, lo que quiere decir que la probabilidad de éxito o fracaso en cada uno de
                        los casos no depende de lo que haya sucedido en el anterior.
                    
                        #### Fórmula
                        """
                        r'''
                        $$
                        P_b(x,n)=\begin{pmatrix}
                            n\\
                            x
                        \end{pmatrix}
                        p^x(1-p)^{n-x}=\frac{n!}{x!(n-x)!}\cdot p^x(1-p)^{n-x}
                        $$
                        '''
                        """
                        Donde $$P_b(x,n)$$ es la probabilidad de $$x$$ aciertos en $$n$$ ensayos, cada uno con probabilidad
                        $$p$$.
                    
                        #### Media y desviación estándar
                    
                        La media de una distribución binomial es de la forma:
                        """
                        r'''
                        $$
                        \mu=np
                        $$
                        '''
                        """
                        La desviación estándar viene dada por:
                        """
                        r'''
                        $$
                        \sigma=\sqrt{npq}=\sqrt{np(1-p)}
                        $$
                        '''
                    )
                    st.markdown("## Definición del problema o caso de estudio")
                    st.write('El presente trabajo tiene como proposito el determinar, de manera experimental, la distribución de probabilidad que presenta el lanzamiento de monedas, de las cuales se sabe que el resultado de cada moneda lanzada es de caracter arbitrario. ')
                        
                if opt == "Referencias":
                    st.markdown("## Referencias bibliográficas (marco teórico)")
                    wpages1 = ["a", '']
                    st.write(wpages1)
                    
                    
                    st.markdown("## Referencias bibliográficas (documentación)")
                    wpages2 = ['st.radio: https://docs.streamlit.io/library/api-reference/widgets/st.radio', '']
                    st.write(wpages2)
            
        if app == "Proyecto":
            proyecto.app()
            
        if app == "Conclusiones":
            final.app()

    run()