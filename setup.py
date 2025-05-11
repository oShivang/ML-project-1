from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->list[str]:
    '''
    this function returns the list of requrements
    '''
    requirements=[]
    with open (file_path) as ff:
        requirements=ff.readlines()
        requirements=[r.replace('\n','')for r in requirements]
        hh='-e .'
        if hh in requirements:
            requirements.remove(hh)
        return requirements

setup(name='project1',version='0.0.1',author='SHIVANG KARTHIKEY',author_email='shivangkarthikey188@gmail.com',packages=find_packages(),
      install_requires=get_requirements('requirements.txt'))