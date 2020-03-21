from tkinter import *
from converter import downloader
from pytube.exceptions import RegexMatchError
from additional import metadata_changer
from cleaner import cleaner


class Converter(object):


    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.background = Label(window, image=img, bd=0)
        self.background.pack(fill='both', expand=True)
        self.background.image = img

        self.entry_link = Entry(self.background, font=('Arial', 15), width=25, bg="#90e8b5", relief=GROOVE)
        self.entry_link.focus()
        self.entry_link.place(relx=0.5,rely=0.2, anchor=CENTER)

        self.entry_name_of_the_file = Entry(self.background, font=("Arial", 20), width=10, bg="#90e8b5", relief=GROOVE)
        self.entry_name_of_the_file.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.download_button = Button(self.background, text="Convert", command=self.la_converter, image=icon2, bg="#cae6d6", relief=GROOVE)
        self.download_button.place(relx=0.5, rely=0.6, anchor=CENTER)

        self.label1 = Label(window, text="File name here", font=("Tiza", 10))
        self.label1.place(relx=0.5, rely=0.3, anchor=CENTER)

        self.label2 = Label(window, text="Your link goes here", font=("Tiza", 10))
        self.label2.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.l1 = Label(window, text="Title", font=("Tiza", 7))
        self.l2 = Label(window, text="Artist", font=("Tiza", 7))
        self.song = Entry(self.background, font=("Courier", 20), width=10, bg="#90e8b5")
        self.artist = Entry(self.background, font=("Courier", 20), width=10, bg="#90e8b5")
        self.button = Button(self.background, text="changes", command=self.tag_changer, bg="#cae6d6", relief=GROOVE, image=icon2)

        self.butt_hole = Button(self.background, text="R you done?",font=("Tiza", 20), command=self.close_window)

    def la_converter(self):
        try:
            downloader(self.entry_link.get(), self.entry_name_of_the_file.get())
            self.erase_all()
            self.new_window()

        except RegexMatchError:
            # messagebox.showerror("Wrong text", "Please enter the link \n Example: https://www.youtube.com")
            warning = Label(window, text="\nCome on\n Enter dat link bro", bg="red", fg="white", font=("Tiza",10), relief=GROOVE)
            warning.place(relx=0.5, rely=0.85, anchor=CENTER)
            self.entry_link.config(bg="red")
            window.after(4000, self.forget, warning)
            window.after(3000, self.config, self.entry_link)

        except KeyError:
            l = Label(window, text="\nwhere's dat name bro?", bg="red", fg="white", font=("Tiza", 10), relief=GROOVE)
            l.place(relx=0.5, rely=0.85, anchor=CENTER)
            self.entry_name_of_the_file.config(bg="red")

            window.after(4000, self.forget, l)
            window.after(3000, self.config, self.entry_name_of_the_file)

    def erase_all(self):
        self.label1.place_forget()
        self.label2.place_forget()
        self.entry_name_of_the_file.place_forget()
        self.entry_link.place_forget()
        self.download_button.place_forget()

    def new_window(self):
        the_title = Label(window, text="Adjust:", font=("Tiza", 10))
        the_title.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.l1.place(relx=0.2, rely=0.3, anchor=CENTER)
        self.l2.place(relx=0.2, rely=0.5, anchor=CENTER)
        self.song.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.artist.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.button.place(relx=0.5, rely=0.7, anchor=CENTER)

    def tag_changer(self):
        file = (self.entry_name_of_the_file.get() + ".mp3")
        metadata_changer(file, self.song.get(), self.artist.get())
        cleaner(self.entry_name_of_the_file.get())
        self.clean()
        # self.again()

    def clean(self):
        self.l1.place_forget()
        self.l2.place_forget()
        self.song.place_forget()
        self.artist.place_forget()
        self.button.place_forget()
        self.butt_hole.place(relx=0.5, rely=0.5, anchor=CENTER)

    def close_window(self):
        window.destroy()

    def config(self, sth):
            sth.config(bg="#90e8b5")

    def forget(self,label):
            label.place_forget()



if __name__ == "__main__":

    window = Tk()
    window.title("My Converter")

    icon2 = PhotoImage(file="gowno.png")
    icon = PhotoImage(file="shit.png")
    img = icon.subsample(1, 1)

    convert = Converter(window)
    window.config(background="#cae6d6")
    window.maxsize(500, 400)
    window.minsize(500, 400)
    window.mainloop()
