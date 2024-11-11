import unittest
from turing_machine import (
    TuringMachine,
    load_machine_config,
)  # Asegúrate de que tu código principal esté en un archivo llamado turing_machine.py


class TestTuringMachine(unittest.TestCase):

    def setUp(self):
        """Carga la configuración de la máquina de Turing desde el archivo JSON antes de cada prueba."""
        (
            self.initial_state,
            self.accept_state,
            self.reject_state,
            self.blank_symbol,
            self.transitions,
        ) = load_machine_config("turing_config.json")

    def test_accept_input(self):
        """Prueba una cadena que debería ser aceptada."""
        tape = "aabaa"
        tm = TuringMachine(
            tape,
            self.transitions,
            self.initial_state,
            self.accept_state,
            self.reject_state,
        )
        result = tm.run()
        self.assertTrue(result, "La máquina debería aceptar la cadena 'aabaa'.")

    def test_reject_input(self):
        """Prueba una cadena que debería ser rechazada."""
        tape = " "
        tm = TuringMachine(
            tape,
            self.transitions,
            self.initial_state,
            self.accept_state,
            self.reject_state,
        )
        result = tm.run()
        self.assertFalse(
            result, "La máquina debería rechazar la cadena 'bbbbbbbbbbbbbbba'."
        )

    def test_infinite_loop_input(self):
        """Prueba una cadena que debería causar un ciclo infinito."""
        tape = "abbb"
        tm = TuringMachine(
            tape,
            self.transitions,
            self.initial_state,
            self.accept_state,
            self.reject_state,
        )
        result = tm.run(step_limit=100)  # Establece un límite de pasos
        self.assertFalse(
            result,
            "La máquina debería entrar en un ciclo infinito para la cadena 'abbb'.",
        )
        self.assertEqual(
            tm.current_state,
            "qloop",
            "La máquina debería estar en el estado 'qloop' al finalizar.",
        )


if __name__ == "__main__":
    unittest.main()
