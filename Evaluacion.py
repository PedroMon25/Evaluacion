import tkinter as tk
import random
from tkinter import messagebox


class JuegoConquista:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Conquista de Territorios")
        self.root.geometry("500x500")

        # Variables de juego
        self.vidas = 5
        self.puntaje = 0
        self.faccion = None
        self.ronda = 0
        self.decisiones_base = {
            "Facción A - Imperio del Sol": ["Atacar", "Defender", "Diplomacia", "Fortificar", "Reclutar tropas",
                                            "Enviar espías"],
            "Facción B - Reino de la Noche": ["Infiltrar", "Aliarse", "Reforzar", "Realizar emboscada",
                                              "Tratar con el enemigo", "Sabotear suministros"],
            "Facción C - Hordas del Caos": ["Explorar", "Saqueo", "Espionaje", "Destruir aldeas",
                                            "Reclutar mercenarios", "Conquistar territorio"]
        }

        # Pantalla inicial
        self.pantalla_inicial()

    def pantalla_inicial(self):
        self.frame_inicial = tk.Frame(self.root, bg="lightblue")
        self.frame_inicial.pack(fill="both", expand=True)

        titulo = tk.Label(self.frame_inicial, text="Conquista de Territorios", font=("Arial", 24), bg="lightblue")
        titulo.pack(pady=20)

        # Añadir el texto de bienvenida como párrafo
        descripcion = tk.Label(self.frame_inicial, text=(
            "Bienvenido a Conquista de Territorios. Escoge tu facción y toma las mejores decisiones "
            "para tu gente mientras expandes tus tierras, te deseo la mayor de las suertes."
        ), wraplength=400, bg="lightblue", font=("Arial", 12), justify="center")
        descripcion.pack(pady=10)

        boton_jugar = tk.Button(self.frame_inicial, text="Jugar", font=("Arial", 16), command=self.iniciar_juego)
        boton_jugar.pack(pady=20)

        boton_instrucciones = tk.Button(self.frame_inicial, text="Instrucciones", font=("Arial", 16),
                                        command=self.mostrar_instrucciones)
        boton_instrucciones.pack(pady=10)

    def mostrar_instrucciones(self):
        # Ocultar el menú inicial y mostrar las instrucciones
        self.frame_inicial.pack_forget()

        self.frame_instrucciones = tk.Frame(self.root, bg="lightgray")
        self.frame_instrucciones.pack(fill="both", expand=True)

        titulo_instrucciones = tk.Label(self.frame_instrucciones, text="Instrucciones", font=("Arial", 20),
                                        bg="lightgray")
        titulo_instrucciones.pack(pady=20)

        instrucciones_texto = (
            "1. Selecciona una facción para comenzar el juego.\n"
            "2. Cada facción tiene sus propias decisiones que puedes tomar.\n"
            "3. Toma decisiones estratégicas para expandir tu territorio.\n"
            "4. Gana puntos con decisiones exitosas y evita perder vidas.\n"
            "5. Si pierdes todas tus vidas, el juego terminará.\n"
            "6. Los eventos aleatorios pueden afectar tu progreso, ¡ten cuidado!"
        )

        instrucciones_label = tk.Label(self.frame_instrucciones, text=instrucciones_texto, font=("Arial", 12),
                                       bg="lightgray", justify="left")
        instrucciones_label.pack(pady=10)

        boton_volver = tk.Button(self.frame_instrucciones, text="Volver", font=("Arial", 14),
                                 command=self.volver_al_menu)
        boton_volver.pack(pady=20)

    def volver_al_menu(self):
        # Volver al menú inicial
        self.frame_instrucciones.pack_forget()
        self.pantalla_inicial()

    def iniciar_juego(self):
        self.frame_inicial.pack_forget()
        self.seleccionar_faccion()

    def seleccionar_faccion(self):
        self.frame_faccion = tk.Frame(self.root, bg="lightgreen")
        self.frame_faccion.pack(fill="both", expand=True)

        titulo = tk.Label(self.frame_faccion, text="Selecciona tu Facción", font=("Arial", 20), bg="lightgreen")
        titulo.pack(pady=20)

        for faccion in self.decisiones_base:
            boton_faccion = tk.Button(self.frame_faccion, text=faccion, font=("Arial", 14),
                                      command=lambda f=faccion: self.iniciar_ronda(f))
            boton_faccion.pack(pady=10)

    def iniciar_ronda(self, faccion):
        self.faccion = faccion
        self.frame_faccion.pack_forget()
        self.ronda += 1

        # Generar eventos aleatorios
        evento_aleatorio = random.choice(["Tormenta", "Espías descubiertos", "Rebelión interna", None])

        self.frame_ronda = tk.Frame(self.root, bg="lightyellow")
        self.frame_ronda.pack(fill="both", expand=True)

        # Información de puntaje y vidas
        info_vidas = tk.Label(self.frame_ronda, text=f"Vidas restantes: {self.vidas}", font=("Arial", 14),
                              bg="lightyellow")
        info_vidas.pack(pady=5)

        info_puntaje = tk.Label(self.frame_ronda, text=f"Puntos acumulados: {self.puntaje}", font=("Arial", 14),
                                bg="lightyellow")
        info_puntaje.pack(pady=5)

        titulo = tk.Label(self.frame_ronda, text=f"Ronda {self.ronda} - {self.faccion}", font=("Arial", 20),
                          bg="lightyellow")
        titulo.pack(pady=10)

        # Mostrar lo que está sucediendo
        if evento_aleatorio:
            label_evento = tk.Label(self.frame_ronda, text=f"Evento: {evento_aleatorio}!", bg="lightyellow",
                                    font=("Arial", 14))
            label_evento.pack(pady=10)
        else:
            label_evento = tk.Label(self.frame_ronda, text="Todo está tranquilo por ahora.", bg="lightyellow",
                                    font=("Arial", 14))
            label_evento.pack(pady=10)

        # Decisiones aleatorias por cada ronda (mayor variedad)
        decisiones_ronda = random.sample(self.decisiones_base[self.faccion], k=3)

        for decision in decisiones_ronda:
            boton_decision = tk.Button(self.frame_ronda, text=decision, font=("Arial", 14),
                                       command=lambda d=decision: self.realizar_accion(d))
            boton_decision.pack(pady=5)

    def realizar_accion(self, decision):
        # Resultado aleatorio de la acción
        resultado = random.choice(["éxito", "fracaso"])

        if resultado == "éxito":
            self.puntaje += 10
            mensaje = f"{decision} tuvo éxito! +10 puntos."
        else:
            self.vidas -= 1
            mensaje = f"{decision} fracasó! -1 vida."

        messagebox.showinfo("Resultado", mensaje)

        # Verificar si el juego continúa o termina
        if self.vidas > 0:
            self.frame_ronda.pack_forget()
            self.iniciar_ronda(self.faccion)
        else:
            messagebox.showinfo("Fin del Juego", f"Has perdido todas tus vidas.\nPuntaje final: {self.puntaje}")
            self.reiniciar_juego()

    def reiniciar_juego(self):
        self.vidas = 5
        self.puntaje = 0
        self.ronda = 0
        self.faccion = None
        self.frame_ronda.pack_forget()
        self.pantalla_inicial()


if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoConquista(root)
    root.mainloop()
