import os
from groq import Groq
from fastmcp import FastMCP


mcp = FastMCP("Calculator")

# Tools:
@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers.
    Args: a(float): first number
          b(float): second number.
    return float: product of two numbers.
          """
    return a * b

@mcp.tool(
    name="Add",
    description="Add two numbers.",
    tags=['math', 'calculator', 'arithmetic']
)
def add(a: int, b: int)-> int:
    return a + b

if __name__ == "__main__":
    mcp.run()
