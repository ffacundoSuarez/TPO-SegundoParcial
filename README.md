# Sistema de Gestión: Velocity Racing Team 🏎️💨

Este proyecto corresponde al Trabajo Práctico Obligatorio (**TPO - Grupo 3**) para la materia de Fundamentos de Informática. Consiste en una aplicación de consola desarrollada en Python orientada a la gestión y análisis de rendimiento de pilotos de Fórmula 1, utilizando estructuras de datos bidimensionales (matrices) y desarrollo modular.

## 🔗 URL del Repositorio de GitHub
[https://github.com/ffacundoSuarez/TPO-SegundoParcial.git](https://github.com/ffacundoSuarez/TPO-SegundoParcial.git)

---

## 🎯 Alcance del Proyecto

El sistema está diseñado para administrar de manera centralizada la información técnica y deportiva de un equipo de carreras, procesando una matriz estructurada con los siguientes 7 atributos por cada piloto:
* `Nombre del Piloto`
* `Número de Monoplaza`
* `Escudería / Equipo`
* `Puntos en el Campeonato`
* `Tiempo Promedio por Vuelta (segundos)`
* `Presupuesto Designado`
* `Cantidad de Abandonos`

### Funcionalidades Implementadas:
1. **Carga Inicial Automatizada:** Precarga del sistema con una matriz de 10 pilotos de la parrilla real actual de F1 para facilitar pruebas inmediatas.
2. **Registrar Piloto (Alta):**
   * **Carga Manual:** Validación en tiempo real de tipos de datos (nombres compuestos, números positivos, presupuestos y tiempos no negativos).
   * **Carga Automática:** Módulo de simulación de datos (*mock data*) utilizando la librería `random` para pruebas rápidas de volumen de datos.
4. **Eliminar Piloto (Baja):** Algoritmo de búsqueda secuencial por número de monoplaza con confirmación de seguridad de doble paso antes de la eliminación física de la fila (método `pop`).
5. **Modificar Puntos o Tiempo Promedio:** Búsqueda del piloto por nombre o número de monoplaza mediante algoritmo de recorrido secuencial. Permite actualizar de forma independiente los puntos acumulados y/o el tiempo promedio por vuelta, con validación de rangos en cada campo y un submenú de edición que permanece activo hasta que el usuario decide volver al menú principal.
6. **Informe General y Visualización:**
   * **Algoritmo de Ordenamiento Doble:** Reordenamiento de la matriz mediante el método de la burbuja bajo un criterio de prioridad: de mayor a menor por puntos, y en caso de empate, de menor a mayor por tiempo promedio de vuelta.
   * **Interfaz Tabular:** Renderizado en consola con alineaciones estéticas de columnas (`<20`, `<18`, etc.) y formato de moneda para presupuestos.

---

## 🛠️ Estructura del Proyecto y Modularización

Para cumplir con las buenas prácticas de diseño de software, el código se encuentra estrictamente dividido en capas independientes:

```text
├── main.py        # Punto de entrada de la aplicación y ciclo de control del menú principal.
├── funciones.py   # Núcleo lógico: inicialización de matrices, validaciones, altas, bajas y ordenamiento.
└── README.md      # Documentación técnica del proyecto (Este archivo).
