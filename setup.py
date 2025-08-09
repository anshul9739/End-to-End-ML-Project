# from setuptools import find_packages,setup
# from typing import List


# HYPHEN_E_DOT = '-e .'
# def get_requirements(file_path:str)->List[str]:

#     requirements = []
#     with open(file_path) as file_obj:
#         requirements=file_obj.readlines()
#         requirements=[req.replace("\n", "")for req in requirements.txt]
       
       
#         if HYPHEN_E_DOT in requirements:
#             requirements.remove(HYPHEN_E_DOT)   
    
#     return requirements



# setup(
#     name='MLProject',
#     version='0.0.1',    
#     author='Anshul',
#     author_email='anshul9739@gmail.com',
#     packages=find_packages(),
#     install_requires = get_requirements('requirements.txt')

# )


from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    with open(file_path, "r", encoding="utf-8") as f:
        reqs = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    if HYPHEN_E_DOT in reqs:
        reqs.remove(HYPHEN_E_DOT)
    return reqs

setup(
    name="MLProject",
    version="0.0.1",
    author="Anshul",
    author_email="anshul9739@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
