from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()  #read lines from the file.
            for line in lines:
                requirement=line.strip()  #process each line
                if requirement and requirement!= '-e .':    #ignore empty line ans e .
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="Network Security",
    version="0.0.1",
    author="Upasana Patra",
    author_email="upasanapatra24@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
    
)

