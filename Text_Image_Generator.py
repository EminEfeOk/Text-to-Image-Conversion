import tkinter as tk
from tkinter import ttk, filedialog, messagebox , StringVar
from PIL import Image, ImageDraw, ImageFont

def create_text_image(text, font_path, font_size, text_color, bg_color, output_path, text_Location, Png_height,Png_width):
        font = ImageFont.truetype(font_path, font_size)
        image_width = Png_width
        image_height = Png_height
        image = Image.new("RGB", (image_width, image_height), bg_color)

        draw = ImageDraw.Draw(image)

        estimated_text_width = (font_size * len(text) / 2 ) + (font_size / len(text))
        estimated_text_height = font_size

        x = (image_width - estimated_text_width) / 2
        y = (image_height - estimated_text_height) / 2

        if text_Location == "left":
            x = 0 
        elif text_Location == "center":
            x = (image_width - estimated_text_width) / 2
        elif text_Location == "right":
            x = image_width - estimated_text_width
        draw.text((x, y), text, fill=text_color, font=font)

        if image_width < estimated_text_width:
            messagebox.showerror("Image Generation Failed", "(Image width < text width) please increase the image width or embrace the text width")
        else:
            image.save(output_path)
            messagebox.showinfo("Image Generated", "Image successfully generated!")

class TextImageGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Text Image Generator")
        self.master.update_idletasks()
        width = self.master.winfo_width()
        frm_width = self.master.winfo_rootx() - self.master.winfo_x()
        win_width = width + 2 * frm_width
        height = self.master.winfo_height()
        titlebar_height = self.master.winfo_rooty() - self.master.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.master.winfo_screenwidth() // 2 - win_width // 2
        y = self.master.winfo_screenheight() // 2 - win_height // 2
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.master.maxsize(400, 170)
        self.master.minsize(400, 170)

        style = ttk.Style()
        style.configure("BW.TLabel", foreground="black", background="white")


        self.text_label = ttk.Label(master, text="Text:")
        self.text_entry_var = tk.StringVar()
        self.text_entry_var.set("Deneme")
        self.text_entry = tk.Entry(master, textvariable=self.text_entry_var,)

        self.locations = StringVar()
        self.location = tk.Label(master, text="Selected Location ")
        self.one = ttk.Radiobutton(master, text="Left", variable=self.locations, value = "left")
        self.two = ttk.Radiobutton(master, text="Center", variable=self.locations, value = "center")
        self.three = ttk.Radiobutton(master, text="Right", variable=self.locations, value = "right")

        self.w = tk.Label(master, text="Png width:")
        self.h = tk.Label(master, text="Png Height:")
        self.w_size_var = tk.StringVar()
        self.w_size_var.set("500")
        self.h_size_var = tk.StringVar()
        self.h_size_var.set("500")
        self.PngW_entry = tk.Entry(master,textvariable=self.w_size_var)
        self.PngH_entry = tk.Entry(master,textvariable=self.h_size_var)

        self.browse_button = ttk.Button(master, text="Browse Font", command=self.browse_font, style="TButton")

        self.font_entry = tk.Entry(master)

        self.font_size_label = tk.Label(master, text="Font Size:")
        self.font_size_var = tk.StringVar()
        self.font_size_var.set("12")
        self.font_size_entry = tk.Entry(master, textvariable=self.font_size_var)

        self.text_color_label = tk.Label(master, text="Text Color (RGB):")
        self.c_var = tk.StringVar()
        self.c_var.set("255,255,255")
        self.text_color_entry = tk.Entry(master,textvariable=self.c_var)

        self.bg_color_label = tk.Label(master, text="Background Color (RGB):")
        self.bg_var = tk.StringVar()
        self.bg_var.set("35,35,35")
        self.bg_color_entry = tk.Entry(master, textvariable=self.bg_var)

        self.generate_button = ttk.Button(master, text="Generate Image", command=self.generate_image, style="TButton")



        self.text_label.grid(column=0, row=0)
        self.location.grid(column=0, row=2)
        self.one.grid(column=0, row=3)
        self.two.grid(column=0, row=4)
        self.three.grid(column=0, row=5)
        self.text_entry.grid(column=0, row=1, padx = 8)
        self.browse_button.grid(column=3, row=0, pady = 2)
        self.font_entry.grid(column=3, row=1,)
        self.font_size_label.grid(column=3, row=2,)
        self.font_size_entry.grid(column=3, row=3,)
        self.text_color_label.grid(column=6, row=0,)
        self.text_color_entry.grid(column=6, row=1,)
        self.bg_color_label.grid(column=6, row=2,)
        self.bg_color_entry.grid(column=6, row=3,)
        self.w.grid(column=3, row=4)
        self.h.grid(column=6, row=4)
        self.PngW_entry.grid(column=6, row=5)
        self.PngH_entry.grid(column=3, row=5)
        self.generate_button.grid(column=3, row=20 ,padx = 5 , pady = 5)

    def generate_image(self):
        text = self.text_entry.get()
        font_path = self.font_entry.get()
        font_size = self.font_size_var.get()
        text_color = map(int, self.text_color_entry.get().split(','))
        bg_color = map(int, self.bg_color_entry.get().split(','))
        text_Location = self.locations.get()
        Png_width = self.PngW_entry.get()
        Png_height = self.PngH_entry.get()

        output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        
        if not text:
            messagebox.showerror("Image Generation Failed", "Please fill in the text field.")
        elif not font_path:
            messagebox.showerror("Image Generation Failed", "Please fill in the font path field.")
        elif not text_color:
            messagebox.showerror("Image Generation Failed", "Please fill in the text color field.")
        elif not bg_color:
            messagebox.showerror("Image Generation Failed", "Please fill in the background color field.")
        elif not output_path:
            messagebox.showerror("Image Generation Failed", "Please fill in the output path field.")
        elif not Png_width:
            messagebox.showerror("Image Generation Failed", "Please fill in the Png width field.")
        elif not Png_height:
            messagebox.showerror("Image Generation Failed", "Please fill in the Png height field.")
        elif not font_size:
            messagebox.showerror("Image Generation Failed", "Please fill in the font size field.")
        else:
            try:
                font_size = int(font_size)
            except AttributeError as e:
                messagebox.showerror("Image Generation Failed", "Enter the number pls fontsize")
            try:
                Png_width = int(Png_width)
            except AttributeError as e:
                messagebox.showerror("Image Generation Failed", "Enter the number pls Png_width")
            try:
                Png_height = int(Png_height)
            except AttributeError as e:
                messagebox.showerror("Image Generation Failed", "Enter the number pls Png_height")
            try:
                text_color = tuple(text_color)
            except AttributeError as e:
                messagebox.showerror("Image Generation Failed", "Enter the tuple pls (0,0,0) textcolor")
            try:
                bg_color = tuple(bg_color)
            except AttributeError as e:
                messagebox.showerror("Image Generation Failed", "Enter the tuple pls (0,0,0) bgcolor")
            
            create_text_image(text, font_path, font_size, text_color, bg_color, output_path, text_Location,Png_width,Png_height)
            

    def browse_font(self):
        font_path = filedialog.askopenfilename(filetypes=[("Font files", "*.ttf;*.otf")])
        if font_path:
            self.font_entry.delete(0, tk.END)
            self.font_entry.insert(0, font_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextImageGeneratorApp(root)
    root.mainloop()
