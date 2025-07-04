from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''Returns a list of requirements from the given file'''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

# 🔧 Call the function before setup()
requirements = get_requirements('requirements.txt')

setup(
    name='summarizer',
    version='0.0.1',
    author='Aarav',
    author_email='b23cm1002@iitj.ac.in',
    packages=find_packages(),
    install_requires=requirements
)
