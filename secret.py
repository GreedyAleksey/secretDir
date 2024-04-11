from tkinter import *
from begin import start
from work import work

window = Tk()
window.title('Доступ к секретной папке')
window.geometry('550x400+600+250')
window.resizable(False, False)
#f8b195  #f67290  #c06c84  #6c5b7b  #355c7d
window['bg'] = '#f8b195'

try:
    with open('topSecret/info.txt', 'r') as file:
        if file.readlines()[1][:-1]=='work':
            work()
except FileNotFoundError:
    start()

window.mainloop()