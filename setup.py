import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ercot_pylib',
    version='1.0.0',
    author='Matthew McCollom',
    author_email='matthew@mccollom.info',
    description="ERCOT MIS integration for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mmccollom/ercot_mis_pylib',
    project_urls={
        "Bug Tracker": "https://github.com/mmccollom/ercot_mis_pylib/issues"
    },
    packages=['ercot_pylib'],
    install_requires=['requests>=2.5.0'],
)