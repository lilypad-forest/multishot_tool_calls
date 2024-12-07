from emp_agents.models.protocol import SkillSet

from ..tools import (
    order_ingredients,
    lookup_substitute,
    find_nearby_stores,
    search_recipes,
)


class CulinarySkillSet(SkillSet):
    order_ingredients = order_ingredients
    lookup_substitute = lookup_substitute
    find_nearby_stores = find_nearby_stores
    search_recipes = search_recipes
