import tkinter as tk
class conversorapp:
    def  __float__(self, root):
        self.root = root
        self.root.title("Conversor de Grados")
        
        self.label_titulo = tk.Label(root, text="Conversión de grados")
        self.label_titulo.pack()
        
        self.label_cantidad = tk.Label(root, text="Ingrese la cantidad de grados en celcius" )
        self.label_cantidad.pack()
        self.entry_monto = tk.Entry(root)
        self.entry_monto.pack()
        
        self.label_monto = tk.Label(root, text="Fahrenheit:")
        self.label_monto.pack()
        
        self.label_resultado = tk.Label(root, text="")
        self.label_resultado.pack()
        
        self.boton_convertir = tk.Button(root, text="Convertir", command=self.realizar_conversion)
        self.boton_convertir.pack()
    def realizar_conversion(self):
        celcius= self.label_cantidad.get()
        fahrenhei = self.label_resultado
        fahrenheit = celcius * 9/5 + 32
        
        self.verif.config (text = fahrenheit)
       
root = tk.Tk()
app = conversorapp(root)
root.mainloop()        

    
        
        
        