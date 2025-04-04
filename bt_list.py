import subprocess
import time
import logging

# Configure logging
logging.basicConfig(filename='bt_list.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Color definitions for spring tones
RESET_COLOR = "\033[0m"
FRESH_GREEN = "\033[38;5;34m"  # Fresh Green
SKY_BLUE = "\033[38;5;45m"     # Sky Blue
SOFT_YELLOW = "\033[38;5;11m"  # Soft Yellow
PASTEL_PINK = "\033[38;5;213m" # Pastel Pink
LIGHT_LAVENDER = "\033[38;5;138m"  # Light Lavender
LIGHT_PEACH = "\033[38;5;220m"   # Light Peach

# Sleep function for a relaxed, spring-like pace
def spring_sleep(seconds):
    """Sleep with a gentle pace, like the breeze of a spring morning."""
    time.sleep(seconds)

def get_installed_packages():
    """Get a list of installed pip packages, with a fresh, spring-inspired output."""
    try:
        # Run the pip freeze command to get installed packages
        result = subprocess.run(['pip3', 'freeze'], capture_output=True, text=True, check=True)
        installed_packages = result.stdout.splitlines()

        # Start the spring-themed sequence of output
        print(FRESH_GREEN + "\n>>> The spring winds are picking up..." + RESET_COLOR)
        spring_sleep(1)

        print(SKY_BLUE + "Gathering the flora of installed packages..." + RESET_COLOR)
        spring_sleep(2)

        print(SOFT_YELLOW + "\nPackage list blooming in the sun...\n" + RESET_COLOR)
        spring_sleep(1)

        # Output the list of packages in a more rhythmic, spring-like manner
        for index, package in enumerate(installed_packages, 1):
            spring_sleep(0.5)  # Gentle pause between each package
            print(PASTEL_PINK + f"  {package}" + RESET_COLOR)

        spring_sleep(1)
        print(LIGHT_LAVENDER + "\nThe petals settle... the list is complete." + RESET_COLOR)

    except subprocess.CalledProcessError as e:
        logging.error(f"Error while retrieving packages: {e}")
        print(f"{LIGHT_PEACH}Error while retrieving packages: {e}{RESET_COLOR}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"{LIGHT_PEACH}Unexpected error: {e}{RESET_COLOR}")

if __name__ == "__main__":
    print(FRESH_GREEN + "\nEntering the spring bloom of Python packages." + RESET_COLOR)
    spring_sleep(2)
    get_installed_packages()
