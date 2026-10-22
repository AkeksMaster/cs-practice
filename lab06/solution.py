def count_by_extension(paths: list[str]) -> dict[str, int]:
    result = {}

    for path in paths:
        filename = path.split("/")[-1]

        if "." in filename:
            extension = filename.rsplit(".", 1)[1].lower()
        else:
            extension = ""

        result[extension] = result.get(extension, 0) + 1

    return result

def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""

    return sorted(paths, key=lambda path: (-path.count("/"), path))[0]

def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = float(n_bytes)

    for unit in units:
        if size < 1024 or unit == "ТБ":
            if unit == "Б":
                return f"{int(size)} {unit}"
            return f"{size:.1f} {unit}"
        size /= 1024