def get_formatted_name(first,last,middle=""): #middle name being optional, also takes middle name as last argument?
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

