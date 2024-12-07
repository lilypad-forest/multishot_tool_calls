import uuid
import json

from emp_agents.agents import SkillsAgent
from emp_agents.types import OpenAIModelType
from openai.types.chat import (
    ChatCompletionUserMessageParam,
    ChatCompletionAssistantMessageParam,
    ChatCompletionMessageToolCallParam,
    ChatCompletionMessageParam,
)
from openai.types.chat.chat_completion_message_tool_call_param import Function

from src.skills import CulinarySkillSet

casual_greeting = [
    ChatCompletionUserMessageParam(
        role="user",
        content="Hey, how are you?",
    ),
    ChatCompletionAssistantMessageParam(
        role="assistant",
        content="I'm doing great, thanks for asking!",
    ),
]

store_lookup = [
    ChatCompletionUserMessageParam(
        role="user",
        content="Where's the closest shop for dill?",
    ),
    ChatCompletionAssistantMessageParam(
        role="assistant",
        content="Let's use our store lookup tool to find the closest shop for dill.",
        tool_calls=[
            ChatCompletionMessageToolCallParam(
                id=str(uuid.uuid4()),
                type="function",
                function=Function(
                    name="find_nearby_stores",
                    arguments=json.dumps(
                        {"ingredient": "dill", "location": "Financial District"}
                    ),
                ),
            ),
        ],
    ),
]

online_order = [
    ChatCompletionUserMessageParam(
        role="user",
        content="Can you place an order for 1lbs of salmon and 2lbs of potatoes?",
    ),
    ChatCompletionAssistantMessageParam(
        role="assistant",
        content="Let's invoke our ordering tool and get that done.",
        tool_calls=[
            ChatCompletionMessageToolCallParam(
                id=str(uuid.uuid4()),
                type="function",
                function=Function(
                    name="order_ingredients",
                    arguments=json.dumps(
                        {"ingredients": ["1lbs of salmon", "2lbs of potatoes"]}
                    ),
                ),
            ),
        ],
    ),
]

substitute_lookup = [
    ChatCompletionUserMessageParam(
        role="user",
        content="I need to find a substitute for honey.",
    ),
    ChatCompletionAssistantMessageParam(
        role="assistant",
        content="Let's use our substitute lookup tool to find a substitute for honey.",
        tool_calls=[
            ChatCompletionMessageToolCallParam(
                id=str(uuid.uuid4()),
                type="function",
                function=Function(
                    name="lookup_substitute",
                    arguments=json.dumps({"ingredient": "honey"}),
                ),
            ),
        ],
    ),
]

recipe_lookup = [
    ChatCompletionUserMessageParam(
        role="user",
        content="I need a recipe for mashed potatoes.",
    ),
    ChatCompletionAssistantMessageParam(
        role="assistant",
        content=(
            "Let's use our recipe lookup tool to find a recipe for mashed potatoes."
        ),
        tool_calls=[
            ChatCompletionMessageToolCallParam(
                id=str(uuid.uuid4()),
                type="function",
                function=Function(
                    name="search_recipes",
                    arguments=json.dumps({"recipe": "mashed potatoes"}),
                ),
            ),
        ],
    ),
]


def _format_example(example: list[ChatCompletionMessageParam]) -> str:
    return json.dumps(example, indent=2)


def _format_examples(
    system_message: str, examples: list[list[ChatCompletionMessageParam]]
) -> str:
    return system_message.format(
        examples="\n".join(
            [
                f"<example>\n{_format_example(example)}\n</example>"
                for example in examples
            ]
        )
    )


system_message = """
You are an experienced chef with a passion for creating delicious homemade meals.
You'll be working with your teammate to prepare a meal for Thanksgiving.

You have a set of tools at your disposal, which you may invoke when appropriate.

Here are some examples to help you decide when to use which tool:
<examples>
{examples}
</examples>
"""


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
