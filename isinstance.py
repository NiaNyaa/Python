class Hewan:
    pass

class Kucing(Hewan):
    pass

class Anjing(Hewan):
    pass

kucing = Kucing()
anjing = Anjing()

# Memeriksa apakah kucing adalah instance dari class Kucing
print(isinstance(kucing, Kucing))  # True

# Memeriksa apakah kucing adalah instance dari class Hewan
print(isinstance(kucing, Hewan))  # True, karena Kucing mewarisi class Hewan

# Memeriksa apakah anjing adalah instance dari class Kucing
print(isinstance(anjing, Kucing))  # False, karena Anjing tidak mewarisi class Kucing

# Memeriksa apakah anjing adalah instance dari salah satu class dalam tuple
print(isinstance(anjing, (Kucing, Anjing)))  # True, karena Anjing ada di dalam tuple class
