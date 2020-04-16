from tkinter import filedialog, messagebox
import os
import shutil


directory_path = filedialog.askdirectory()
files = os.listdir(directory_path)
os.chdir(directory_path)
books_path = '/home/maxim/Стільниця/Books'
videos_path = '/home/maxim/Відео'
photos_path = '/home/maxim/Зображення'
music_path = '/home/maxim/Музика'
docs_path = '/home/maxim/Документи'

for file in files:
    if file.endswith('.fb2') or file.endswith('.pdf'):
        shutil.move(file, books_path)
    elif file.endswith('.mp4') or file.endswith('.avi'):
        shutil.move(file, videos_path)
    elif file.endswith('.jpg') or file.endswith('jpeg') or file.endswith('.png'):
        shutil.move(file, photos_path)
    elif file.endswith('.mp3') or file.endswith('.wav'):
        shutil.move(file, music_path)
    elif (file.endswith('.docx')
          or file.endswith('.xlsx')
          or file.endswith('.pptx')
          or file.endswith('.doc')
          or file.endswith('.txt')):
        shutil.move(file, docs_path)
messagebox.showinfo(title='Success!', message='You folder has been sorted!')
