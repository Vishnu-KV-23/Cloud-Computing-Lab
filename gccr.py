import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog

host = '127.0.0.1'
port = 12347

class Client:
    def __init__(self, host, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))

        msg = tk.Tk()
        msg.withdraw()
        self.username = simpledialog.askstring("Username", "Enter your username", parent=msg)

        self.gui_done = False
        self.running = True

        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)

        gui_thread.start()
        receive_thread.start()

    def gui_loop(self):
        self.win = tk.Tk()
        self.win.title("Chat")

        self.chat_label = tk.Label(self.win, text="Chat:", font=("Arial", 12))
        self.chat_label.pack(padx=20, pady=5)

        self.text_area = scrolledtext.ScrolledText(self.win)
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state='disabled')

        self.msg_label = tk.Label(self.win, text="Message:", font=("Arial", 12))
        self.msg_label.pack(padx=20, pady=5)

        self.input_area = tk.Entry(self.win, font=("Arial", 12))
        self.input_area.pack(padx=20, pady=5)

        self.send_button = tk.Button(self.win, text="Send", command=self.write)
        self.send_button.pack(padx=20, pady=5)

        self.gui_done = True
        self.win.protocol("WM_DELETE_WINDOW", self.stop)
        self.win.mainloop()

    def write(self):
        message = f'{self.username}: {self.input_area.get()}'
        self.client_socket.send(message.encode('ascii'))
        self.input_area.delete(0, tk.END)

    def stop(self):
        self.running = False
        self.win.destroy()
        self.client_socket.close()
        exit(0)

    def receive(self):
        while self.running:
            try:
                message = self.client_socket.recv(1024).decode('ascii')
                if message == 'NICK':
                    self.client_socket.send(self.username.encode('ascii'))
                else:
                    if self.gui_done:
                        self.text_area.config(state='normal')
                        self.text_area.insert('end', message + '\n')
                        self.text_area.yview('end')
                        self.text_area.config(state='disabled')
            except ConnectionAbortedError:
                break
            except:
                print("An error occurred!")
                self.client_socket.close()
                break

client = Client(host, port)
