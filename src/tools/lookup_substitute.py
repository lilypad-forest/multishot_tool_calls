from enum import StrEnum

from emp_agents.models.protocol.decorators import tool_method


class Ingredient(StrEnum):
    BAKING_POWDER = "baking powder"
    BUTTERMILK = "buttermilk"
    CORNSTARCH = "cornstarch"
    HEAVY_CREAM = "heavy cream"
    HONEY = "honey"
    LEMON_JUICE = "lemon juice"
    MAYONNAISE = "mayonnaise"
    MOLASSES = "molasses"
    SOUR_CREAM = "sour cream"
    SOY_SAUCE = "soy sauce"


@tool_method
def lookup_substitute(ingredient: Ingredient) -> str:
    """
    Looks up substitutes for a given ingredient from external resources.
    """

    substitutes: dict[Ingredient, str] = {
        Ingredient.BAKING_POWDER: (
            "Combine 1/2 teaspoon cream of tartar with 1/4 teaspoon baking soda."
        ),
        Ingredient.BUTTERMILK: (
            "Use 1 cup of plain yogurt or 1 cup of milk with 1 tablespoon of lemon"
            " juice or vinegar."
        ),
        Ingredient.CORNSTARCH: (
            "Use 2 tablespoons of all-purpose flour for every 1 tablespoon of"
            " cornstarch."
        ),
        Ingredient.HEAVY_CREAM: "Use 3/4 cup of milk and 1/3 cup of butter.",
        Ingredient.HONEY: "Use 1 cup of sugar and 1/4 cup of water.",
        Ingredient.LEMON_JUICE: (
            "Use 1/2 teaspoon of vinegar for every teaspoon of lemon juice."
        ),
        Ingredient.MAYONNAISE: "Use an equal amount of plain yogurt or sour cream.",
        Ingredient.MOLASSES: "Use 1 cup of honey or 3/4 cup of brown sugar.",
        Ingredient.SOUR_CREAM: "Use an equal amount of plain yogurt.",
        Ingredient.SOY_SAUCE: "Use an equal amount of tamari or coconut aminos.",
    }

    return substitutes.get(
        ingredient, f"Sorry, I couldn't find a substitute for '{ingredient}'."
    )
