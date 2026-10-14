import json
import argparse
from pathlib import Path


def convert_ipynb_to_py(notebook_path: Path) -> None:
    """Converts a single .ipynb file to a .py file."""
    py_path = notebook_path.with_suffix(".py")

    try:
        with open(notebook_path, "r", encoding="utf-8") as f:
            nb_data = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"Failed to read {notebook_path}: {e}")
        return

    py_content = []

    for cell in nb_data.get("cells", []):
        cell_type = cell.get("cell_type")
        source = cell.get("source", [])

        # Standardize source input (list of strings or single string)
        source_text = "".join(source) if isinstance(source, list) else source

        if cell_type == "code":
            py_content.append(source_text)
            py_content.append("\n\n")
        elif cell_type == "markdown":
            # Formats markdown as commented blocks
            commented_md = "\n".join(
                f"# {line}" if line else "#" for line in source_text.splitlines()
            )
            py_content.append(f"# %% [markdown]\n{commented_md}\n\n")

    with open(py_path, "w", encoding="utf-8") as f:
        f.write("".join(py_content))

    print(f"Converted: {notebook_path} -> {py_path}")


def convert_directory(target_dir: str) -> None:
    """Recursively converts all .ipynb files in target_dir and subdirectories."""
    root_path = Path(target_dir)

    if not root_path.is_dir():
        print(f"Error: Directory '{target_dir}' does not exist.")
        return

    # Recursively find all .ipynb files, excluding Jupyter checkpoint folders
    ipynb_files = [
        p for p in root_path.rglob("*.ipynb")
        if ".ipynb_checkpoints" not in p.parts
    ]

    if not ipynb_files:
        print("No .ipynb files found.")
        return

    print(f"Found {len(ipynb_files)} notebook(s). Processing...\n")
    for file in ipynb_files:
        convert_ipynb_to_py(file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Recursively convert Jupyter Notebooks (.ipynb) to Python scripts (.py)."
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Path to the target directory (default: current directory)",
    )
    args = parser.parse_args()

    convert_directory(args.directory)
