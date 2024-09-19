import random
import os

# File paths
PROJECTS_FILE = 'projects.txt'  # File containing the projects
CACHE_FILE = 'accessed_projects_cache.txt'  # Cache file for accessed projects

def load_projects():
    """Load projects from the main file."""
    if not os.path.exists(PROJECTS_FILE):
        print(f"Error: {PROJECTS_FILE} does not exist.")
        return []

    with open(PROJECTS_FILE, 'r') as f:
        projects = [line.strip() for line in f if line.strip()]
    return projects

def load_accessed_projects():
    """Load accessed projects from the cache file."""
    if not os.path.exists(CACHE_FILE):
        return []

    with open(CACHE_FILE, 'r') as f:
        accessed_projects = [line.strip() for line in f if line.strip()]
    return accessed_projects

def save_accessed_project(project):
    """Save an accessed project to the cache file."""
    with open(CACHE_FILE, 'a') as f:
        f.write(f"{project}\n")

def get_random_project():
    """Get a random project that hasn't been accessed yet."""
    projects = load_projects()
    accessed_projects = load_accessed_projects()
    
    # Get the list of unaccessed projects
    unaccessed_projects = list(set(projects) - set(accessed_projects))

    if not unaccessed_projects:
        print("All projects have been accessed.")
        return None

    # Select a random project
    selected_project = random.choice(unaccessed_projects)

    # Save the accessed project to cache
    save_accessed_project(selected_project)

    return selected_project

def main():
    project = get_random_project()
    if project:
        print(f"Your random project: {project}")
    else:
        print("No new projects to display.")

if __name__ == '__main__':
    main()
