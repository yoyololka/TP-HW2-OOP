from recipes import Ingredient, Recipe
import pytest


def test_ingredient_creation():
    ing = Ingredient("Мука", 500, "г")
    assert ing.name == "Мука"
    assert ing.quantity == 500.0
    assert ing.unit == "г"


def test_ingredient_quantity_becomes_float():
    ing = Ingredient("Яйца", 2, "шт")
    assert isinstance(ing.quantity, float)


def test_ingredient_quantity_zero_raises():
    with pytest.raises(ValueError):
        Ingredient("Мука", 0, "г")


def test_ingredient_quantity_negative_raises():
    with pytest.raises(ValueError):
        Ingredient("Мука", -100, "г")


def test_ingredient_str():
    ing = Ingredient("Мука", 500, "г")
    assert str(ing) == "Мука: 500.0 г"


def test_ingredient_eq_same_name_and_unit():
    ing1 = Ingredient("Мука", 500, "г")
    ing2 = Ingredient("Мука", 200, "г")
    assert ing1 == ing2


def test_ingredient_eq_different_name():
    ing1 = Ingredient("Мука", 500, "г")
    ing2 = Ingredient("Сахар", 500, "г")
    assert ing1 != ing2


def test_ingredient_eq_different_unit():
    ing1 = Ingredient("Молоко", 500, "мл")
    ing2 = Ingredient("Молоко", 500, "г")
    assert ing1 != ing2


def test_recipe_creation():
    recipe = Recipe("Пицца", [])
    assert recipe.title == "Пицца"
    assert recipe.ingredients == []


def test_recipe_add_new_ingredient():
    recipe = Recipe("Пицца")
    ing = Ingredient("Мука", 500, "г")
    recipe.add_ingredient(ing)
    assert len(recipe) == 1


def test_recipe_add_duplicate_ingredient_sums_quantity():
    recipe = Recipe("Пицца")
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    recipe.add_ingredient(Ingredient("Мука", 200, "г"))
    assert len(recipe) == 1
    assert recipe.ingredients[0].quantity == 700.0


def test_recipe_scale_returns_new_object():
    recipe = Recipe("Пицца")
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    scaled = recipe.scale(2)
    assert scaled is not recipe


def test_recipe_scale_multiplies_quantity():
    recipe = Recipe("Пицца")
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    scaled = recipe.scale(2)
    assert scaled.ingredients[0].quantity == 1000.0


def test_recipe_scale_does_not_change_original():
    recipe = Recipe("Пицца")
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    recipe.scale(2)
    assert recipe.ingredients[0].quantity == 500.0


def test_recipe_scale_invalid_ratio_raises():
    recipe = Recipe("Пицца")
    with pytest.raises(ValueError):
        recipe.scale(-1)


def test_recipe_scale_zero_ratio_raises():
    recipe = Recipe("Пицца")
    with pytest.raises(ValueError):
        recipe.scale(0)


def test_recipe_len():
    recipe = Recipe("Пицца")
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    recipe.add_ingredient(Ingredient("Томаты", 200, "г"))
    assert len(recipe) == 2
