from setuptools import find_packages, setup
from typing import List


# Function to read the requirements file
def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    # Use 'with open' for safe file handling
    with open(file_path) as file_obj:
        # Read all lines
        requirements = file_obj.readlines()

        # Clean up the list by removing the newline character ('\n')
        requirements = [req.replace("\n", "") for req in requirements]

        # Critical step: remove the editable install marker if present
        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements


setup(
    # ------------------------------------------------------------------
    # !!! YOU MUST CUSTOMIZE THESE LINES WITH YOUR PROJECT'S DETAILS !!!
    # ------------------------------------------------------------------
    name='mlproject',
    version='0.0.1',
    author='Kaibalya',
    author_email='kaibalyaprasadjena81@gmail.com',

    # ------------------------------------------------------------------

    # This automatically discovers your 'src' folder as a package
    packages=find_packages(),

    # Install the packages from your requirements file
    # Ensure your file is named 'requirements.txt'
    install_requires=get_requirements('requirements.txt'),
)