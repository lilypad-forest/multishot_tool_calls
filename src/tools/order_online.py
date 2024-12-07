from datetime import datetime, timedelta
from pydantic import BaseModel, Field
from uuid import uuid4
import random

from emp_agents.models.protocol.decorators import tool_method


class Order(BaseModel):
    order_id: str = Field(default_factory=lambda: str(uuid4()))
    items: list[str]
    estimated_delivery: datetime
    status: str = "PENDING"


@tool_method
def order_ingredients(ingredients: list[str]) -> str:
    """
    Places an online order for the specified ingredients. Delivery in 12-72 hours.
    """
    random_hours = random.randint(12, 72)
    delivery_time = datetime.now() + timedelta(hours=random_hours)

    return Order(items=ingredients, estimated_delivery=delivery_time).model_dump_json(
        indent=2
    )
