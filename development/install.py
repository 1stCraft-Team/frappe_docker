#!/usr/bin/env python3
import sys
import subprocess
import os

def main():
    # Check if project_name is provided
    if len(sys.argv) < 2:
        print("Error: project_name is required")
        print("Usage: python install.py <project_name> [additional_options]")
        sys.exit(1)

    project_name = sys.argv[1]
    
    # Get any additional arguments after project_name
    additional_args = sys.argv[2:]

    # Construct the arguments for original_installer.py
    args = [
        "python",
        "original_installer.py",
        "-j", f"{project_name}-apps.json",
        "-b", f"frappe-bench-{project_name}",
        "-s", f"{project_name}.localhost",
        "-a", "123"
    ]
    
    # Append any additional arguments
    args.extend(additional_args)

    print(f"Installing Frappe for project: {project_name}")
    print(f"Running: {' '.join(args)}")

    # Call original_installer.py with the constructed arguments
    try:
        result = subprocess.run(args, check=True)
        sys.exit(result.returncode)
    except subprocess.CalledProcessError as e:
        print(f"Error: Installation failed with exit code {e.returncode}")
        sys.exit(e.returncode)
    except FileNotFoundError:
        print("Error: original_installer.py not found in the current directory")
        sys.exit(1)

if __name__ == "__main__":
    main()
