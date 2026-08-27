class CompraInvalida(Exception):
    """Se lanza cuando el monto de la compra es inválido."""


class PlazoInvalido(Exception):
    """Se lanza cuando el plazo es inválido."""


class TasaExcesiva(Exception):
    """Se lanza cuando la tasa de interés supera el límite permitido."""


def calcular_cuota(compra, interes, plazo):
    if compra == 0:
        raise CompraInvalida("La compra debe ser mayor a cero")
    if plazo <= 0:
        raise PlazoInvalido("El plazo debe ser mayor a cero")
    if plazo > 60:
        raise PlazoInvalido("El plazo no puede superar 60 cuotas")
    if interes > 0.04:
        raise TasaExcesiva("La tasa de interés supera el límite permitido")

    if interes == 0:
        return round(compra / plazo, 2)

    cuota_exacta = compra * interes / (1 - (1 + interes) ** (-plazo))
    return round(cuota_exacta, 2)


def calcular_total_abonos(compra, interes, plazo):
    cuota_exacta = calcular_cuota_exacta(compra, interes, plazo)
    return round(cuota_exacta * plazo, 2)


def calcular_total_intereses(compra, interes, plazo):
    total_abonos = calcular_total_abonos(compra, interes, plazo)
    return round(total_abonos - compra, 2)


def calcular_cuota_exacta(compra, interes, plazo):
    if compra == 0:
        raise CompraInvalida("La compra debe ser mayor a cero")
    if plazo <= 0:
        raise PlazoInvalido("El plazo debe ser mayor a cero")
    if plazo > 60:
        raise PlazoInvalido("El plazo no puede superar 60 cuotas")
    if interes > 0.04:
        raise TasaExcesiva("La tasa de interés supera el límite permitido")

    if interes == 0:
        return compra / plazo

    return compra * interes / (1 - (1 + interes) ** (-plazo))
