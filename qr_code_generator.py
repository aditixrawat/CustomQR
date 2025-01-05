import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image, ImageTk
import os

def generate_qr():
    url = url_entry.get()
    clr = CLR_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return
    if not clr:
        clr="black"
    try:
    # Create a QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=5,
            border=2,
        )
        qr.add_data(url)
        qr.make(fit=True)

        # Generate  QR code image
        img = qr.make_image(fill_color=clr,back_color="white")
        img_path = "qrcode.png"
        img.save(img_path)

        # Display QR code in the GUI
        qr_image = Image.open(img_path)
        qr_image = qr_image.resize((150, 150))
        qr_photo = ImageTk.PhotoImage(qr_image)
        qr_label.config(image=qr_photo)
        qr_label.image = qr_photo
        messagebox.showinfo("Success", f"QR code saved as {img_path}")
    except ValueError:
        messagebox.showerror("Error","pls enter valid color") 

def save_qr():
    if not qr_label.image:
        messagebox.showerror("Error", "No QR code to save!")
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".png", 
                                             filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if save_path:
        os.rename("qrcode.png", save_path)
        messagebox.showinfo("Saved", f"QR code saved as {save_path}")



# GUI setup
root = ttk.Window(themename="vapor")  
root.title("QR Code Generator ")

# rounded corner card using a Canvas
canvas = ttk.Canvas(root,width=560, height=400)
canvas.pack(pady=20)

# Rounded rectangle (for card background)
radius = 20
x1, y1, x2, y2 = 10, 10, 550, 390  # Dimensions of the card
canvas.create_arc(x1, y1, x1 + 2 * radius, y1 + 2 * radius, start=90, extent=90, fill="#000435", outline="")
canvas.create_arc(x2 - 2 * radius, y1, x2, y1 + 2 * radius, start=0, extent=90, fill="#000435", outline="")
canvas.create_arc(x1, y2 - 2 * radius, x1 + 2 * radius, y2, start=180, extent=90, fill="#000435", outline="")
canvas.create_arc(x2 - 2 * radius, y2 - 2 * radius, x2, y2, start=270, extent=90, fill="#000435", outline="")
canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, fill="#000435", outline="")
canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, fill="#000435", outline="")

# Add form fields inside the card
card_frame = ttk.Frame(canvas, style="secondary", padding=20)
canvas.create_window((280, 190), window=card_frame, anchor=CENTER)

# URL entry inside the card
ttk.Label(card_frame, text="Enter URL:", font=("Helvetica", 12)).pack(pady=10)
url_entry = ttk.Entry(card_frame, width=50, bootstyle=SUCCESS)
url_entry.pack(pady=5)

# Fill color entry inside the card
ttk.Label(card_frame, text="Choose Fill color:", font=("Helvetica", 12)).pack(pady=10)
CLR_entry = ttk.Entry(card_frame, width=50, bootstyle=INFO)
CLR_entry.pack(pady=5)
# Generate button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=10)

# QR Code display
qr_label = tk.Label(root)
qr_label.pack(pady=10)

# Save button
save_button = tk.Button(root, text="Save QR Code", command=save_qr)
save_button.pack(pady=10)

# Run the GUI
root.mainloop()
