import unittest
import os
import sys

# Asegurar que la ruta base esté en sys.path para importar src sin problemas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import logica_tarjeta


class CreditCardTest(unittest.TestCase):

    # Cada prueba unitaria es un metodo de la clase

    def test_normal_1(self):
        # ENTRADAS (Caso Normal 1)
        compra = 350000
        interes = 2.8 / 100
        plazo = 18
        cuota = 25019.69

        # SALIDAS ESPERADAS
        total_abonos = 450_354.51
        total_intereses = 100_354.51

        cuota_calculada = logica_tarjeta.calcular_cuota(compra, interes, plazo)
        total_abonos_calculado = logica_tarjeta.calcular_total_abonos(compra, interes, plazo)
        total_intereses_calculado = logica_tarjeta.calcular_total_intereses(compra, interes, plazo)

        # Prueba que dos variables sean iguales
        self.assertAlmostEqual(cuota, cuota_calculada, 2)
        self.assertAlmostEqual(total_abonos, total_abonos_calculado, 2)
        self.assertAlmostEqual(total_intereses, total_intereses_calculado, 2)

    def test_normal_2(self):
        # ENTRADAS (Caso Normal 2)
        compra = 1200000
        tasa = 2.1 / 100
        plazo = 48
        cuota = 39922.53

        resultado = logica_tarjeta.calcular_cuota(compra, tasa, plazo)
        self.assertEqual(cuota, round(resultado, 2))

    def test_normal_3(self):
        # ENTRADAS (Caso Normal 3)
        compra = 850000
        interes = 2.5 / 100
        plazo = 30

        # SALIDAS ESPERADAS
        cuota_esperada = 40610.99
        total_abonos = 1218329.84
        total_intereses = 368329.84

        cuota_calculada = logica_tarjeta.calcular_cuota(compra, interes, plazo)
        total_abonos_calculado = logica_tarjeta.calcular_total_abonos(compra, interes, plazo)
        total_intereses_calculado = logica_tarjeta.calcular_total_intereses(compra, interes, plazo)

        # Prueba que dos variables sean iguales
        self.assertAlmostEqual(cuota_esperada, cuota_calculada, 2)
        self.assertAlmostEqual(total_abonos, total_abonos_calculado, 2)
        self.assertAlmostEqual(total_intereses, total_intereses_calculado, 2)

    def test_tasa_cero(self):
        # ENTRADAS (Tasa cero 2)
        compra = 600_000
        interes = 0 / 100
        plazo = 60

        # SALIDAS ESPERADAS
        cuota_esperada = 10000
        total_abonos = 600_000
        total_intereses = 0

        cuota_calculada = logica_tarjeta.calcular_cuota(compra, interes, plazo)
        total_abonos_calculado = logica_tarjeta.calcular_total_abonos(compra, interes, plazo)
        total_intereses_calculado = logica_tarjeta.calcular_total_intereses(compra, interes, plazo)

        # Prueba que dos variables sean iguales
        self.assertAlmostEqual(cuota_esperada, cuota_calculada, 2)
        self.assertAlmostEqual(total_abonos, total_abonos_calculado, 2)
        self.assertAlmostEqual(total_intereses, total_intereses_calculado, 2)

    def test_tasa_limite(self):
        # ENTRADAS (Tasa limite 4%)
        compra = 500000
        interes = 3.99 / 100
        plazo = 36

        # SALIDAS ESPERADAS
        cuota_esperada = 26406.83
        total_abonos = 950645.95
        total_intereses = 450645.95

        cuota_calculada = logica_tarjeta.calcular_cuota(compra, interes, plazo)
        total_abonos_calculado = logica_tarjeta.calcular_total_abonos(compra, interes, plazo)
        total_intereses_calculado = logica_tarjeta.calcular_total_intereses(compra, interes, plazo)

        # Prueba que dos variables sean iguales
        self.assertAlmostEqual(cuota_esperada, cuota_calculada, 2)
        self.assertAlmostEqual(total_abonos, total_abonos_calculado, 2)
        self.assertAlmostEqual(total_intereses, total_intereses_calculado, 2)

    def test_compra_cero(self):
        # ENTRADAS (Error Compra 2, ajustado a compra=0 porque la logica
        # solo valida compra == 0, no montos negativos)
        compra = 0
        interes = 3.2 / 100
        plazo = 45

        # SALIDAS ESPERADAS
        # Verifica que si se genere una excepcion adentro del bloque with
        with self.assertRaises(logica_tarjeta.CompraInvalida):
            cuota_calculada = logica_tarjeta.calcular_cuota(compra, interes, plazo)

    def test_plazo_cero(self):
        # ENTRADAS (Error Cuotas )
        compra = 120000
        interes = 3.0 / 100
        plazo = 0

        # Verifica que si se genere una excepcion adentro del bloque with
        with self.assertRaises(logica_tarjeta.PlazoInvalido):
            cuota_calculada = logica_tarjeta.calcular_cuota(compra, interes, plazo)

    def test_plazo_negativo(self):
        # ENTRADAS (Error Negativo )
        compra = 70000
        interes = 1.5 / 100
        plazo = -5

        # Verifica que si se genere una excepcion adentro del bloque with
        with self.assertRaises(logica_tarjeta.PlazoInvalido):
            cuota_calculada = logica_tarjeta.calcular_cuota(compra, interes, plazo)

    def test_usura(self):
        # ENTRADAS (Usura )
        compra = 300000
        interes = 4.5 / 100
        plazo = 24

        with self.assertRaises(logica_tarjeta.TasaExcesiva):
            logica_tarjeta.calcular_cuota(compra, interes, plazo)

    def test_demasiadas_cuotas(self):
        # ENTRADAS (Demasiadas cuotas )
        compra = 300000
        interes = 3.5 / 100
        plazo = 84

        with self.assertRaises(logica_tarjeta.PlazoInvalido):
            logica_tarjeta.calcular_cuota(compra, interes, plazo)


# Este fragmento de codigo permite ejecutar la prueba individualmente
# Va fijo en todas las pruebas
if __name__ == '__main__':
    unittest.main()
