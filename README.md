# Hamilton Phytonism
## Proyecto Libre Mecánica Analítica II
## Universidad Nacional de Colombia 2023-2
### Alejandro Celis

Este repositorio alberga un proyecto libre creado como parte del curso de Mecánica Analítica II del pregrado en Física. El proyecto se centra en la creación de simulaciones gráficas utilizando Python para abordar dos problemas específicos del curso. 


## Tabla de contenido
1. [Introducción](#Introducción)
2. [Problemas](#Problemas)
3. [Resultados](#Resultados)
4. [Conclusiones](#Conclusiones)

## Introducción
En el desarrollo de este proyecto, se llevaron a cabo simulaciones en Python, haciendo uso de diversas bibliotecas como numpy, matplotlib, pyplot y FuncAnimation. El enfoque principal se centró en abordar las ecuaciones de movimiento asociadas a dos problemas dinámicos planteados en el curso. La herramienta central utilizada para resolver estas ecuaciones de movimiento, y por consiguiente, las ecuaciones diferenciales que describían los problemas, fue el método de Euler.

Para comprender mejor el proyecto a continuación se presenta una breve descripción de las herramientas de Software implementadas:

NumPy es una biblioteca de Python diseñada para operaciones numéricas eficientes. Sus características incluyen arreglos N-dimensionales para manipulación de datos, funciones matemáticas optimizadas, broadcasting para operaciones eficientes en arreglos de diferentes formas, álgebra lineal avanzada y generación de números aleatorios. En este caso, se uso como fuente de diferentes funciónes, ademas de usarse para la creación y computo de diferentes matrices necesarias en el metodo de Euler.

Matplotlib es una biblioteca de visualización en Python que ofrece una amplia gama de herramientas para la creación de gráficos estáticos, interactivos y animaciones. Es ampliamente utilizada en campos como ciencia de datos, ingeniería y ciencias naturales. Matplotlib permite crear gráficos de dispersión, líneas, barras, histogramas y más, con un control detallado sobre aspectos visuales. En el proyecto se usaron dos modulos pertenecientes a esta libreria; pyplot y FuncAnimation.

Pyplot es un módulo específico dentro de la biblioteca Matplotlib que proporciona una interfaz de estilo de scripting para crear gráficos de manera rápida y sencilla. FuncAnimation es una clase clave en Matplotlib que pertenece al módulo animation. Esta clase permite crear animaciones fácilmente al actualizar de forma iterativa un gráfico a lo largo del tiempo. Al utilizar FuncAnimation, puedes definir una función que actualiza el contenido del gráfico en cada cuadro de la animación. Herramientas utilizadas para realizar la animación y grabación de los videos.

El método de Euler es una técnica numérica fundamental para resolver ecuaciones diferenciales ordinarias (EDOs). La idea central consiste en aproximar la solución de una EDO dividiendo el intervalo de tiempo en pequeños pasos y actualizando la solución en cada paso de acuerdo con la tasa de cambio instantánea en ese punto. Esto se logra utilizando la pendiente en el punto actual para estimar el cambio en la variable dependiente. Aunque el método de Euler es simple y eficiente, puede introducir errores acumulativos, especialmente en sistemas no lineales o con pasos de tiempo grandes. 

## Problemas

### Primer Problema
Supóngase que el hilo del cual pende la masa de un péndulo simple pasa por un pequeño orificio en el soporte. Si se tira del hilo hacia arriba, a través del orificio, con una velocidad constante u en la dirección del hilo.

La ecuación de movimiento de este problema es:

$$(l-ut)\ddot{\theta}-2u\theta+g\sin\theta=0$$

### Segundo Problema
Masa pendular suspendida de un resorte espiral a la que se le permite oscilar en un plano vertical considerando la situacion donde se desprecian efectos de fricción.

Las ecuaciones de movimiento para este problema son:

$$r\ddot{\theta}+2\dot{\theta}-g\sin\theta$$
$$\ddot{r}+\dfrac{k}{m}(r-a)-g\cos\theta$$

## Resultados


## Conclusiones

* El metodo de Euler para ecuaciones diferenciales resulta divergente en nuestro caso, esto dada la alta velocidad 
que alcanza el pendulo, generando angulos fisicamente imposibles.

* El metodo de Euler es altamente dependiente de la cantidad de muestras de tiempo a simular

* Los problemas carecen de muchas restricciones físicas que provocan escenarios poco realistas y resultan ser simulaciones de situaciones ideales. Algunas de estas restricciones son: longitudes limitadas para la cuerda y el resorte, velocidades limitadas, modelación de un limite horizontal o techo.

