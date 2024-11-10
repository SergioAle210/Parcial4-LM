import os
from colorama import init, Fore, Style

# Inicializa colorama para Windows
init(autoreset=True)


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
        self.tape = list(tape)  # Cinta de entrada
        self.head = 0  # Posición inicial del cabezal de lectura/escritura
        self.transitions = transitions  # Tabla de transiciones
        self.current_state = initial_state  # Estado inicial
        self.accept_state = accept_state  # Estado de aceptación
        self.reject_state = reject_state  # Estado de rechazo
        self.blank_symbol = blank_symbol  # Símbolo en blanco

    def step(self):
        """Ejecuta un paso de la máquina de Turing y muestra el estado de la cinta."""
        if self.current_state in [self.accept_state, self.reject_state]:
            return False  # Termina si alcanzamos un estado de aceptación o rechazo

        # Leer el símbolo actual y obtener la transición
        symbol = (
            self.tape[self.head] if self.head < len(self.tape) else self.blank_symbol
        )
        action = self.transitions.get((self.current_state, symbol))

        if action is None:
            self.current_state = self.reject_state
            return False

        # Ejecutar la transición
        new_symbol, direction, new_state = action
        self.tape[self.head] = new_symbol

        # Movimiento del cabezal
        if direction == "R":
            self.head += 1
            if self.head >= len(self.tape):
                self.tape.append(self.blank_symbol)
        elif direction == "L":
            self.head -= 1
            if self.head < 0:
                self.tape.insert(0, self.blank_symbol)
                self.head = 0

        # Actualizar el estado
        self.current_state = new_state
        return True

    def display_tape(self):
        """Imprime la cinta mostrando el estado actual en la posición del cabezal."""
        tape_with_state = [
            (
                f"{Fore.BLUE}{self.current_state}{Style.RESET_ALL}"
                if i == self.head
                else char
            )
            for i, char in enumerate(self.tape)
        ]
        return " ".join(map(str, tape_with_state))

    def run(self, output_file=None, step_limit=100):
        """Ejecuta la máquina hasta alcanzar un estado de aceptación, rechazo o límite de pasos y guarda en archivo."""
        output_lines = [
            f"{Fore.CYAN}Estado inicial de la cinta:{Style.RESET_ALL}\n{self.display_tape()}"
        ]

        step_count = 0
        while self.step() and step_count < step_limit:
            output_lines.append(self.display_tape())
            step_count += 1

        # Resultado final según el estado
        if self.current_state == self.accept_state:
            result = f"{Fore.GREEN}Accepted{Style.RESET_ALL}"
        elif self.current_state == self.reject_state:
            result = f"{Fore.RED}Rejected{Style.RESET_ALL}"
        else:
            result = f"{Fore.YELLOW}Ciclo Infinito (Límite de pasos alcanzado){Style.RESET_ALL}"

        output_lines.append(f"\nResultado: {result}")

        # Imprimir en la terminal y guardar en archivo si se especifica
        if output_file:
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            with open(output_file, "w") as file:
                clean_output = [
                    line.replace(Fore.BLUE, "")
                    .replace(Style.RESET_ALL, "")
                    .replace(Fore.GREEN, "")
                    .replace(Fore.RED, "")
                    .replace(Fore.YELLOW, "")
                    .replace(Fore.CYAN, "")
                    for line in output_lines
                ]
                file.write("\n".join(clean_output) + "\n")
            print(
                f"{Fore.YELLOW}Archivo de salida guardado en '{output_file}'.{Style.RESET_ALL}"
            )
        print("\n".join(output_lines))
        return self.current_state == self.accept_state


def save_input_to_file(directory, filename, tape):
    """Guarda una cadena de entrada en un archivo de texto."""
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, filename), "w") as file:
        file.write(tape)
    print(
        f"{Fore.YELLOW}Archivo de entrada guardado en '{directory}/{filename}'.{Style.RESET_ALL}"
    )


def run_predefined_test(
    input_string,
    output_dir,
    input_filename,
    output_filename,
    transitions,
    initial_state,
    accept_state,
    reject_state,
):
    """Ejecuta una prueba predefinida y crea el archivo de entrada y salida en el directorio especificado."""
    # Crear el archivo de entrada con el nombre especificado
    save_input_to_file(output_dir, input_filename, input_string)

    # Ejecutar la máquina de Turing y guardar el resultado en el archivo de salida
    output_file = os.path.join(output_dir, output_filename)
    tm = TuringMachine(
        input_string, transitions, initial_state, accept_state, reject_state
    )
    tm.run(output_file)


def show_machine_description():
    print(f"{Fore.CYAN}\n--- Descripción de la Máquina de Turing ---{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Lenguaje aceptado (L(M)):{Style.RESET_ALL}")
    print("L(M) = { x ∈ {a, b}* | x contiene la subcadena 'aba' }\n")

    print(f"{Fore.YELLOW}Componentes de la Máquina de Turing (M):{Style.RESET_ALL}")
    print(
        f"{Fore.CYAN}Q{Style.RESET_ALL} = {{q0, q1, q2, qaccept, qreject}}  # Conjunto de estados"
    )
    print(f"{Fore.CYAN}Alfabeto{Style.RESET_ALL} = {{a, b}}  # Alfabeto de entrada")
    print(
        f"{Fore.CYAN}Tau (Σ){Style.RESET_ALL} = {{a, b, _}}  # Alfabeto de la cinta, con símbolo de blanco '_'\n"
    )

    print(f"{Fore.YELLOW}Función de Transición (S):{Style.RESET_ALL}")
    print(
        """
        S(q0, a) = (a, R, q1)
        S(q0, b) = (b, R, q0)
        S(q0, _) = (_, R, qreject)
        S(q1, a) = (a, R, q1)
        S(q1, b) = (b, R, q2)
        S(q1, _) = (_, R, qreject)
        S(q2, b) = (b, R, q0)
        S(q2, a) = (a, R, qaccept)
        S(q2, _) = (_, R, qreject)
    """
    )
    print(f"{Fore.YELLOW}q0{Style.RESET_ALL} = Estado inicial")
    print(f"{Fore.YELLOW}qaccept{Style.RESET_ALL} = Estado de aceptación")
    print(f"{Fore.YELLOW}qreject{Style.RESET_ALL} = Estado de rechazo\n")


def main_menu():
    """Menú principal para ejecutar la máquina de Turing con opciones predefinidas o ingresadas por el usuario."""
    transitions = {
        ("q0", "a"): ("a", "R", "q1"),
        ("q0", "b"): ("b", "R", "q0"),
        ("q0", "_"): ("_", "R", "qreject"),
        ("q1", "a"): ("a", "R", "q1"),
        ("q1", "b"): ("b", "R", "q2"),
        ("q1", "_"): ("_", "R", "qreject"),
        ("q2", "b"): ("b", "R", "q0"),
        ("q2", "a"): ("a", "R", "qaccept"),
        ("q2", "_"): ("_", "R", "qreject"),
    }
    initial_state = "q0"
    accept_state = "qaccept"
    reject_state = "qreject"

    while True:
        print(f"{Fore.MAGENTA}\n--- Menú de la Máquina de Turing ---{Style.RESET_ALL}")
        print("1. Ver descripción del lenguaje aceptado y máquina de Turing")
        print("2. Ingresar una cadena manualmente")
        print("3. Ejecutar cadena de prueba 'accept_input'")
        print("4. Ejecutar cadena de prueba 'reject_input'")
        print("5. Ejecutar cadena de prueba 'infinite_input'")
        print("6. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            show_machine_description()

        elif choice == "2":
            user_input = input("Por favor, ingrese la cadena a evaluar: ")
            print(
                f"{Fore.MAGENTA}\n--- Resultado para la cadena ingresada ---{Style.RESET_ALL}"
            )
            tm = TuringMachine(
                user_input, transitions, initial_state, accept_state, reject_state
            )
            tm.run()

        elif choice == "3":
            print(
                f"{Fore.MAGENTA}\n--- Resultado de 'accept_input' ---{Style.RESET_ALL}"
            )
            run_predefined_test(
                "aabaaaaaaaaaaba",
                "accept",
                "turing_accept_input.txt",
                "turing_accept_output.txt",
                transitions,
                initial_state,
                accept_state,
                reject_state,
            )

        elif choice == "4":
            print(
                f"{Fore.MAGENTA}\n--- Resultado de 'reject_input' ---{Style.RESET_ALL}"
            )
            run_predefined_test(
                "abbbaaaaaaa",
                "reject",
                "turing_reject_input.txt",
                "turing_reject_output.txt",
                transitions,
                initial_state,
                accept_state,
                reject_state,
            )

        elif choice == "5":
            print(
                f"{Fore.MAGENTA}\n--- Resultado de 'infinite_input' ---{Style.RESET_ALL}"
            )
            run_predefined_test(
                "aaaaaaa",
                "infinite",
                "turing_infinite_input.txt",
                "turing_infinite_output.txt",
                transitions,
                initial_state,
                accept_state,
                reject_state,
            )

        elif choice == "6":
            print(
                f"{Fore.GREEN}Gracias por usar la Máquina de Turing. ¡Hasta luego!{Style.RESET_ALL}"
            )
            break

        else:
            print(f"{Fore.RED}Opción no válida. Intente nuevamente.{Style.RESET_ALL}")


if __name__ == "__main__":
    main_menu()
