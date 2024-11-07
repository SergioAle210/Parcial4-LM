class TuringMachine:
    def __init__(
        self,
        tape,
        transitions,
        initial_state,
        accept_state,
        reject_state,
        blank_symbol="_",
    ):
        # Agrega "x" al inicio de la cinta para indicar el punto de inicio
        self.tape = list("x" + tape)
        self.head = 0  # Posición inicial del cabezal de lectura/escritura
        self.transitions = transitions
        self.current_state = initial_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.blank_symbol = (
            blank_symbol  # Símbolo en blanco para celdas fuera de los límites iniciales
        )

    def step(self):
        """Ejecuta un paso de la máquina de Turing y muestra el estado de la cinta."""
        if self.current_state in [self.accept_state, self.reject_state]:
            return False  # Termina si estamos en un estado de aceptación o rechazo

        # Lee el símbolo actual y busca la transición correspondiente
        symbol = self.tape[self.head]
        action = self.transitions.get((self.current_state, symbol))

        if action is None:
            self.current_state = self.reject_state
            return False  # Rechaza si no hay transición definida

        # Ejecuta la acción: escribe, mueve el cabezal, y cambia de estado
        new_symbol, direction, new_state = action
        self.tape[self.head] = new_symbol

        # Mostrar información detallada del paso
        print(
            f"\nEstado actual: {self.current_state}, Símbolo: '{symbol}' -> '{new_symbol}', Dirección: {direction}"
        )

        # Mover el cabezal a la derecha o izquierda, expandiendo la cinta si es necesario
        previous_head = self.head
        if direction == "R":
            self.head += 1
            if self.head >= len(self.tape):
                self.tape.append(self.blank_symbol)
        elif direction == "L":
            self.head -= 1
            if self.head < 0:
                self.tape.insert(0, self.blank_symbol)
                self.head = 0

        # Actualiza el estado de la máquina de Turing
        self.current_state = new_state

        # Mostrar el estado actual de la cinta y la posición del cabezal
        self.display_tape(previous_head, self.head)
        return True

    def display_tape(self, previous_head, current_head):
        """Imprime la cinta resaltando la posición actual del cabezal."""
        tape_str = "".join(self.tape)
        # Resaltar la posición del cabezal actual y movimiento con '[]'
        if previous_head < current_head:
            print(
                f"Cinta: {tape_str[:current_head]}[{tape_str[current_head]}]{tape_str[current_head+1:]} (moved right)"
            )
        elif previous_head > current_head:
            print(
                f"Cinta: {tape_str[:current_head]}[{tape_str[current_head]}]{tape_str[current_head+1:]} (moved left)"
            )
        else:
            print(
                f"Cinta: {tape_str[:current_head]}[{tape_str[current_head]}]{tape_str[current_head+1:]}"
            )

    def run(self):
        """Ejecuta la máquina de Turing hasta alcanzar un estado de aceptación o rechazo."""
        print("Estado inicial de la cinta:")
        self.display_tape(self.head, self.head)

        while self.step():
            pass
        print("\nResultado final:")
        self.display_tape(self.head, self.head)
        return self.current_state == self.accept_state


# Ejemplo de configuración para una máquina de Turing simple con desplazamiento a la derecha
tape = input("Por favor, ingrese la cadena a evaluar: ")
transitions = {
    ("q0", "0"): ("0", "R", "q0"),
    ("q0", "1"): ("1", "R", "q0"),
    ("q0", "x"): ("x", "R", "q0"),
    ("q0", "_"): ("_", "L", "q1"),
    ("q1", "_"): ("_", "L", "q1"),
    ("q1", "0"): ("_", "R", "q2"),
    ("q1", "1"): ("_", "R", "q3"),
    ("q2", "_"): ("0", "L", "q1"),
    ("q3", "_"): ("1", "L", "q1"),
    ("q1", "x"): ("_", "L", "q_accept"),  # Elimina la "x" al final del desplazamiento
}

tm = TuringMachine(
    tape=tape,
    transitions=transitions,
    initial_state="q0",
    accept_state="q_accept",
    reject_state="q_reject",
)

# Ejecución de la máquina
result = tm.run()
print("\nAccepted" if result else "Rejected")
