# Baca konten dari program.py
with open('program.py', 'r') as file:
    program_content = file.read()

# Proses obfuskasi sederhana
obfuscated_content = ''.join([f"\\x{ord(char):02x}" for char in program_content])

# Simpan konten yang telah dienkripsi ke dalam file program_encrypted.py
with open('program_encrypted.py', 'w') as file:
    file.write("# Encrypted content - do not modify\n")
    file.write("exec('''" + obfuscated_content + "''')")

# Eksekusi file yang telah dienkripsi
exec(open('program_encrypted.py').read())
