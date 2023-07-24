import tkinter

root = tkinter.Tk()

def read_file():
    labels = [w for w in root.winfo_children() if isinstance(w, tkinter.Label)]
    for label in labels:
        label.destroy()
    with open(input1.get(), 'r') as file:
        for index, line in enumerate(file):
            tkinter.Label(root, text = f'{index + 1}: {line}').grid(row=index + 2, column=1)

input1 = tkinter.Entry(root)
input1.grid(row=1, column=1)

submit = tkinter.Button(root, text = "Read File", command=read_file)
submit.grid(row=1, column=2)

if __name__ == '__main__':
    root.mainloop()