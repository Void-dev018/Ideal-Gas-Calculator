import customtkinter as ctk

# थीम और कलर सेट करें
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Ideal Gas Calculator")
root.geometry("400x500")

# कैलकुलेशन लॉजिक फंक्शन
def calculate():
    p_in = entry_p.get().strip().lower()
    v_in = entry_v.get().strip().lower()
    n_in = entry_n.get().strip().lower()
    t_in = entry_t.get().strip().lower()

    try:
        if p_in == "no" or p_in == "":
            v, n, t = float(v_in), float(n_in), float(t_in)
            ans = (n * 0.0821 * t) / v
            label_result.configure(text=f"P = {ans:.4f} atm")
        elif v_in == "no" or v_in == "":
            p, n, t = float(p_in), float(n_in), float(t_in)
            ans = (n * 0.0821 * t) / p
            label_result.configure(text=f"V = {ans:.4f} L")
        elif n_in == "no" or n_in == "":
            p, v, t = float(p_in), float(v_in), float(t_in)
            ans = (p * v) / (0.0821 * t)
            label_result.configure(text=f"n = {ans:.4f} mol")
        elif t_in == "no" or t_in == "":
            p, v, n = float(p_in), float(v_in), float(n_in)
            ans = (p * v) / (n * 0.0821)
            label_result.configure(text=f"T = {ans:.4f} K")
    except ValueError:
        label_result.configure(text="Error: Invalid Input!")

# UI डिजाइन (Labels and Entry Boxes)
ctk.CTkLabel(root, text="Ideal Gas Law (PV = nRT)", font=("Arial", 20, "bold")).pack(pady=15)
ctk.CTkLabel(root, text="Leave blank or type 'no' for the unknown value", font=("Arial", 12)).pack(pady=2)

developer_label = ctk.CTkLabel(root, text="Developed by: Naman", font=("Arial", 12, "italic"), text_color="#00FFFF") # Neon Cyan Color
developer_label.pack(pady=2)


# Input P
ctk.CTkLabel(root, text="Value of P?").pack(pady=2)
entry_p = ctk.CTkEntry(root, placeholder_text="e.g. 2 or no")
entry_p.pack(pady=2)

# Input V
ctk.CTkLabel(root, text="Value of V?").pack(pady=2)
entry_v = ctk.CTkEntry(root, placeholder_text="e.g. 8.21")
entry_v.pack(pady=2)

# Input n
ctk.CTkLabel(root, text="Number of Moles (n)?").pack(pady=2)
entry_n = ctk.CTkEntry(root, placeholder_text="e.g. 0.5")
entry_n.pack(pady=2)

# Input T
ctk.CTkLabel(root, text="Value of Temp (T)?").pack(pady=2)
entry_t = ctk.CTkEntry(root, placeholder_text="e.g. 400")
entry_t.pack(pady=2)

# Button
btn = ctk.CTkButton(root, text="Calculate", command=calculate)
btn.pack(pady=20)

# Result Output
label_result = ctk.CTkLabel(root, text="Result will appear here", font=("Arial", 16, "bold"), text_color="#1f538d")
label_result.pack(pady=10)

root.mainloop()

