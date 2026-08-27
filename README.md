# 💳 Calculadora de Cuota de Tarjeta de Crédito

Una pequeña aplicación en Python que calcula cuánto se debe pagar cada mes al diferir una compra con tarjeta de crédito, y cuánto termina costando esa compra en intereses.

## ✍️ Autor

**Pedro Hernandez**

---

## 📁 Estructura del Proyecto

El proyecto está organizado de manera modular siguiendo las buenas prácticas de Python:

```text
Tarjeta-de-credito/
├── src/
│   ├── __init__.py
│   ├── logica_tarjeta.py       # Lógica de cálculo y excepciones del negocio
│   └── consola_tarjeta.py      # Interfaz de usuario por consola
├── tests/
│   ├── __init__.py
│   └── test_tarjeta.py         # Suite de pruebas unitarias (unittest)
├── docs/
│   └── Casos_de_prueba_tarjeta_de_credito.xlsx # Matriz de casos de prueba
├── main.py                     # Punto de entrada principal
├── README.md                   # Documentación del proyecto
└── .gitignore
```

---

## 🧾 ¿Qué hace esta aplicación?

Cuando compras algo y decides pagarlo "a cuotas" con tu tarjeta de crédito, el banco te cobra un interés por ese plazo. Esta aplicación simula exactamente ese cálculo: le das los datos de la compra y te dice cuánto pagarás cada mes y cuánto terminarás pagando en total.

Está pensada como una herramienta educativa, con su lógica separada en tres partes:

| Carpeta / Archivo | ¿Para qué sirve? |
|---|---|
| `src/logica_tarjeta.py` | El "cerebro" — hace todos los cálculos y valida reglas de negocio |
| `src/consola_tarjeta.py` | La interfaz que interactúa con el usuario por consola |
| `tests/test_tarjeta.py` | Comprueba que los cálculos siempre den el resultado correcto |
| `docs/` | Contiene los casos de prueba de referencia en Excel |

---

## 📥 Datos de entrada

Para calcular la cuota, la aplicación te pide tres cosas:

1. **Monto de la compra** — cuánto vale lo que compraste
2. **Tasa de interés mensual** — el porcentaje que cobra la tarjeta cada mes (ej. `2.5` para 2.5%)
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

Desde la terminal, en la carpeta raíz del proyecto:

### 1. Ejecutar la aplicación
Puedes iniciar la aplicación usando el punto de entrada principal:
```bash
python main.py
```
O directamente como módulo:
```bash
python -m src.consola_tarjeta
```

Y solo tienes que responder las preguntas que te va haciendo (monto, tasa y plazo).

### 2. Ejecutar las pruebas unitarias
Para verificar que todos los casos de prueba sigan pasando correctamente:

```bash
python -m unittest discover tests -v
```
o también:
```bash
python -m unittest tests/test_tarjeta.py -v
```
