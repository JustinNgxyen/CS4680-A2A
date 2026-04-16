async def handle_task(request) -> str:
    text_parts = [p.text for p in request.message.parts if p.type == 'text']
    combined = ' '.join(text_parts)

    if combined.lower().startswith("!summarise"):
        return "This is a short summary of the provided text."

    return combined

def handle_task_sync(request) -> str:
    """Synchronous wrapper for use in Agent Engine (no event loop needed)."""
    text_parts = [p.text for p in request.message.parts if p.type == 'text']
    combined = ' '.join(text_parts)

    if combined.lower().startswith("!summarise"):
        return "This is a short summary of the provided text."

    return combined