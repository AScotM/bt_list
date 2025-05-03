#!/usr/bin/env python3

import subprocess
import logging

# Configure logging
logging.basicConfig(filename='bt_list.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_installed_packages():
    """Get a list of installed pip packages and log them."""
    try:
        result = subprocess.run(['pip3', 'freeze'], capture_output=True, text=True, check=True)
        installed_packages = result.stdout.splitlines()

        print("Installed pip packages:")
        for package in installed_packages:
            print(f"  {package}")
            logging.info(f"Installed package: {package}")

    except subprocess.CalledProcessError as e:
        logging.error(f"Error retrieving packages: {e}")
        print(f"Error retrieving packages: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    get_installed_packages()
