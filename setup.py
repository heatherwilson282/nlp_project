from setuptools import setup, find_namespace_packages

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name='nlp',
    version='0.0.1',
    author='Heather Wilson, Vera Patricio',
    description=' ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/heatherwilson282/nlp_project',
    packages=find_namespace_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'configparser',
        'matplotlib',
        'numpy',
        'pandas',
        'scikit-learn',
        'seaborn',
        'black'],
    python_requires='>=3.6',
    zip_safe=False
)
