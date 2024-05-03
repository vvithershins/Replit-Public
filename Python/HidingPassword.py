import tkinter as tk

def pwinput(prompt, mask_password=True):
    result = None

    def get_password(entry):
        nonlocal result
        result = entry.get()
        root.destroy()

    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.title("Password Input")

    label = tk.Label(root, text=prompt)
    label.pack()

    entry = tk.Entry(root, show="*" if mask_password else "")
    entry.pack()

    button = tk.Button(root, text="Submit", command=lambda: get_password(entry))
    button.pack()

    root.mainloop()

    return result

# Example usage
print("check the output window")
yourpw = pwinput("Make a password")
print("you entered:", yourpw)

hello = pwinput("Enter a greeting", mask_password=False)
print("Hello entered:", hello)

