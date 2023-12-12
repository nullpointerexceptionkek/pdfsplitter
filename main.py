import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
import os
def split_pdf(input_pdf_path, output_pdf_path, start_page, end_page):
    with open(input_pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()

        for page_num in range(start_page - 1, end_page):
            writer.add_page(reader.pages[page_num])

        with open(output_pdf_path, 'wb') as output_file:
            writer.write(output_file)

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        entry_input_pdf.delete(0, tk.END)
        entry_input_pdf.insert(0, file_path)


def process_pdf():
    input_pdf = entry_input_pdf.get()

    if not input_pdf:
        messagebox.showwarning("No file selected", "Please select a PDF file first.")
        return
    input_dir = os.path.dirname(input_pdf)

    output_pdf = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        initialdir=input_dir
    )

    if not output_pdf:
        return
    with open(input_pdf, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        total_pages = len(reader.pages)

    start_page = int(entry_start_page.get() or 1)
    end_page = int(entry_end_page.get() or total_pages)

    try:
        split_pdf(input_pdf, output_pdf, start_page, end_page)
        messagebox.showinfo("Success", "PDF successfully split and saved!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


root = tk.Tk()
root.title("PDF Splitter")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

label_input_pdf = tk.Label(frame, text="Select PDF:")
label_input_pdf.pack()

entry_input_pdf = tk.Entry(frame, width=50)
entry_input_pdf.pack()

button_browse = tk.Button(frame, text="Browse", command=select_file)
button_browse.pack()

label_start_page = tk.Label(frame, text="Start Page:")
label_start_page.pack()

entry_start_page = tk.Entry(frame)
entry_start_page.pack()

label_end_page = tk.Label(frame, text="End Page:")
label_end_page.pack()

entry_end_page = tk.Entry(frame)
entry_end_page.pack()

button_split = tk.Button(frame, text="Split PDF", command=process_pdf)
button_split.pack()

root.mainloop()
