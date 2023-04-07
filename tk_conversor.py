import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import webbrowser
import os

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Conversor de imagens PNG para ICO")
        self.geometry("400x400")
        self.minsize(400, 400)
        try:
         self.iconbitmap("icon.ico")
        except:
            pass

        self.file_path = None
        self.image_preview = None       

        # Widgets
        self.label_file = tk.Label(self, text="Nenhum arquivo selecionado.")
        self.button_select = tk.Button(self, text="Selecionar arquivo", command=self.select_file)
        self.button_convert = tk.Button(self, text="Converter", command=self.convert_file)
        self.button_reset = tk.Button(self, text="Reset", command=self.reset_app)
        self.label_image = tk.Label(self, image=self.image_preview)

        self.github_label = tk.Label(self, text="Veja mais projetos no Github", fg="blue", cursor="hand2")
        self.github_label.pack(side="bottom")
        self.github_label.bind("<Button-1>", self.open_github_page)


        # Layout
        self.label_file.pack(pady=10)
        self.button_select.pack(pady=5)
        self.label_image.pack(pady=5)
        self.button_convert.pack(pady=5)
        self.button_reset.pack(pady=5)


      

    def open_github_page(self, event):
     webbrowser.open_new("https://github.com/Faguiro/conversor_png_ico")


    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Imagem PNG", "*.png")])
        if self.file_path:
            self.label_file.config(text=f"Arquivo selecionado: {self.file_path}")
            file_name, file_ext = os.path.splitext(os.path.basename(self.file_path))
            self.show_image_preview()
        else:
            self.label_file.config(text="Nenhum arquivo selecionado.")
            self.hide_image_preview()

    def show_image_preview(self):
        try:
            image = Image.open(self.file_path)
            image.thumbnail((200, 200))
            self.image_preview = ImageTk.PhotoImage(image)
            self.label_image.config(image=self.image_preview)

            # Resize window if needed
            window_width = max(self.winfo_width(), 400)
            window_height = max(self.winfo_height(), 400)
            image_width, image_height = image.size
            if image_width > window_width or image_height + 120 > window_height:
                new_width = max(image_width, 400)
                new_height = max(image_height + 120, 400)
                self.geometry(f"{new_width}x{new_height}")

        except Exception as e:
            self.hide_image_preview()


    def hide_image_preview(self):
        self.image_preview = None
        self.label_image.config(image=self.image_preview)

    def convert_file(self):
        filename = tk.filedialog.asksaveasfilename(initialdir="./converted", defaultextension=".ico", filetypes=[("Arquivo ICO", "*.ico")], title="Salvar arquivo")
        if self.file_path:
            try:
                if filename:
                    with Image.open(self.file_path) as im:
                        output_path = os.path.join("converted", filename)
                        im.save(output_path)
                        tk.messagebox.showinfo("Conversão concluída", f"Arquivo ICO gerado: {output_path}")
                        self.reset_app()
            except Exception as e:
                tk.messagebox.showerror("Erro", str(e))
        else:
            tk.messagebox.showwarning("Selecione um arquivo", "Por favor, selecione um arquivo PNG para converter.")

    def reset_app(self):
        self.file_path = None
        self.label_file.config(text="Nenhum arquivo selecionado.")
        self.hide_image_preview()

if __name__ == "__main__":
    app = App()
    app.mainloop()
