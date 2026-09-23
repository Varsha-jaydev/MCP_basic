from mcp.server.mcpserver import MCPServer


server = MCPServer(
    "Notes MCP Server",
)


@server.tool()
def hello(name: str) -> str:
    """
    Say hello to a person.

    Args:
        name: The person's name.
    """

    return f"Hello, {name}! Welcome to MCP."


@server.tool()
def create_note(
    title: str,
    content: str,
) -> dict:
    """
    Create a note.

    Args:
        title: The title of the note.
        content: The content of the note.
    """

    if not title.strip():
        raise ValueError("Title cannot be empty.")

    if not content.strip():
        raise ValueError("Content cannot be empty.")

    return {
        "id": 1,
        "title": title,
        "content": content,
    }


if __name__ == "__main__":
    server.run()
