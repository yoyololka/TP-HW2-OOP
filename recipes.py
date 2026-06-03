class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = float(value)

    def __str__(self):
        return f"{self.name}: {self._quantity} {self.unit}"

    def __repr__(self):
        return f"Ingredient('{self.name}', {self._quantity}, '{self.unit}')"

    def __eq__(self, other):
        if not isinstance(other, Ingredient):
            return False
        return self.name == other.name and self.unit == other.unit


class Recipe:
    def __init__(self, title: str, ingredients: list = None):
        self.title = title
        self.ingredients = ingredients if ingredients is not None else []

    def add_ingredient(self, ingredient: Ingredient):
        for ing in self.ingredients:
            if ing == ingredient:
                ing.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        return isinstance(ratio, (int, float)) and ratio > 0

    def scale(self, ratio: float):
        if not Recipe.is_valid_ratio(ratio):
            raise ValueError("Коэффициент должен быть положительным числом")
        new_recipe = Recipe(self.title)
        for ing in self.ingredients:
            new_ingredient = Ingredient(ing.name, ing.quantity * ratio, ing.unit)
            new_recipe.ingredients.append(new_ingredient)
        return new_recipe

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        result = self.title + ":\n"
        for ing in self.ingredients:
            result += "  - " + str(ing) + "\n"
        return result
