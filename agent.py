"""Minimal ADK agent with one tool. ADK looks for `root_agent`."""
import datetime
from zoneinfo import ZoneInfo

from google.adk.agents import Agent


def get_current_time(timezone: str = "Asia/Kolkata") -> dict:
    """Returns the current time in the given IANA timezone.

    Args:
        timezone: IANA timezone name, e.g. "Asia/Kolkata" or "America/New_York".
    """
    try:
        now = datetime.datetime.now(ZoneInfo(timezone))
    except Exception:
        return {"status": "error", "error_message": f"Unknown timezone: {timezone}"}
    return {"status": "success", "time": now.strftime("%Y-%m-%d %H:%M:%S %Z")}


root_agent = Agent(
    name="my_agent",
    model="gemini-3.8-flash",
    description="A helpful assistant that can tell the current time.",
    instruction=(
        "You are a helpful assistant. When the user asks about the time, "
        "use the get_current_time tool."
    ),
    tools=[get_current_time],
)
