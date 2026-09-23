import asyncio

from mcp import Client, StdioServerParameters


async def main() -> None:
    server = StdioServerParameters(
        command="python",
        args=[
            "-m",
            "server.server",
        ],
    )

    async with Client(server) as client:

        print("\nConnected to MCP server!")

        # -------------------------------
        # DISCOVER TOOLS
        # -------------------------------

        result = await client.list_tools()

        print("\nAvailable tools:")

        for tool in result.tools:
            print(f"- {tool.name}")


        print("\nCreating note...")

        result = await client.call_tool(
            "create_note",
            {
                "title": "Learn MCP",
                "content": (
                    "I am learning how MCP "
                    "clients and servers communicate."
                ),
            },
        )

        print("\nCreated note:")

        print(result)


if __name__ == "__main__":
    asyncio.run(main())
