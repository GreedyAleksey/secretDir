from tkinter import *
import os, ctypes

def work():
    def getHelp():
        def cl():
            helpLabel.destroy()
            helpFrame.destroy()
            helpButton.config(command=getHelp)

        with open('topSecret/info.txt', 'r') as file:
            helpLabel = Label(text='Подсказка', font='Consolas 15', bg='#f8b195')
            helpLabel.place(relx=0.025, rely=0.43)

            helpFrame = Frame(width=37, height=5, relief=RIDGE, bd=4, bg='#6c5b7b')
            helpFrame.place(relx=0.025, rely=0.5)

            helpTextbox = Text(helpFrame, width=37, height=5, bg='#E6E6FA')
            helpTextbox.insert(END, file.readlines()[4][:-1])
            helpTextbox.config(state=DISABLED)
            helpTextbox.pack()

            helpButton.config(command=cl)


    def checkPassword():
        def deleteAll(directory):
            for root, dirs, files in os.walk(directory, topdown=False):
                for file in files:
                    try:
                        os.remove(os.path.join(root, file))
                        print(f"Deleted file: {os.path.join(root, file)}")
                    except OSError as e:
                        print(f"Error deleting file: {os.path.join(root, file)}, {e}")

                for dir_name in dirs:
                    try:
                        os.rmdir(os.path.join(root, dir_name))
                        print(f"Deleted directory: {os.path.join(root, dir_name)}")
                    except OSError as e:
                        print(f"Error deleting directory: {os.path.join(root, dir_name)}, {e}")

        def deleteMainDirectory(directory):
            os.rmdir(directory)

        pas = passwordEntry.get()

        with open('topSecret/info.txt', 'r') as file:
            f = file.readlines()

            if (f[2])[:-1]==pas:
                ctypes.windll.kernel32.SetFileAttributesW('topSecret', 1)

            else:
                with open('topSecret/info.txt', 'w') as file:
                    label = Label(text=f'Осталось попыток:{f[3][:-1]}', font='Consolas 15', bg='#f8b195')
                    label.place(relx=0.025, rely=0.24)

                    discriptionFrame = Frame(width=175, height=222, relief=RIDGE, bd=4, bg='#6c5b7b')
                    discriptionFrame.place(relx=0.63, rely=0.17)
                    discriptionLabel = Label(discriptionFrame, text=('ВНИМАНИЕ!\nКогда закончатся\nпопытки все файлы\nв папке удалятся!'),
                                             font='Consolas 12 bold', bg='#f3d3d7', width=20, height=11)

                    discriptionLabel.pack()

                    f[3] = str(int((f[3])[:-1])-1)+'\n'
                    label.config(text=f'Осталось попыток:{f[3][:-1]}')

                    for i in f:
                        file.write(i)

        if int((f[3])[:-1]) == 0:
            label.config(text='Все файлы были удалены!')
            file.close()
            deleteAll('topSecret')
            deleteMainDirectory('topSecret')

            head.destroy()
            passwordLabel.destroy()
            passwordFrame.destroy()
            checkButton.destroy()
            hideButton.destroy()
            helpButton.destroy()


    def hide():
        ctypes.windll.kernel32.SetFileAttributesW('topSecret', 2)

    head = Label(text='Управление скрытой папкой', font='Consolas 18 bold italic', bg='#f8b195', fg='#355c7d')
    head.pack()

    # PASSWORD
    passwordLabel = Label(text='Введите пароль от папки', font='Consolas 15', bg='#f8b195')
    passwordLabel.place(relx=0.025, rely=0.1)

    passwordFrame = Frame(width=35, relief=RIDGE, bd=4, bg='#6c5b7b')
    passwordFrame.place(relx=0.025, rely=0.17)

    passwordEntry = Entry(passwordFrame, width=49, bg='#E6E6FA', relief=FLAT)
    passwordEntry.pack()

    #check button
    checkButton = Button(text='Показать папку', font='Consolas 13 bold', fg='#6c5b7b',
                        activeforeground='#c06c84',
                        command=checkPassword)
    checkButton.place(relx=0.025, rely=0.8)

    #hide button
    hideButton = Button(text='Скрыть папку', font='Consolas 13 bold', fg='#6c5b7b',
                        activeforeground='#c06c84', command=hide)
    hideButton.place(relx=0.4, rely=0.8)

    #help button
    helpButton = Button(text='Забыл пароль', font='Consolas 13 bold', fg='#6c5b7b',
                         activeforeground='#c06c84',
                         command=getHelp)
    helpButton.place(relx=0.725, rely=0.8)
