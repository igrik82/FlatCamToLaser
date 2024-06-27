def find_min_max_gcode(file_path):
    min_x = float("inf")
    max_x = float("-inf")
    min_y = float("inf")
    max_y = float("-inf")

    with open(file_path, "r") as file:
        for line in file:
            parts = line.split()
            for part in parts:
                if part.startswith("X"):
                    try:
                        x_value = float(part[1:])
                        min_x = min(min_x, x_value)
                        max_x = max(max_x, x_value)
                    except ValueError:
                        continue
                elif part.startswith("Y"):
                    try:
                        y_value = float(part[1:])
                        min_y = min(min_y, y_value)
                        max_y = max(max_y, y_value)
                    except ValueError:
                        continue

    return min_x, max_x, min_y, max_y


# Пример использования
try:
    file_path = (
        "fan_regulator-1.3.gcode"  # Замените на путь к вашему файлу G-code
    )
    min_x, max_x, min_y, max_y = find_min_max_gcode(file_path)
except Exception as e:
    print(e)

print(f"Минимальное значение X: {min_x}")
print(f"Максимальное значение X: {max_x}")
print(f"Минимальное значение Y: {min_y}")
print(f"Максимальное значение Y: {max_y}")
