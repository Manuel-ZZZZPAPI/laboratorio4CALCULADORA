from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import math, cmath, re

# Configurar ventana
Window.size = (360, 600)
Window.clearcolor = (0.1, 0.1, 0.1, 1)

class Calculadora(BoxLayout):

   def calcular(self):
    texto = self.ids.entry.text
    try:
    
        texto = texto.replace("^", "**")          
        texto = texto.replace(" ", "")
        texto = texto.replace(")(", ")*(")         

        import re
        texto = re.sub(r'√\(?([^\)]+)\)?', r'cmath.sqrt(\1)', texto)

      
        texto = re.sub(r'(?<!\d)j', '1j', texto)    
        texto = re.sub(r'(\d)j', r'\1*1j', texto)   
       
        import math, cmath
        resultado = eval(texto, {"__builtins__": None}, {"math": math, "cmath": cmath})

       
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
