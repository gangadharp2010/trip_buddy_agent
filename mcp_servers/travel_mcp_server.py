
import sys
from pathlib import Path

# Add project root to Python import path
BASE_DIR = Path(__file__).resolve().parent.parent

if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from mcp.server.fastmcp import FastMCP

from tools.travel_tools import (
    list_destinations,
    estimate_trip,
    compare_budget
)

mcp = FastMCP("Trip Buddy Travel Server")


@mcp.tool()
def get_destinations() -> list:
    """Retrieve all available travel destinations."""
    return list_destinations()


@mcp.tool()
def calculate_trip_cost(
    destination: str,
    friends: int,
    nights: int,
    budget_per_person: float = None
) -> dict:
    """Calculate estimated trip cost."""

    return estimate_trip(
        destination=destination,
        friends=friends,
        nights=nights,
        budget_per_person=budget_per_person
    )


@mcp.tool()
def find_destinations_by_budget(
    budget_per_person: float,
    friends: int,
    nights: int
) -> list:
    """Find destinations within the specified budget."""

    return compare_budget(
        budget_per_person=budget_per_person,
        friends=friends,
        nights=nights
    )


if __name__ == "__main__":
    mcp.run(transport="stdio")