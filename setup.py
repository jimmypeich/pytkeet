
#==========================#
# PROJECT INFO
#==========================#

PROJECT_NAME = "pytkeet"
PROJECT_DESCRIPTION = "Python common helper utils"
PROJECT_AUTHOR = "jimmypeich"
PROJECT_AUTHOR_EMAIL = "jimmypeich@outlook.com"
PROJECT_URL = ""

# Libraries (and versions) "libname{==><}X.Y.Z"
DEPENDENCIES = [
    "pytz",
]

#==========================#
# BUILD
#==========================#

if __name__ == "__main__":

    import os
    from setuptools import setup, find_packages

    # Read version from module
    version = {}
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), PROJECT_NAME, "version.py")) as vfile:
        exec(vfile.read(), version)

    # Add special modules to the build process
    SETUP_DEPENDENCIES = ["wheel", "sphinx"]

    setup(name=PROJECT_NAME,
          version=version["__version__"],
          description=PROJECT_DESCRIPTION,
          author=PROJECT_AUTHOR,
          author_email=PROJECT_AUTHOR_EMAIL,
          url=PROJECT_URL,
          setup_requires=SETUP_DEPENDENCIES,
          install_requires=DEPENDENCIES,
          test_suite='tests',
          packages=find_packages(exclude=["tests"]),
          classifiers=[],
    )
