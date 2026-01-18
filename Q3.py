def save_error(error, errors=None):
    # Create a fresh list if no list was provided
    if errors is None:
        errors = []

    errors.append(error)
    return errors


# Example usage (multiple calls)
print(save_error("E1"))
print(save_error("E2"))
print(save_error("E3"))
