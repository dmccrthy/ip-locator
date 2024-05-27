import tkinter as tk
import src.main as main

# Define functions
def updateWindow():
    # Get username status
    status = main.checkUsername(username.get())

    # Add/update window w/ response
    response = tk.Label(window, text=status, font="bold")
    response.pack(fill="both", expand=True, side="left")

# Init tkinter & windows
root = tk.Tk()
root.title("Github Username Checker")

window = tk.Frame(root, padx=100, pady=100)
window.pack(fill="both", expand=True)

# Create text labels
header = tk.Label(window, text="Github Username Checker!", font=("Terminal", 15, "bold"))
header.pack(fill="both", expand=True, side="top", pady=30)

instruct = tk.Label(window, text="Input Username Below:")
instruct.pack(fill="both", expand=True)

# Create username input
username = tk.StringVar()
inputuser = tk.Entry(window, textvariable=username)
inputuser.pack(fill="both", expand=True)

# Check user button and func call
checkuser = tk.Button(window, text="Check Username", command=updateWindow)
checkuser.pack(fill="both", expand=True,)

# Response header

reshead = tk.Label(window, text="Username Availability:")
reshead.pack(fill="both", expand=True, pady=20)

root.mainloop()