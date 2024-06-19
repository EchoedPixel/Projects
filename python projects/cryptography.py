import tkinter as tk


def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha(): # CHECK (A-Z) OR (a-z)
            if char.isupper():
                ascii_n = 65
            else:
                ascii_n = 97
            shft_ascii_n = (ord(char) - ascii_n + key) % 26 # ord  converts the char to ascii
            if shft_ascii_n < 0:
                shft_ascii_n += 26
            encrypted_char = chr(shft_ascii_n + ascii_n) # return the ascii to char
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(encrypted_message, key):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            ascii_n = 65 if char.isupper() else 97
            shft_ascii_n = (ord(char) - ascii_n - key) % 26
            if shft_ascii_n < 0:
                shft_ascii_n += 26
            decrypted_char = chr(shft_ascii_n + ascii_n)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

def encrypt_button_clicked():
    message = message_entry.get() # message entry is a global variable in tk
    key_text = key_entry.get()
    if key_text:
        try:
            key = int(key_text)
            encrypted_message = encrypt(message, key)
            result_label.config(text=f"Encrypted message: {encrypted_message}")
            add_to_list(encrypted_message, key) 
        except ValueError:
            messagebox.showerror("Error", "Invalid key value. Please enter an integer value.")
    else:
        messagebox.showerror("Error", "Key field is empty.")

def decrypt_button_clicked():
    encrypted_message = message_entry.get() # message entry is a global variable in tk
    key_text = key_entry.get()
    if key_text:
        try:
            key = int(key_text)
            decrypted_message = decrypt(encrypted_message, key)
            result_label.config(text=f"Decrypted message: {decrypted_message}")
            add_to_list(decrypted_message, key)  
        except ValueError:
            messagebox.showerror("Error", "Invalid key value. Please enter an integer value.")
    else:
        messagebox.showerror("Error", "Key field is empty.")

def add_to_list(message, key):
    data_listbox.insert(tk.END, f"Key: {key},\t Message: {message}")

root = tk.Tk()
root.title("Messenger encryptor/decryptor")
root.configure(bg="light grey")

message_label = tk.Label(root, text="Enter the message:",bg="light grey")
message_label.pack()

message_entry = tk.Entry(root, width=40)
message_entry.pack()

key_label = tk.Label(root, text="Enter the key (any integer):",bg="light grey")
key_label.pack()

key_entry = tk.Entry(root, width=40)
key_entry.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_button_clicked,bg="light grey")
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_button_clicked,bg="light grey")
decrypt_button.pack()

result_label = tk.Label(root, text="",bg="light grey")
result_label.pack()

data_listbox = tk.Listbox(root, width=50)
data_listbox.pack()

root.mainloop()