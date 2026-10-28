from mcp.server.fastmcp import FastMCP

server = FastMCP("demo")


@server.tool()
def hello(name: str) -> str:
    return f"hello {name}"


if __name__ == "__main__":
    server.run()
