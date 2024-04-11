from tkinter import *
import os, ctypes
from work import work

def start():
    def createDir():
        password = passwordEntry.get()
        attempt = attemptEntry.get()
        help = helpTextbox.get('1.0', END)

        try:
            os.mkdir('topSecret')
            ctypes.windll.kernel32.SetFileAttributesW('topSecret', 2)

            with open('topSecret/info.txt', 'w') as file:
                file.write('Статус программы, пароль, количество попыток, подсказка\n')
                file.write('work\n')
                file.write(f'{password}\n')
                file.write(f'{attempt}\n')
                file.write(help)

        except FileExistsError:
            pass

        head.destroy()

        passwordLabel.destroy()
        passwordFrame.destroy()

        attemptLabel.destroy()
        attemptFrame.destroy()

        helpLabel.destroy()
        helpFrame.destroy()

        startButton.destroy()
        discriptionFrame.destroy()

        work()


    head = Label(text='Создание новой скрытой папки', font='Consolas 18 bold italic', bg='#f8b195', fg='#355c7d')
    head.pack()

    # PASSWORD
    passwordLabel = Label(text='Задайте пароль', font='Consolas 15', bg='#f8b195')
    passwordLabel.place(relx=0.025, rely=0.1)

    passwordFrame = Frame(width=35, relief=RIDGE, bd=4, bg='#6c5b7b')
    passwordFrame.place(relx=0.025, rely=0.17)

    passwordEntry = Entry(passwordFrame, width=49, bg='#E6E6FA', relief=FLAT)
    passwordEntry.pack()

    # ATTEMPT
    attemptLabel = Label(text='Задайте количество попыток', font='Consolas 15', bg='#f8b195')
    attemptLabel.place(relx=0.025, rely=0.24)

    attemptFrame = Frame(width=35, relief=RIDGE, bd=4, bg='#6c5b7b')
    attemptFrame.place(relx=0.025, rely=0.31)

    attemptEntry = Entry(attemptFrame, width=49, bg='#E6E6FA', relief=FLAT)
    attemptEntry.pack()

    # HELP
    helpLabel = Label(text='Придумайте подсказку', font='Consolas 15', bg='#f8b195')
    helpLabel.place(relx=0.025, rely=0.43)

    helpFrame = Frame(width=37, height=5, relief=RIDGE, bd=4, bg='#6c5b7b')
    helpFrame.place(relx=0.025, rely=0.5)

    helpTextbox = Text(helpFrame, width=37, height=5, bg='#E6E6FA')
    helpTextbox.pack()

    # START
    startButton = Button(text='Создать скрытую папку', font='Consolas 13 bold', fg='#6c5b7b', activeforeground='#c06c84',
                         command=createDir)
    startButton.place(relx=0.025, rely=0.8)

    # DISCRIPTION
    discriptionFrame = Frame(width=175, height=222, relief=RIDGE, bd=4, bg='#6c5b7b')
    discriptionFrame.place(relx=0.63, rely=0.17)
    discriptionLabel = Label(discriptionFrame, text=('Нажав кнопку,\nсоздастся скрытая\nпапка, которая\nпокажется только\nпосле введения\nпароля. Изменить\nпароль можно будет\nтолько через\nтекстовый файл\nв самой папке!'), font='Consolas 12 bold', bg='#f3d3d7', width=19, height=11)
    discriptionLabel.pack()
