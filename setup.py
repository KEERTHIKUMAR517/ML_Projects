from setuptools import find_packages,setup
from typing import List

HYPEN = '-e .'

def get_requirements(file_path:str):

    """This function will return the list of requirements"""

    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if HYPEN in requirements:
            requirements.remove(HYPEN)


setup(
    name = 'ML Projects',
    version = '0.0.1',
    author='keerthi',
    author_email='keerthikumar517@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)