"""deliberately bad entry: no FastMCP import/instance, no @server.tool()"""


class NotRealServer:
    """This file intentionally does NOT import FastMCP and does NOT declare tools,
    so PYTHON_ENTRY_NO_FASTMCP_SERVER and PYTHON_ENTRY_NO_TOOL_DECLARED both fire."""
