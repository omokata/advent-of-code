def get_file_content(filepath):
    content = ""
    try:
        with open(filepath, "r") as f:
            content = f.read()
    except OSError as e:
        raise
    return content
