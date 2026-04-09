# 📦 Sistema de Gestión de Envíos con Lista Doblemente Enlazada

## Descripción

Este proyecto implementa un sistema básico de gestión de envíos utilizando una **lista doblemente enlazada** en Python. Donde soluciona un problema en una empresa de logistica para mejorar el control de envios en tiempo real.

Permite:

✅ Agregar un envío
🔍 Buscar un envío por código
❌ Eliminar un envío
📄 Mostrar envíos (orden normal)
🔄 Mostrar envíos en orden inverso

## ANALISIS DE LAS ESTRUCTURAS DE DATOS COMO SOLUCIÓN.

### ¿Porque utilizar lista doblemente enlazada ?

El sistema necesita :

 🔄 Recorrer envíos en ambos sentidos
 ➕ Agregar y eliminar fácilmente
 🔍 Buscar por código
 📦 Mantener orden dinámico

👉 la lista doblemente enlazada es ideal, porque:

 ✔️ Permite ir hacia adelante y hacia atrás
 ✔️ Facilita eliminar nodos sin recorrer desde el inicio
 ✔️ No depende de posiciones fijas (como arreglos)

## ⚡ Complejidad (Big O)

📊 Lista doblemente enlazada

| Operación | Complejidad |
|----------|------------|
| Agregar  | O(n)       |
| Buscar   | O(n)       |
| Eliminar | O(n)       |
| Recorrer | O(n)       |

## COMPARACIÓN DE ESTRUCTURA DE DATOS 

2. Lista doble vs tabla hash

| Característica | Lista doble       | Tabla hash        |
|---------------|--------------------|-------------------|
| Búsqueda      | 🔴 Lenta           | 🟢 Muy rápida     |
| Orden         | ✅ Mantiene orden  | ❌ No ordenado    |
| Recorrido     | ✅ Secuencial      | ❌ No natural     |
| Inserción     | 🟢 Fácil           | 🟢 Rápida         |
| Uso ideal     | Listas dinámicas   | Búsqueda rápida    |

### CONCLUSIÓN 

👉 La lista doblemente enlazada es mejor porque permite recorridos bidireccionales y facilita la eliminación de nodos, lo cual no es posible en una lista simplemente enlazada.

👉 Aunque la tabla hash tiene mejor complejidad O(1) en búsqueda, no mantiene orden ni permite recorridos secuenciales, por lo que no es adecuada para este sistema.

👉 La complejidad de la lista doblemente enlazada es O(n) en búsqueda, inserción y eliminación.

## PREGUNTAS DE REFLEXIÓN 

1.  ¿Cómo cambiaría la eficiencia del sistema si se utilizara otra estructura de 
datos diferente a la seleccionada?

Si se utilizara una lista simplemente enlazada, la eficiencia en inserción y búsqueda se mantendría, pero se perdería la capacidad de recorrer en ambos sentidos, lo que afecta directamente los requerimientos del sistema.
Por otro lado, si se utilizara una tabla hash, la búsqueda y eliminación mejorarían a O(1), pero se perdería el orden de los datos y la posibilidad de recorrerlos secuencialmente en ambos sentidos, lo que hace que no sea adecuada para este problema.
Por lo tanto, la lista doblemente enlazada ofrece el mejor balance entre eficiencia y funcionalidad.

2. ¿Qué limitaciones presenta la estructura elegida en escenarios de gran 
volumen de datos?
Las limitaciones son las siguientes :

👉 En escenarios de gran volumen de datos, la lista doblemente enlazada se ve limitada por su complejidad lineal O(n) en operaciones de búsqueda, inserción (en posición específica) y eliminación, ya que requiere recorridos secuenciales.

👉 Adicionalmente  el uso de dos punteros por nodo (anterior y siguiente) incrementa el consumo de memoria, afectando la escalabilidad.

👉 Finalmente, la ausencia de acceso directo por índice reduce el rendimiento frente a estructuras como las tablas hash, que ofrecen complejidad promedio O(1).



---

## ⚙️ Estructura del Código

🔹 Clase Nodo

Representa cada envío dentro de la lista.

### Atributos:

codigo: Identificador del envío
cliente: Nombre del cliente
estado: Estado del envío
siguiente: Apunta al siguiente nodo
anterior: Apunta al nodo anterior

🔹 Clase ListaDoble

### Gestiona la lista doblemente enlazada.

#### Métodos principales:

* agregar(): Inserta un nuevo envío al final
* buscar(): Busca un envío por código
* eliminar(): Elimina un envío específico
* mostrar(): Recorre la lista hacia adelante
* mostrar_inverso(): Recorre la lista hacia atrás

## 🔹 Función menu()

Permite la interacción con el usuario mediante consola.

#### Opciones disponibles:

* Agregar envío
* Buscar envío
* Eliminar envío
* Mostrar envíos
* Mostrar envíos inverso
* Salir

## ▶️ Cómo ejecutar

* Asegúrate de tener Python instalado
* Guarda el archivo como main.py
* Ejecuta en la terminal:
* python main.py

## 📝 Ejemplo de uso

--- SISTEMA DE ENVÍOS ---

1. Agregar envío
2. Buscar envío
3. Eliminar envío
4. Mostrar envíos
5. Mostrar envíos inverso
6. Salir
---

## 👨‍💻 Autor

* Angela Maria Medina 
* Gustavo Valencia 
* kevin 

