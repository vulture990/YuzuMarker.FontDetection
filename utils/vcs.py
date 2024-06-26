from pathlib import Path
import pygit2

def get_current_tag() -> str:
    repo = pygit2.Repository(Path(__file__).parent.absolute())
    unstaged_changes = False
    for file, val in repo.status().items():
        if val != 1 << 14:
            unstaged_changes = True
            print(f"Unstaged commit detected: {file} with status {val}")
    if unstaged_changes:
        # Optionally raise a warning or handle it differently
        print("Warning: Unstaged changes detected. Proceeding with the current commit.")
    return repo.head.peel().short_id
