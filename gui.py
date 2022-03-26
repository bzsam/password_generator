import tkinter as tk
import password


# Values if the entries are empty
MIN = 6
MAX = 12


class GUI:
    def __init__(self, wd):
        """GUI for the PASSWORD app. Takes only one input, the Tkinter frame."""
        self.wd = wd  # Tkinter frame

        # Frame configuration
        self.wd.title("Password generator")
        self.wd.minsize(400, 400)
        self.wd.maxsize(400, 400)
        self.wd.configure(bg="#d0e9fd")

        # Text label
        self.label = tk.Label(self.wd, text="Password generator")
        self.label.configure(bg="#d0e9fd")
        self.label.config(font=('Helvatical bold', 15))
        self.label.pack(pady=(50, 20))

        # Min length label
        self.min = tk.Label(self.wd, text="Min length")
        self.min.configure(bg="#d0e9fd")
        self.min.config(font=('Helvatical bold', 10))
        self.min.pack(pady=(0, 0))

        # Min length entry
        self.entry1 = tk.Entry(justify="center", bd=0, bg="#e3ffff")
        self.entry1.focus()
        self.entry1.pack(pady=(0, 20))

        # Max length label
        self.max = tk.Label(self.wd, text="Max length")
        self.max.configure(bg="#d0e9fd")
        self.max.config(font=('Helvatical bold', 10))
        self.max.pack(pady=(0, 0))

        # Max length entry
        self.entry2 = tk.Entry(justify="center", bd=0, bg="#e3ffff")
        self.entry2.pack(pady=(0, 20))

        # Button to generate the password
        self.button = tk.Button(text="Generate", command=self._get_input, bg="#e3ffff", bd=0)
        self.button.config(font=('Helvatical bold', 14))
        self.wd.bind("<Return>", self._get_input)
        self.button.pack(pady=(20, 0))

        # Label to show the generated password
        self.result = tk.Label(self.wd, text="")
        self.result.configure(bg="#d0e9fd")
        self.result.config(font=('Helvatical bold', 13))
        self.result.pack(pady=(20, 0))

        # Button to copy the generated password
        self.copy_button = tk.Button(text="Copy", command=self._copy, bg="#e3ffff", bd=0)
        self.copy_button.config(font=('Helvatical bold', 14))

        self.min = ""  # Min length value
        self.max = ""  # Max length value
        self.pw = password.Password()  # Password generator
        self.password = ""  # Variable for the password

    def _get_input(self,ok=None):
        """ Function to take the length values, formats them for the password generator"""
        self.min = self.entry1.get()
        self.max = self.entry2.get()
        try:
            # With empty entries it sets itself the length values
            if self.min == "":
                self.min = MIN
            if self.max == "":
                self.max = MAX
            self.min = int(self.min)
            self.max = int(self.max)
            if self.min < 6 or self.min > self.max or self.max > 30:
                raise
            self._output()
        except:
            self.result.configure(text="Invalid input")
            self.entry1.delete(0, tk.END)
            self.entry2.delete(0, tk.END)
            self.entry1.focus()
            self.copy_button.pack_forget()

    def _output(self):
        """Calls the password generator, prints the generated password"""
        self.password = self.pw.password(self.min, self.max)
        self.result.configure(text=self.password)
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.entry1.focus()
        self.copy_button.pack(pady=(20, 0))

    def _copy(self):
        """Creates a copy to the clipboard from the password"""
        self.wd.clipboard_append(self.password)
