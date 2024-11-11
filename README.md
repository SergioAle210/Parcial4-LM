#### Directorio Principal

- **turing_machine.py**:

  - Archivo principal del programa que implementa la lógica de la Máquina de Turing, la interacción con el usuario y las opciones del menú. Contiene la clase principal de la Máquina de Turing, funciones para crear archivos de entrada/salida y el menú principal para seleccionar diferentes operaciones.
  - Componentes principales:
    - **Clase TuringMachine**: Implementa la lógica de la Máquina de Turing, incluyendo los métodos `step`, `display_tape` y `run`.
    - **Función save_input_to_file**: Guarda las cadenas de entrada de prueba en archivos.
    - **Función run_predefined_test**: Ejecuta pruebas predefinidas con una entrada específica, guardando el resultado en un archivo de salida.
    - **Función show_machine_description**: Muestra los detalles de la Máquina de Turing, incluyendo el lenguaje aceptado y las funciones de transición.
    - **Función main_menu**: Proporciona una interfaz de menú para la interacción con el usuario, permitiéndole elegir diferentes opciones, como ejecutar entradas predefinidas o cadenas personalizadas.

- **test_turing_machine.py**:

  - Contiene pruebas unitarias para la Máquina de Turing. Importa la clase `TuringMachine` y realiza pruebas con varias entradas para verificar si son aceptadas, rechazadas o entran en un bucle infinito. Cada prueba valida un comportamiento específico de la Máquina de Turing.
  - Incluye pruebas para:
    - Aceptación de entradas válidas.
    - Rechazo de entradas inválidas.
    - Detección de bucles infinitos.

- **.gitignore**:
  - Especifica los archivos y directorios que no deben ser rastreados por Git, como archivos temporales o de salida compilada.

#### Estructura de Directorios

- **accept**:

  - **turing_accept_input.txt**: Almacena la entrada predefinida para un caso "aceptado", diseñado para ser aceptado por la Máquina de Turing.
  - **turing_accept_output.txt**: Contiene la salida y el estado final de la Máquina de Turing para la entrada "aceptada".

- **reject**:

  - **turing_reject_input.txt**: Almacena la entrada predefinida para un caso "rechazado", que debe ser rechazado por la Máquina de Turing.
  - **turing_reject_output.txt**: Contiene la salida y el estado final de la Máquina de Turing para la entrada "rechazada".

- **infinite**:
  - **turing_infinite_input.txt**: Almacena la entrada predefinida que causa que la Máquina de Turing entre en un bucle infinito.
  - **turing_infinite_output.txt**: Contiene la salida de la Máquina de Turing hasta que alcanza el límite de pasos, indicando un ciclo infinito, seguido de "Rejected" como resultado final.

#### Estructura del Código y Funciones

1. **Clase TuringMachine**:

   - `__init__`: Inicializa la Máquina de Turing con la cinta, las transiciones y los estados.
   - `step`: Ejecuta un paso de la máquina según el estado y símbolo actual, actualizando la cinta y la posición del cabezal.
   - `display_tape`: Muestra la cinta con el estado actual y la posición del cabezal.
   - `run`: Ejecuta la máquina con un límite de pasos, deteniéndose si alcanza un estado de aceptación/rechazo o el límite.

2. **Funciones Utilitarias**:

   - `save_input_to_file`: Guarda la cinta de entrada para cada caso de prueba en un archivo de texto.
   - `run_predefined_test`: Combina el guardado de archivo de entrada y la ejecución de la Máquina de Turing, almacenando los resultados en un archivo de salida.
   - `show_machine_description`: Proporciona información detallada sobre el lenguaje aceptado y la estructura de la Máquina de Turing.

3. **Menú e Interacción con el Usuario**:
   - La función `main_menu` presenta opciones para que el usuario vea los detalles de la máquina, ingrese una cadena personalizada o ejecute casos de prueba predefinidos.
