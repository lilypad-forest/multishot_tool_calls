from emp_agents.agents import SkillsAgent
from emp_agents.types import OpenAIModelType

from src.skills import CulinarySkillSet

system_message = """
You are an experienced chef with a passion for creating delicious homemade meals.
You'll be working with your teammate to prepare a meal for Thanksgiving.

You have a set of tools at your disposal, which you may invoke when appropriate.
"""


def init_agent() -> SkillsAgent:
    return SkillsAgent(
        skills=[CulinarySkillSet],
        default_model=OpenAIModelType.gpt4o_mini,
        prompt=system_message,
    )
