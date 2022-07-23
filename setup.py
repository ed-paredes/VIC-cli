from setuptools import find_packages, setup

setup(
    name='covid_cli',
    packages=find_packages(),
    install_requires=[
        'SQLAlchemy>1.4',
        'pandas',
        'pydantic',
        'pytest',
        'wget',
        'psycopg2-binary',
        'pydantic[dotenv]'
    ],
    entry_points={
        'console_scripts': [
            'vic = src.core.cli:main'
        ]
    }
)