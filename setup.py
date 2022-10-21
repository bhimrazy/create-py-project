from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read()

setup(
    name="create-py-project-by-bhimrazy",
    version="0.1.0",
    author="Bhimraj Yadav",
    author_email="bhimrajyadav977@gmail.com",
    description="A  CLI tool to scaffold python projects. Generate flask, FastAPI, Django, Ml/DL,etc projects using this tool.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bhimrazy/create-py-project",
    packages=find_packages(),
    py_modules=["main"],
    install_requires=[requirements],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points="""
        [console_scripts]
        create-py-project=create_py_project.main:main
    """,
    python_requires=">=3.6",
)
