import smtplib
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import messagebox, ttk
from flask import Flask, request, render_template, redirect, url_for, flash
import uuid
import re
import webbrowser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
 
 
 
# Email configuration
EMAIL_USERNAME = "zimkhitha.nongomaza@capaciti.org.za"
EMAIL_PASSWORD = "Losiwe@1"
SMTP_SERVER = "smtp.office365.com"
SMTP_PORT = 587
 
app = Flask(__name__)
app.secret_key =""
# Function to generate unique password
def generate_password():
    return str(uuid.uuid4())
 
# Function to generate unique access link

def generate_access_link(guest_name):
    return f"https://Yonela986.github.io/rsvp/{guest_name}"
# Function to send email invitation
def send_invitation(guest_name, guest_email, password):
    access_link = generate_access_link(guest_name)

    msg = MIMEMultipart()
    msg['Subject'] = 'Event Invitation'
    msg['From'] = EMAIL_USERNAME
    msg['To'] = guest_email

    body = f"""\
    <html>
      <body>
        <p>Dear {guest_name},</p>
        <p>You're invited to our event! Your password is:</p>
        <p><strong>{password}</strong></p>
        <p>Click on the link to RSVP: <a href="{access_link}">RSVP Here</a></p>
        <p>Best regards,<br>Zimi Nongomaza</p>
      </body>
    </html>
    """
    
    msg.attach(MIMEText(body, 'html'))

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
    server.sendmail(EMAIL_USERNAME, guest_email, msg.as_string())
    server.quit()

#Validation Email Function
def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)
# Function to validate cellphone number
def validate_cellphone(cellphone):
    pattern = r"^\d{10}$"
    return re.match(pattern, cellphone)
 
# Function to validate name
def validate_name(name):
    pattern = r"^[a-zA-Z\s]+$"
    return re.match(pattern, name)

# Register custom protocol handler
def rsvp_protocol_handler(url):
    guest_name = url.split("://")[1]
    rsvp_window = tk.Toplevel()
    rsvp_window.title("RSVP")
    # RSVP GUI code here...
    name_entry = tk.Entry(rsvp_window)
    name_entry.insert(0, guest_name)
    name_entry.pack()
 
# Set up protocol handler
webbrowser.register('rsvp', rsvp_protocol_handler)
 
 
# Function to validate email

 

 
# Function to add guest to list and send invitation

# Function to view guest list
def view_guests():
    tree.delete(*tree.get_children())
 
    try:
        with open("guestlist.txt", "r") as file:
            guests = file.readlines()
 
        for guest in guests:
            name, email, cellphone, _ = guest.strip().split(",")
            tree.insert("", tk.END, values=(name, email, cellphone))
    except FileNotFoundError:
        messagebox.showerror("Error", "No guests added yet.")
 
# Function to delete selected guest
def delete_guest():
    selected = tree.focus()
 
    if selected:
        tree.delete(selected)
 
        with open("guestlist.txt", "r") as file:
            guests = file.readlines()
 
        with open("guestlist.txt", "w") as file:
            for guest in guests:
                name, email, cellphone, _ = guest.strip().split(",")
                if name != tree.item(selected, "values")[0]:
                    file.write(guest)
 
        messagebox.showinfo("Success", "Guest deleted.")
    else:
        messagebox.showerror("Error", "Please select a guest.")
 
# Function to update selected guest
def update_guest():
    selected = tree.focus()
 
    if selected:
        name = tree.item(selected, "values")[0]
        email = tree.item(selected, "values")[1]
        cellphone = tree.item(selected, "values")[2]
 
        update_window = tk.Toplevel()
        update_window.title("Update Guest")
 
        name_label = tk.Label(update_window, text="Name:")
        name_label.pack()
        name_entry = tk.Entry(update_window)
        name_entry.insert(0, name)
        name_entry.pack()
 
        email_label = tk.Label(update_window, text="Email:")
        email_label.pack()
        email_entry = tk.Entry(update_window)
        email_entry.insert(0, email)
        email_entry.pack()
 
        cellphone_label = tk.Label(update_window, text="Cellphone:")
        cellphone_label.pack()
        cellphone_entry = tk.Entry(update_window)
        cellphone_entry.insert(0, cellphone)
        cellphone_entry.pack()
 
        def save_update():
            new_name = name_entry.get()
            new_email = email_entry.get()
            new_cellphone = cellphone_entry.get()
 
            if not validate_name(new_name):
                messagebox.showerror("Error", "Invalid name.")
                return
 
            if not validate_email(new_email):
                messagebox.showerror("Error", "Invalid email.")
                return
 
            if not validate_cellphone(new_cellphone):
                messagebox.showerror("Error", "Invalid cellphone number.")
                return
 
            with open("guestlist.txt", "r") as file:
                guests = file.readlines()
 
            with open("guestlist.txt", "w") as file:
                for guest in guests:
                    guest_name, guest_email, guest_cellphone, password = guest.strip().split(",")
                    if guest_name == name:
                        file.write(f"{new_name},{new_email},{new_cellphone},{password}\n")
                    else:
                        file.write(guest)
 
            tree.item(selected, values=(new_name, new_email, new_cellphone))
            update_window.destroy()
            messagebox.showinfo("Success", "Guest updated.")
 
        save_button = tk.Button(update_window, text="Save", command=save_update)
        save_button.pack()
    else:
        messagebox.showerror("Error", "Please select a guest.")
 
# Function to RSVP
def rsvp():
    rsvp_window = tk.Toplevel()
    rsvp_window.title("RSVP")
 
#GUI FOR RSVP
    name_label = tk.Label(rsvp_window, text="Name:")
    name_label.pack()
    name_entry = tk.Entry(rsvp_window)
    name_entry.pack()
 
    email_label = tk.Label(rsvp_window, text="Email:")
    email_label.pack()
    email_entry = tk.Entry(rsvp_window)
    email_entry.pack()
 
    password_label = tk.Label(rsvp_window, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(rsvp_window, show="")
    password_entry.pack()
 
    def submit_rsvp():
       name = name_entry.get().strip()
       email = email_entry.get().strip()
       password = password_entry.get().strip()
 
       
 
       if not name or not email or not password:
          messagebox.showerror("Error", "Please fill in all fields.")
          return
 
       try:
           with open("guestlist.txt", "r") as file:
            guests = file.readlines()
 
           for guest in guests:
               
               guest_info = guest.strip().split(",")
 
               if len(guest_info) < 4:
 
                messagebox.showerror("Error", "Invalid guest information.")
                continue
 
               guest_name, guest_email, _, guest_password = guest_info
 
               if  guest_name == name and guest_email == email and guest_password == password:
                # RSVP successful
                with open("rsvp.txt", "a") as rsvp_file:
                    rsvp_file.write(f"{name},{email}\n")
                messagebox.showinfo("Success", "RSVP successful!")
                rsvp_window.destroy()
                break
           else:
                  messagebox.showerror("Error", "Invalid credentials.")
 
 
       except FileNotFoundError:
        messagebox.showerror("Error", "Guest list file not found.")
       except Exception as e:
        messagebox.showerror("Error", str(e))
 
 
 
    submit_button = tk.Button(rsvp_window, text="Submit RSVP", command=submit_rsvp)
    submit_button.pack()
 
# Create GUI
root = tk.Tk()
root.title("Guest List System")
 
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()
 
email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()
 
cellphone_label = tk.Label(root, text="Cellphone:")
cellphone_label.pack()
cellphone_entry = tk.Entry(root)
cellphone_entry.pack()
 
add_button = tk.Button(root, text="Add Guest", command=add_guest)
add_button.pack()
 
view_button = tk.Button(root, text="View Guests", command=view_guests)
view_button.pack()
 
delete_button = tk.Button(root, text="Delete Guest", command=delete_guest)
delete_button.pack()
 
update_button = tk.Button(root, text="Update Guest", command=update_guest)
update_button.pack()
 
rsvp_button = tk.Button(root, text="RSVP", command=rsvp)
rsvp_button.pack()
 
tree = ttk.Treeview(root)
tree['columns'] = ('Name', 'Email', 'Cellphone')
tree.column("#0", width=0, )
tree.column("Name", anchor=tk.W, width=100)
tree.column("Email", anchor=tk.W, width=150)
tree.column("Cellphone", anchor=tk.W, width=100)
tree.heading("#0", text='', anchor=tk.W)
tree.heading("Name", text='Name', anchor=tk.W)
tree.heading("Email", text='Email', anchor=tk.W)
tree.heading("Cellphone", text='Cellphone', anchor=tk.W)
tree.pack()
 
root.mainloop()