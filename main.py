from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import math, cmath, re
from kivy.metrics import dp
from kivy.utils import platform

if platform != "android":
    Window.size = (dp(350), dp(550))
class Calculadora(BoxLayout):

   def calcular(self):
    texto = self.ids.entry.text
    try:
        # --- LIMPIEZA Y REEMPLAZOS ---
        texto = texto.replace("^", "")            # Potenciación
        texto = texto.replace(" ", "")
        texto = texto.replace(")(", ")*(")          # Multiplicación implícita

        # --- RAÍZ CUADRADA (soporta varios formatos) ---
        # Reemplazar √x por cmath.sqrt(x)
        import re
        texto = re.sub(r'√\(?([^\)]+)\)?', r'cmath.sqrt(\1)', texto)

        # --- COMPLEJOS ---
        # Reemplazar 'j' aislada por '1j'
        texto = re.sub(r'(?<!\d)j', '1j', texto)    # j → 1j
        texto = re.sub(r'(\d)j', r'\1*1j', texto)   # 3j → 3*1j

        # --- EVALUAR EXPRESIÓN ---
        import math, cmath
        resultado = eval(texto, {"_builtins_": None}, {"math": math, "cmath": cmath})

        # --- SIMPLIFICAR SALIDA ---
        if isinstance(resultado, complex):
            if abs(resultado.imag) < 1e-12:
                resultado = resultado.real
        if isinstance(resultado, float) and resultado.is_integer():
            resultado = int(resultado)

        self.ids.entry.text = str(resultado)

    except Exception as e:
        self.ids.entry.text = "Error"

class CalculadoraApp(App):
    def build(self):
        self.title = "Calculadora Avanzada"
        return Calculadora()

if __name__ == "__main__":
    CalculadoraApp().run()
