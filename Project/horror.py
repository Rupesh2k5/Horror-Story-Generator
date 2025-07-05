def build_prompt(character, situation, lines):
    return (
        f"Write a horror story with the following:\n"
        f"Character: {character}\n"
        f"Situation: {situation}\n"
        f"Length: {lines} lines\n"
        f"Make it suspenseful, creepy, and with a twist ending."
    )
