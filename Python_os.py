import os

# Mengganti direktori kerja
os.chdir('/path/to/directory')

# Membuat direktori
os.mkdir('new_directory')

# Membuat beberapa direktori bersamaan
os.makedirs('dir1/dir2/dir3')

# Menghapus file atau direktori
os.remove('file.txt')
os.rmdir('empty_directory')

# Mengecek apakah file atau direktori ada
if os.path.exists('file.txt'):
    print("File ada!")

# Menjalankan perintah shell
os.system('cls')
