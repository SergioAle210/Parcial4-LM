import unittest
from turing_machine import (
    TuringMachine,
)  # Asegúrate de que tu código principal esté en un archivo llamado turing_machine.py


class TestTuringMachine(unittest.TestCase):

    def setUp(self):
        """Configura las transiciones y estados antes de cada prueba."""
        self.transitions = {
            ("q0", "a"): ("a", "R", "q1"),
            ("q0", "b"): ("b", "R", "qloop"),
            ("q0", "_"): ("_", "R", "qreject"),
            ("q1", "a"): ("a", "R", "q1"),
            ("q1", "b"): ("b", "R", "q2"),
            ("q1", "_"): ("_", "R", "qreject"),
            ("q2", "a"): ("a", "R", "qaccept"),
            ("q2", "b"): ("b", "R", "qloop"),
            ("q2", "_"): ("_", "R", "qloop"),
            ("qloop", "a"): ("a", "R", "q1"),
            ("qloop", "b"): ("b", "R", "qloop"),
            ("qloop", "_"): ("_", "R", "qloop"),
        }
        self.initial_state = "q0"
        self.accept_state = "qaccept"
        self.reject_state = "qreject"

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
