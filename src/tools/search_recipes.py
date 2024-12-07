from typing import Any, Optional
import json
import random

from emp_agents.models.protocol.decorators import tool_method


@tool_method
def search_recipes(ingredients: list[str]) -> str:
    """
    Searches external recipe databases for recipes matching the provided ingredients and dietary preferences.
    """

    recipes: list[dict[str, Any]] = [
        {
            "name": "Salmon Quinoa Bowl",
            "ingredients": ["salmon", "quinoa", "avocado"],
            "dietary": ["pescatarian", "gluten-free"],
            "instructions": "Assemble quinoa, salmon, and avocado in a bowl.",
        },
        {
            "name": "Vegan Tacos",
            "ingredients": ["tortilla", "black beans", "corn", "avocado"],
            "dietary": ["vegan", "gluten-free"],
            "instructions": "Fill tortillas with black beans, corn, and avocado.",
        },
        {
            "name": "Chicken Caesar Salad",
            "ingredients": ["chicken", "romaine lettuce", "parmesan", "croutons"],
            "dietary": ["gluten-free"],
            "instructions": (
                "Toss chicken, lettuce, parmesan, and croutons with Caesar dressing."
            ),
        },
        {
            "name": "Beef Stir Fry",
            "ingredients": ["beef", "broccoli", "soy sauce", "ginger"],
            "dietary": ["gluten-free"],
            "instructions": "Stir fry beef and broccoli with soy sauce and ginger.",
        },
        {
            "name": "Spaghetti Carbonara",
            "ingredients": ["spaghetti", "eggs", "parmesan", "bacon"],
            "dietary": ["gluten-free"],
            "instructions": "Mix cooked spaghetti with eggs, parmesan, and bacon.",
        },
    ]

    return json.dumps(random.choice(recipes), indent=2)
