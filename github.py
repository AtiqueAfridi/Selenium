import os
import subprocess

def git_push(repo_path, branch_name, commit_message="Automatic commit"):
    """
    Automatically adds, commits, and pushes changes to a Git repository.

    Args:
        repo_path (str): The path to the local Git repository.
        branch_name (str): The name of the branch to push.
        commit_message (str): The commit message to use.
    """
    try:
        # Change the current working directory to the repository path
        os.chdir(repo_path)

        # Add all changes
        subprocess.run(["git", "add", "."], check=True, capture_output=True, text=True)

        # Commit changes
        subprocess.run(["git", "commit", "-m", commit_message], check=True, capture_output=True, text=True)

        # Push changes to the specified branch
        subprocess.run(["git", "push", "origin", branch_name], check=True, capture_output=True, text=True)

        print(f"Git push to branch '{branch_name}' successful!")

    except subprocess.CalledProcessError as e:
        print(f"Git push failed: {e.stderr}")
    except FileNotFoundError:
        print(f"Error: Git command not found. Ensure Git is installed and in your PATH.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    repo_path = r"D:\Selenium"  # Use raw string for Windows paths
    branch_name = "selenium_practice" #The branch to push to.
    commit_message = input("Enter your commit message (or leave blank for default): ")
    if not commit_message:
        commit_message = "Automatic commit" #default commit message.
    git_push(repo_path, branch_name, commit_message)