from recipes import Ingredient
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
