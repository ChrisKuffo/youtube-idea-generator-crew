from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

# Define the input schema for the custom tool using Pydantic's BaseModel
class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    # Define a field with a description, ensuring the argument is required
    argument: str = Field(..., description="Description of the argument.")

# Define the custom tool class inheriting from BaseTool
class MyCustomTool(BaseTool):
    # Name of the tool, which can be used for identification
    name: str = "Name of my tool"
    # Description of the tool, explaining its purpose and usage
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    # Specify the input schema type for the tool's arguments
    args_schema: Type[BaseModel] = MyCustomToolInput

    # Private method to run the tool's main functionality
    def _run(self, argument: str) -> str:
        # Placeholder for the tool's implementation logic
        # This is where the main processing or action of the tool would occur
        return "this is an example of a tool output, ignore it and move along."