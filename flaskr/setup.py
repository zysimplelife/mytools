from setuptools import setup

setup(
    name='flaskr',
    package=['flaskr'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    test_requre=[
        'pytest',
    ],
)