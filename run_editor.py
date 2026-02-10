import sys
import subprocess
import os

def install_dependencies():
    """
    Checks for requirements.txt and installs dependencies using pip.
    """
    requirements_file = os.path.join(os.path.dirname(__file__), "requirements.txt")
    
    if not os.path.exists(requirements_file):
        print(f"Warning: {requirements_file} not found. Skipping dependency check.")
        return

    print("--- Checking and installing dependencies ---")
    try:
        # Run pip install -r requirements.txt
        # This will automatically check if packages are already installed and skip them if so.
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", requirements_file],
            stdout=sys.stdout,
            stderr=sys.stderr
        )
        print("--- Dependencies check complete ---")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to install dependencies. Exit code: {e.returncode}")
        # We might want to continue or exit depending on severity. 
        # For now, we pause to let user see the error.
        input("Press Enter to exit...")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error during dependency check: {e}")
        input("Press Enter to exit...")
        sys.exit(1)

def run_application():
    """
    Runs the main application script.
    """
    # Define the path to the main script relative to this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_dir, "codeFile", "json_form_gui.py")

    if not os.path.exists(script_path):
        print(f"Error: Main script not found at {script_path}")
        input("Press Enter to exit...")
        sys.exit(1)

    print(f"--- Launching Character Creator ---")
    print(f"Script: {script_path}")
    
    try:
        # Run the script using the current Python interpreter
        subprocess.run([sys.executable, script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Application exited with error code: {e.returncode}")
    except KeyboardInterrupt:
        print("\nApplication stopped by user.")
    except Exception as e:
        print(f"Error running application: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    install_dependencies()
    run_application()
