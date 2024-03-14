#!/usr/bin/env python
"""
This script is used to push the changes to the git repository in CSV format.
"""
import os
import time


def push_to_git():
    """
    This function is used to push the changes to the git repository.
    """
    os.system("git add .")
    # commit_message = f"Updated files at {
    #     time.strftime('%a %b %d %H:%M:%S %Y')}"
    os.system("git commit -m 'commit_message'")
    # Assuming the branch is 'main', change if necessary
    os.system("git push origin main")
    print("[INFO] --- Pushed the changes to the git repository. ---")


if __name__ == "__main__":
    push_to_git()
