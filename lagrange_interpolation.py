def lagrange_interpolation(x_data, y_data, x):
    """
    Interpolasi polinomial Lagrange.
    
    Args:
    x_data: List of x-coordinates of data points.
    y_data: List of y-coordinates of data points.
    x: The x-coordinate where interpolation is to be evaluated.
    
    Returns:
    Interpolated value at x.
    """
    n = len(x_data)
    interpolated_value = 0
    
    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if j != i:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        interpolated_value += term
    
    return interpolated_value

# Contoh penggunaan
x_data = [1, 2, 3, 4, 5]
y_data = [2, 3, 5, 7, 11]
x_interpolate = 2.5

interpolated_value = lagrange_interpolation(x_data, y_data, x_interpolate)
print("Interpolated value at x =", x_interpolate, ":", interpolated_value)
