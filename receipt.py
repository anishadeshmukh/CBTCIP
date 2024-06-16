import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
from reportlab.lib.utils import ImageReader


def create_receipt(receipt_number, date, company_name, customer_name, items, total_amount,):
    # Define the PDF file name
    receipt_filename = f"receipt_{receipt_number}.pdf"

    # Create a canvas object
    c = canvas.Canvas(receipt_filename, pagesize=letter)
    width, height = letter


    # Set the title of the receipt
    c.setTitle("Payment Receipt")

    # Draw the company name
    c.setFont("Helvetica-Bold", 20)
    c.drawString(30, 750, company_name)

    # Draw the receipt title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(30, 725, "Payment Receipt")

    # Draw the receipt number and date
    c.setFont("Helvetica", 12)
    c.drawString(30, 700, f"Receipt Number: {receipt_number}")
    c.drawString(400, 700, f"Date: {date}")

    # Draw a line to separate the header
    c.line(30, 690, 580, 690)

    # Draw the customer name
    c.drawString(30, 670, f"Customer Name: {customer_name}")

    # Draw the table headers
    c.drawString(30, 650, "Item")
    c.drawString(400, 650, "Price")

    # Draw the items
    y = 630
    for item, price in items.items():
        c.drawString(30, y, item)
        c.drawString(400, y, f"${price:.2f}")
        y -= 20

    # Draw the total amount
    c.setFont("Helvetica-Bold", 14)
    c.drawString(30, y-20, f"Total: ${total_amount:.2f}")

    # Save the PDF
    c.save()
    messagebox.showinfo("Success", f"Receipt saved as {receipt_filename}")

def add_item():
    item = item_name_entry.get()
    price = price_entry.get()
    if item and price:
        try:
            price = float(price)
            items[item] = price
            items_listbox.insert(tk.END, f"{item}: ${price:.2f}")
            item_name_entry.delete(0, tk.END)
            price_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid input", "Price must be a number")
    else:
        messagebox.showerror("Missing input", "Item name and price are required")

def generate_receipt():
    receipt_number = receipt_number_entry.get()
    date = date_entry.get()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    company_name = company_name_entry.get()
    customer_name = customer_name_entry.get()
   

    if not (receipt_number and company_name and customer_name):
        messagebox.showerror("Missing input", "Receipt number, company name, and customer name are required")
        return

    total_amount = sum(items.values())
    create_receipt(receipt_number, date, company_name, customer_name, items, total_amount,)

app = tk.Tk()
app.title("Receipt Generator ")
app.configure(bg='lightblue')
app.geometry("700x700")
# Entry fields

tk.Label(app, text="RECEIPT GENERATOR",bg='lightgreen',font=("Helvetica", 25 , "bold")).grid(row=0, column=2,padx=10,pady=10)
tk.Label(app, text="Receipt Number:",bg='pink').grid(row=1, column=1,padx=10,pady=10)
receipt_number_entry = tk.Entry(app)
receipt_number_entry.grid(row=1, column=2)

tk.Label(app, text="Date (YYYY-MM-DD):",bg='white').grid(row=2, column=1,padx=10,pady=10)
date_entry = tk.Entry(app)
date_entry.grid(row=2, column=2)

tk.Label(app, text="Company Name:",bg='pink').grid(row=4, column=1,padx=10,pady=10)
company_name_entry = tk.Entry(app)
company_name_entry.grid(row=4, column=2)

tk.Label(app, text="Customer Name:",bg='white').grid(row=6, column=1,padx=10,pady=10)
customer_name_entry = tk.Entry(app)
customer_name_entry.grid(row=6, column=2)



# Items input
tk.Label(app, text="Item Name:",bg='pink').grid(row=8, column=1,padx=10,pady=10)
item_name_entry = tk.Entry(app)
item_name_entry.grid(row=8, column=2)

tk.Label(app, text="Price:",bg='white').grid(row=9, column=1,padx=10,pady=10)
price_entry = tk.Entry(app)
price_entry.grid(row=9, column=2)

tk.Button(app, text="Add Item", command=add_item).grid(row=10, column=2, columnspan=2,padx=10,pady=10)

# Items listbox
items_listbox = tk.Listbox(app, width=50)
items_listbox.grid(row=11, column=2, columnspan=2,padx=10,pady=10)

# Generate receipt button
tk.Button(app, text="Generate Receipt", command=generate_receipt).grid(row=12, column=2, columnspan=2,padx=10,pady=10)

items = {}

app.mainloop()
