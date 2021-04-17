from setuptools import setup, find_packages

def installs(file):
    return [req.strip() for req in open(file).readlines()]


setup(
    name="flask_dash_yaml",
    version="0.1.0",
    description="Flask Framework Yaml",
    packages=find_packages(),
    include_package_data=True,
    install_requires=installs("requeriments.txt"),
    extras_requires= installs("requeriments.txt"),
    package_data = {
        'templates': ['flask_dash_yaml/templates/*'],
        'static': ['flask_dash_yaml/static/*'],
    },
)