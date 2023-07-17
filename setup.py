from setuptools import find_packages, setup
from typing import List

HYP_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    get_requirements function returns a list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n", "") for req in requirements]

        if HYP_E_DOT in requirements:
            requirements.remove(HYP_E_DOT)
        
    return requirements

setup(
    name="mlproject",
    version="0.0.0",
    author="Mohit",
    author_email="mkbhagat50.mb@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)