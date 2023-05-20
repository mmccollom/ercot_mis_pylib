import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ercotutils',
    version='1.0.0',
    author='Matthew McCollom',
    author_email='matthewmccollom1989@gmail.com',
    description="ERCOT utils for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mmccollom/ercot_mis_pylib',
    project_urls={
        "Bug Tracker": "https://github.com/mmccollom/ercot_mis_pylib/issues"
    },
    install_requires=['requests>=2.5.0'],
)