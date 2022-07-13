from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="startpage-python",
    version='1.0.0',
    license="GPL-3.0 License",
    description='performing websearch via startpage search engine (based on google.com)',
    py_modules=["startpage"],
    long_description=readme,
    long_description_content_type="text/markdown",
    package_dir={'':'src'},
    url='https://github.com/mohamedkasem99/startpage-python',
    python_requires='>=3.6',
    install_requires=required
)