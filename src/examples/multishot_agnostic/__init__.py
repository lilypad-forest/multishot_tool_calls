import json

from emp_agents.agents import SkillsAgent
from emp_agents.types import OpenAIModelType

from src.skills import CulinarySkillSet

casual_greeting: list[dict] = [
    {
        "role": "user",
        "content": "Hey, how are you?",
    },
    {
        "role": "assistant",
        "content": "I'm doing great, thanks for asking!",
    },
]

store_lookup: list[dict] = [
    {
        "role": "user",
        "content": "Where's the closest shop for dill?",
    },
    {
        "role": "assistant",
        "content": "Let's use our store lookup tool to find the closest shop for dill.",
        "tool_call": {
            "name": "find_nearby_stores",
            "args": {"ingredient": "dill", "location": "Financial District"},
        },
    },
]

online_order: list[dict] = [
    {
        "role": "user",
        "content": "Can you place an order for 1lbs of salmon and 2lbs of potatoes?",
    },
    {
        "role": "assistant",
        "content": "Let's invoke our ordering tool and get that done.",
        "tool_call": {
            "name": "order_ingredients",
            "args": {
                "ingredients": ["1lbs of salmon", "2lbs of potatoes"],
            },
        },
    },
]

substitute_lookup: list[dict] = [
    {
        "role": "user",
        "content": "I need to find a substitute for honey.",
    },
    {
        "role": "assistant",
        "content": (
            "Let's use our substitute lookup tool to find a substitute for honey."
        ),
        "tool_call": {
            "name": "lookup_substitute",
            "args": {"ingredient": "honey"},
        },
    },
]

recipe_lookup: list[dict] = [
    {
        "role": "user",
        "content": "I need a recipe for mashed potatoes.",
    },
    {
        "role": "assistant",
        "content": (
            "Let's use our recipe lookup tool to find a recipe for mashed potatoes."
        ),
        "tool_call": {
            "name": "search_recipes",
        },
    },
]

system_message = """
You are an experienced chef with a passion for creating delicious homemade meals.
You'll be working with your teammate to prepare a meal for Thanksgiving.

You have a set of tools at your disposal, which you may invoke when appropriate.

Here are some examples to help you decide when to use which tool:
<examples>
{examples}
</examples>
"""


def _format_example(example: list[dict]) -> str:
    return json.dumps(example, indent=2)


def _format_examples(system_message: str, examples: list[list[dict]]) -> str:
    return system_message.format(
        examples="\n".join(
            [
                f"<example>\n{_format_example(example)}\n</example>"
                for example in examples
            ]
        )
    )


def init_agent() -> SkillsAgent:
    return SkillsAgent(
        skills=[CulinarySkillSet],
        default_model=OpenAIModelType.gpt4o_mini,
        prompt=_format_examples(
            system_message,
            [
                casual_greeting,
                store_lookup,
                online_order,
                substitute_lookup,
                recipe_lookup,
            ],
        ),
    )
