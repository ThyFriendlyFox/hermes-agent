"""Cursor ACP provider profile.

cursor-acp uses an external ACP subprocess — NOT the standard transport.
Hermes spawns `cursor-agent acp` and speaks newline-delimited JSON-RPC 2.0
over stdio (the same generic ACP client used for GitHub Copilot ACP).
The profile captures auth + endpoint metadata for registry migration.
"""

from providers import register_provider
from providers.base import ProviderProfile


class CursorACPProfile(ProviderProfile):
    """Cursor ACP — external process, no REST models endpoint."""

    def fetch_models(
        self,
        *,
        api_key: str | None = None,
        timeout: float = 8.0,
    ) -> list[str] | None:
        """Model listing is handled by the ACP subprocess / Cursor subscription."""
        return None


cursor_acp = CursorACPProfile(
    name="cursor-acp",
    aliases=("cursor", "cursor-agent", "cursor-cli", "cursor-agent-acp"),
    api_mode="chat_completions",  # ACP subprocess uses chat_completions routing
    env_vars=(),  # Managed by ACP subprocess
    base_url="acp://cursor",  # ACP internal scheme
    auth_type="external_process",
)

register_provider(cursor_acp)
