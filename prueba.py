import customtkinter as ctk

# Configuración de la apariencia
ctk.set_appearance_mode("dark")  # Modos: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Temas: "blue" (standard), "green", "dark-blue"

class MiApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurar ventana
        self.title("Mi primera App")
        self.geometry("400x300")

        # Agregar un texto (Label)
        self.label = ctk.CTkLabel(self, text="¡Python GUI funcionando!", font=("Roboto", 20))
        self.label.pack(pady=40)

        # Agregar un botón
        self.boton = ctk.CTkButton(self, text="Púlsame", hover_color="purple", command=self.accion_boton)
        self.boton.pack(pady=20)

    def accion_boton(self):
        self.label.configure(text="¡Genial, hiciste clic!")
        print("Botón presionado correctamente")

if __name__ == "__main__":
    app = MiApp()
    app.mainloop()