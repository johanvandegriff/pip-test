from setuptools import setup

setup(
    name='pip_test',
    version='0.1.0',
    description='An example Python package',
    url='https://github.com/johanvandegriff/pip-test',
    author='Johan Vandegriff',
    author_email='johan@vandymail.com',
    license='MIT',
    packages=['pip_test'],
    install_requires=['scipy',
                      'numpy',
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
