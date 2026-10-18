
"""Playback logging compatibility without a global logger group."""


async def play_logs(message, streamtype):
    # Keep existing playback handlers compatible.
    return None
