# 💳 Calculadora de Cuota de Tarjeta de Crédito

Una pequeña aplicación en Python que calcula cuánto se debe pagar cada mes al diferir una compra con tarjeta de crédito, y cuánto termina costando esa compra en intereses.

## ✍️ Autor

**Pedro Hernandez**

---

## 🧾 ¿Qué hace esta aplicación?

Cuando compras algo y decides pagarlo "a cuotas" con tu tarjeta de crédito, el banco te cobra un interés por ese plazo. Esta aplicación simula exactamente ese cálculo: le das los datos de la compra y te dice cuánto pagarás cada mes y cuánto terminarás pagando en total.

Está pensada como una herramienta educativa, con su lógica separada en tres partes:

| Archivo | ¿Para qué sirve? |
|---|---|
| `logica_tarjeta.py` | El "cerebro" — hace todos los cálculos |
| `consola_tarjeta.py` | La parte que conversa contigo por consola |
| `test_tarjeta.py` | Comprueba que los cálculos siempre den el resultado correcto |

---

## 📥 Datos de entrada

Para calcular la cuota, la aplicación te pide tres cosas:

1. **Monto de la compra** — cuánto vale lo que compraste
2. **Tasa de interés mensual** — el porcentaje que cobra la tarjeta cada mes
3. **Plazo (número de cuotas)** — en cuántos meses quieres pagarlo

---

## 📤 ¿Cómo se convierten en salidas?

Con esos tres datos, la aplicación calcula:

- 💰 **Cuota mensual** — lo que pagarás cada mes
- 📊 **Total de abonos** — la suma de todas las cuotas que vas a pagar
- 📈 **Total de intereses** — cuánto de más pagaste, solo por financiar la compra

En pocas palabras: entre más alta sea la tasa o más largo el plazo, más intereses terminas pagando — aunque la cuota mensual sea más pequeña. La aplicación hace justo esa cuenta, para que sepas de antemano qué tan conveniente es diferir una compra.

Hay un par de casos especiales que la aplicación reconoce:

- Si la **tasa es 0%**, simplemente divide el monto entre el número de cuotas (sin cobrar nada extra).
- Si la **tasa supera el 4% mensual**, la aplicación no calcula nada y te avisa que ese interés supera el límite legal permitido (la tasa de usura).
- Si el **monto de la compra es cero** o el **plazo es menor a un mes**, también te avisa que esos datos no son válidos.

---

## ▶️ Cómo usarla

Desde la terminal, en la carpeta del proyecto:

```
python consola_tarjeta.py
```

Y solo tienes que responder las preguntas que te va haciendo (monto, tasa y plazo).

Si quieres verificar que todo esté funcionando correctamente:

```
python -m unittest test_tarjeta.py -v
```
