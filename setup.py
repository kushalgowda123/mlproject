from setuptools import find_packages, setup

from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    Read the requirements.txt file and return a list of dependencies.

    :param file_path: Path to the requirements.txt file
    :return: List of dependencies
    """
    try:
        with open(file_path, 'r') as file_obj:
            requirements = file_obj.readlines()
            # Remove whitespace and newline characters
            requirements = [req.strip() for req in requirements]
            # Remove '-e .' if present
            if '-e .' in requirements:
                requirements.remove('-e .')
            return requirements
    except FileNotFoundError:
        raise Exception(f"Error: {file_path} not found!")

setup(
    name='mlproject',
    version='1.0',
    description='Python Distribution Utilities',
    author='Kushal Gowda',
    author_email='kushalgowda44664@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirments.txt'),
)