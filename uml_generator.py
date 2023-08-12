def generate_class_diagram(class_name, properties):
    max_length = max(len(class_name), max(len(prop) for prop in properties)) + 2
    diagram = f"+{'=' * max_length}+\n"
    diagram += f"| {class_name}{' ' * (max_length - len(class_name) - 1)} |\n"
    diagram += f"+{'-' * max_length}+\n"

    for prop in properties:
        diagram += f"| {prop}{' ' * (max_length - len(prop) - 1)} |\n"

    diagram += f"+{'=' * max_length}+\n"

    return diagram


class_name = "ClassName"
properties = ["+<<get, set>> Description : string", "+<<get>> -<<set>> Id : int"]

diagram = generate_class_diagram(class_name, properties)
print(diagram)
