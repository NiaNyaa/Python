global_var = 20  # Variabel global

def ubah_global_var():
    global global_var
    global_var = 30 

ubah_global_var()  

print("Nilai dari global_var setelah diubah:", global_var)
