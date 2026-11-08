# Imports
from fastapi import FastAPI
from fastmcp import FastMCP

# FastAPI App:
app = FastAPI(title = "Calculator APP")

@app.post("/multiply")
def multiply(a: int, b: int) -> int:
    """Multiplies two numbers and returns the result"""

    return a * b

@app.post("/add")
def add(a: int, b: int) -> int:
    """Adds two numbers and returns the result"""

    return a + b

@app.post("/subtract")
def subtract(a: int, b: int) -> int:
    """Subtracts two numbers and returns the result"""

    return a - b

@app.post("/divide")
def divide(a: int, b: int) -> int:
    """Multiplies two numbers and returns the result"""

    return a // b

# Conversion of FastAPI app to MCP:
mcp = FastMCP.from_fastapi(app=app)

if __name__ == "__main__":
    mcp.run(transport="stdio")

mcp.http_app()
