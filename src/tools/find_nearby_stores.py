import random
import json

from emp_agents.models.protocol.decorators import tool_method


@tool_method
def find_nearby_stores(ingredient: str, location: str) -> str:
    """
    Finds nearby stores that have the specified ingredient in stock.
    For demonstration, we'll sample from a mock list.
    """

    stores = [
        {"name": "Fresh Market", "address": "123 Main St", "distance": "0.5 miles"},
        {"name": "Gourmet Grocers", "address": "456 Elm St", "distance": "1.2 miles"},
        {"name": "Healthy Harvest", "address": "789 Oak Ave", "distance": "0.8 miles"},
        {"name": "Organic Oasis", "address": "321 Maple Rd", "distance": "2.0 miles"},
        {
            "name": "Local Farmer's Market",
            "address": "654 Pine St",
            "distance": "3.5 miles",
        },
        {"name": "Global Foods", "address": "987 Cedar Blvd", "distance": "2.5 miles"},
        {
            "name": "Neighborhood Mart",
            "address": "246 Birch Ln",
            "distance": "1.0 miles",
        },
        {
            "name": "City Supermarket",
            "address": "135 Spruce Ct",
            "distance": "4.0 miles",
        },
        {"name": "Village Grocer", "address": "864 Willow Dr", "distance": "1.5 miles"},
        {"name": "Downtown Deli", "address": "579 Poplar St", "distance": "0.7 miles"},
    ]

    return json.dumps(random.choice(stores), indent=2)
