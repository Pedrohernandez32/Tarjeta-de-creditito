# Tarjeta de crédito

## Autor
Pedro Hernández (@Pedrohernandez32)

## Qué es este proyecto
Un proyecto simple hecho para aprender: recibe datos de una tarjeta y de una compra, revisa que estén bien y devuelve si la compra se aprueba o no.

## Cómo funciona (en palabras sencillas)
1. Llega la información: número de tarjeta, vencimiento, CVV, nombre y monto.
2. Se revisa rápido: que no falte nada y que la fecha no esté vencida.
3. Se protege la tarjeta: no se muestra el número completo, se oculta la mayoría.
4. Se decide si la compra pasa o no (aprobada / denegada / pendiente).
5. Se devuelve una respuesta simple con el estado y datos que no sean sensibles.

## Cómo convierte datos de entrada en salida

Ejemplo de entrada (muy simple):
{ "card_number": "4111111111111111", "expiry": "2027-08", "cvv": "123", "amount": 125.5 }

Transformación paso a paso:
- Quitar espacios y arreglar formatos.
- Revisar fecha de vencimiento.
- Ocultar partes del número para no mostrar todo.
- Aplicar reglas básicas y decidir resultado.

Ejemplo de salida:
{ "status": "approved", "amount": 125.5, "masked_card": "4111 **** **** 1111", "message": "Aprobada" }

## Notas
- Es un ejemplo para aprender; no usar en producción sin más mejoras.
- No se deben guardar datos sensibles como el CVV.

## Contacto
https://github.com/Pedrohernandez32/Tarjeta-de-creditito
