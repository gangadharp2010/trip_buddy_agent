
# from mcp.server.fastmcp import FastMCP

# from rag.retriever import search_knowledge

# mcp = FastMCP("Trip Buddy Knowledge Server")


# @mcp.tool()
# def search_travel_knowledge(
#     query: str,
#     top_k: int = 3
# ) -> list:
#     """
#     Search travel knowledge documents.

#     Args:
#         query: Travel-related question.
#         top_k: Maximum number of relevant documents.
#     """
#     return search_knowledge(
#         query=query,
#         top_k=top_k
#     )


# if __name__ == "__main__":
#     mcp.run(transport="stdio")

import sys
import logging
from pathlib import Path

# Add project root to Python import path
BASE_DIR = Path(__file__).resolve().parent.parent

if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from mcp.server.fastmcp import FastMCP
from rag.retriever import search_knowledge

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stderr
)

mcp = FastMCP("Trip Buddy Knowledge Server")


@mcp.tool()
def search_travel_knowledge(query: str, top_k: int = 3) -> list:
    """Search travel knowledge documents using RAG."""
    logging.info("Searching travel knowledge: %s", query)

    return search_knowledge(
        query=query,
        top_k=top_k
    )


if __name__ == "__main__":
    logging.info("Starting Knowledge MCP Server")
    mcp.run(transport="stdio")