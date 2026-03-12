from setuptools import find_packages, setup

def get_requirements(file_path):
    """Read requirements.txt and return a clean list of packages"""
    with open(file_path) as f:
        requirements = f.read().splitlines()
    
    # Remove '-e .' if it exists
    if "-e ." in requirements:
        requirements.remove("-e .")
    
    return requirements

setup(
    name="financial_churn_mlops_project",
    version="0.0.1",
    author="Amareswari Potu",
    author_email="amareswaripotu123@gmail.com",
    packages=find_packages(),        # automatically find packages in src or project folder
    install_requires=get_requirements("requirements.txt"),
)