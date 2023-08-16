spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food['name'] for food in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food['heat_level'] > 5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food['name']
        cuisine = food.get('cuisine', 'Unknown')
        spiciness = "🌶" * food['heat_level']

        print(f"{name} ({cuisine}) | Heat Level: {spiciness}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get('cuisine', '').lower() == cuisine.lower():
            return food
    return None

def print_spiciest_foods(spicy_foods):
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)

def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0  # Return 0 for an empty list

    total_heat = sum(food['heat_level'] for food in spicy_foods)
    average = total_heat / len(spicy_foods)
    return int(average)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
