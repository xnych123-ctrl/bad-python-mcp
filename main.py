from mcp.server.fastmcp import FastMCP

mcp = FastMCP("demo")

@mcp.tool()
def hello(name: str) -> str:
    return f"hello {name}"

if __name__ == "__main__":
    mcp.run()
