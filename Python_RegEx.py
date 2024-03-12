import re

# Mencocokkan pola digit
pattern = r'\d+'
text = 'There are 123 apples and 456 oranges'
matches = re.findall(pattern, text)
print("Mencocokkan pola digit:")
print(matches)  # Output: ['123', '456']
print()

# Mengganti pola tertentu dengan string lain
new_text = re.sub(pattern, 'X', text)
print("Mengganti pola tertentu:")
print(new_text)  # Output: 'There are X apples and X oranges'
print()

# Mencocokkan pola kata tertentu
pattern_word = r'\b\w{5}\b'  # Mencocokkan kata yang terdiri dari tepat 5 karakter
matches_word = re.findall(pattern_word, text)
print("Mencocokkan pola kata tertentu:")
print(matches_word)  # Output: ['There', 'apples']
