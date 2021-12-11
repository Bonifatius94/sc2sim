from setuptools import setup

def load_pip_dependency_list():
    with open('./requirements.txt', 'r', encoding='utf-8') as file:
        return file.read().splitlines()

def load_readme_desc():
    with open("README.md", "r", encoding="utf-8") as readme_file:
        return readme_file.read()

setup(
    name="sc2sim",
    version="1.0.0",
    author="Marco Tröster",
    author_email="marco@troester-gmbh.de",
    description="A StarCraft II environment for reinforcement learning purposes",
    long_description=load_readme_desc(),
    long_description_content_type="text/markdown",
    url="https://github.com/Bonifatius94/sc2sim",
    packages=["sc2sim"],
    python_requires=">=3",
    install_requires=load_pip_dependency_list()
)
