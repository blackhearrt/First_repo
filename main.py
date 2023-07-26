def format_ingredients(items):
    num_ingredients = len(items)

    # Перевіряємо, чи список не порожній
    if num_ingredients == 0:
        return ""

    # Якщо є лише один інгредієнт, повертаємо його без змін
    if num_ingredients == 1:
        return items[0]

    # Якщо інгредієнтів більше одного, форматуємо список
    formatted_ingredients = ", ".join(items[:-1])  # Об'єднуємо всі елементи, крім останнього

    # Додаємо "and" перед останнім елементом
    formatted_ingredients += " and " + items[-1]

    return formatted_ingredients
    

# Приклад використання:
print(format_ingredients(["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]))

