**Este repositorio contiene una colección completa de ejercicios de C#, organizados en módulos temáticos.**

## 01 - Fundamentos de Python

- Variables y Tipos de Datos

_Declaración de variables y comprensión de tipos primitivos y estructuras de datos._

- Control de Flujo

_Uso de instrucciones condicionales y bucles (if, elif, else, for, while)._

- Funciones

_Declaración y uso de funciones, incluyendo funciones lambda._

- Alcance (Scope)

_Cómo funcionan los ámbitos de variables._

- Cierres (Closures)

_Funciones que capturan el estado de su entorno._

- Contexto Self

_Cómo funciona el contexto de ejecución  Self._

- Manejo de errores y excepciones

_Captura y manejo de errores usando try, except, y finally._


## 02 - Programación Orientada a Objetos en Python

- Objetos y propiedades

_Creación y manipulación de objetos, así como el acceso a sus atributos._

- Herencia de clases y MRO (Method Resolution Order)

_Cómo funciona la herencia y el orden de resolución de métodos._

- Clases y sintaxis moderna

_Uso de clases con la sintaxis moderna de Python, métodos especiales y herencia._

- Encapsulación, herencia y polimorfismo

_Principios fundamentales de POO: encapsulamiento, herencia y polimorfismo._

- Funciones de fábrica

_Uso de funciones que retornan instancias de objetos de manera flexible._

- Composición de objetos

_Construcción de objetos complejos a partir de otros más simples, en lugar de herencia._


## 03 - Programación Funcional en Python

- Funciones puras

_Funciones que, dado un mismo conjunto de entradas, siempre devuelven la misma salida sin producir efectos secundarios._

- Inmutabilidad

_Principio de no modificar directamente los datos existentes, sino crear nuevas estructuras de datos._

- Funciones de orden superior

_Funciones que aceptan otras funciones como argumentos o las retornan como resultados._

- Currying

_Transformación de una función que toma múltiples argumentos en una serie de funciones que toman un solo argumento._

- Composición de funciones

_Técnica que permite encadenar funciones pequeñas en una sola función compleja._

- Funciones y categorías

_Estructuras que permiten mapear funciones sobre valores envueltos o estructurados._

- Monads

_Patrón que permite encadenar operaciones, manejando contextos como errores o valores nulos._

- Lenses

_Herramientas para acceder y modificar estructuras de datos inmutables de forma segura._

- Transductores

_Funciones que transforman otras funciones de transformación, permitiendo operaciones eficientes sobre estructuras de datos._


## 04 - Estructuras de Datos y Algoritmos en Python

- Arrays, Objects, Sets, y Maps

_Uso de estructuras de datos como listas, diccionarios, sets y su manipulación._

- Stacks y Queues

_Estructuras de datos lineales que permiten inserción y eliminación en un orden específico (LIFO y FIFO)._

- Listas enlazadas

_Estructura donde cada nodo apunta al siguiente, permitiendo inserciones y eliminaciones eficientes._

- Recursion

_Uso de la recursión para resolver problemas complejos de forma más elegante._

- Operaciones de matriz (map, filter, reduce)

_Uso de funciones de orden superior para transformar, filtrar y reducir listas._

- Algoritmos de ordenamiento

_Implementación de algoritmos de ordenamiento como bubble sort, quicksort y merge sort._

- Algoritmos de búsqueda

_Algoritmos de búsqueda como búsqueda lineal y binaria para encontrar elementos._

- Tipos de datos abstractos

_Tipos abstractos como pilas, colas y listas, definiendo operaciones sin especificar implementación concreta._


## 05 - Programación Asíncrona en Python

- Callbacks

_Funciones que se ejecutan después de completar una operación asíncrona, permitiendo la continuación de un flujo de ejecución._

- Promesas

_Objeto que representa la terminación o el fracaso eventual de una operación asíncrona._

- Async/Await

_Sintaxis que simplifica el manejo de operaciones asíncronas, haciendo el código más legible y mantenible._

- Manejo de errores asincrónicos

_Manejo de errores en operaciones asíncronas utilizando bloques try, except y finally._

- Bucle de eventos

_Mecanismo que permite que Python maneje múltiples operaciones asíncronas a través de un bucle de eventos._

- Ciclo de vida de la promesa

_Etapas de una promesa en JavaScript: pendiente, cumplida o rechazada. En Python, se maneja mediante Future y estados de la tarea._


## 06 - Buenas Prácticas de Código en Python

- Código legible

_Escribir código limpio y entendible siguiendo convenciones como PEP8._

- Comentarios útiles

_Escribir comentarios que expliquen el por qué de una decisión, no lo obvio._

- Nombres descriptivos

_Usar nombres significativos que indiquen claramente el propósito de una variable o función._

- Modularidad

_Dividir el código en funciones pequeñas con responsabilidades bien definidas._

- Evitar duplicación

_Aplicar el principio DRY (Don't Repeat Yourself)._


## 07 - Patrones de Diseño en Python

- Patrón Singleton

_Asegurar que una clase tenga una única instancia y proporcionar un punto global de acceso a ella._

- Patrón de fábrica

_Crear objetos sin especificar la clase exacta del objeto que se va a crear._

- Patrón de observador

_Permitir a un objeto notificar a otros cuando cambia su estado._

- Patrón de estrategia

_Permitir cambiar el comportamiento de un objeto en tiempo de ejecución._

- Patrón de adaptador

_Convertir la interfaz de una clase en otra esperada por el cliente._

- Patrón decorador

_Agregar funcionalidad a objetos dinámicamente sin modificar su estructura._

- Patrón de comando

_Encapsular una petición como un objeto, permitiendo parametrizar clientes._

- Patrón de proxy

_Proveer un sustituto para controlar el acceso a otro objeto._

- Patrón de constructor

_Separar la construcción de un objeto complejo de su representación._

- Método de plantilla

_Definir el esqueleto de un algoritmo, delegando pasos a subclases._


## 08 - Principios SOLID en Python

- Principio de Responsabilidad Única (PRU)

_Una clase debe tener una única razón para cambiar._

- Principio de Abierto/Cerrado (OCP)

_Las entidades deben estar abiertas para extensión, pero cerradas para modificación._

- Principio de sustitución de Liskov (LSP)

_Las subclases deben poder reemplazar a sus superclases sin alterar el funcionamiento esperado._

- Principio de segregación de interfaces (ISP)

_Los clientes no deben depender de interfaces que no utilizan._

- Principio de inversión de dependencia (DIP)

_Los módulos de alto nivel no deben depender de los de bajo nivel, ambos deben depender de abstracciones._


## 09 - Testing en Python

- Pruebas unitarias con unittest (función pura)

_Probar funciones puras con casos simples y repetibles._

- Pruebas de clase con unittest (configuración/desmontaje)

_Preparar y limpiar el estado antes y después de cada test._

- Pruebas parametrizadas con pytest

_Reducir repetición usando @pytest.mark.parametrize._

- Mocking de dependencias externas (unittest.mock)

_Aislar el código de IO/red con patch y objetos simulados._

- Accesorios en pytest

_Reutilizar preparación de estado con fixtures._

- TDD mini–kata (FizzBuzz)

_Escribir tests primero, luego la implementación mínima._