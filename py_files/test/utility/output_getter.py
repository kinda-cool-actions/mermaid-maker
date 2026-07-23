def output_getter(output_file: str):
    found_output_vars = {}
    with open(output_file) as file:
        content_lines = file.readlines()
        for line in content_lines:
            key, value = line.split("=")
            found_output_vars[key] = value
    return found_output_vars
