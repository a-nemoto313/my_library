from setuptools import setup

version = {}
with open('./my_package/__version__.py') as f:
    exec(f.read(), version)


setup(
    name="MyLibrary",
    version=version["__version__"],
    description="This is test library.",
    url="https://github.com/a-nemoto313/my_library",
    packages=["my_package"],
)
