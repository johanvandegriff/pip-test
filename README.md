# pip-test
This is an example python pip package to show how you can turn your code into a format that is easy to distribute. It covers the bare minimum, so after you are done, check out [this guide](https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python-pypi-packaging/) or any of the many guides online to create pip packages.
## Install
Use one of the methods below to install this example pip package.
### From Release
```bash
wget https://github.com/johanvandegriff/pip-test/releases/download/v0.1.0/pip_test-0.1.0.tar.gz
pip install pip_test-0.1.0.tar.gz
```
### From Source
```bash
git clone https://github.com/johanvandegriff/pip-test.git
cd pip-test
pip install .
```
## Use
After installing, you can run the python console or make a `.py` file and import the package.
```bash
$ python
Type "help", "copyright", "credits" or "license" for more information.
>>> from pip_test import MyClass
>>> c = MyClass()
>>> c.get_versions()
numpy: 1.21.2
scipy: 1.7.1
>>> 
>>> from pip_test import my_function
>>> my_function()
numpy: 1.21.2
scipy: 1.7.1
>>> 
```
## Modify
This section covers how to modify this repo to create your own pip package. We will review each file, what it does, and what you need to change. Here is the entire project's directory structure:
```
$ tree pip-test

pip-test/
├── LICENSE
├── setup.py
└── pip_test
    ├── some_code.py
    └── __init__.py
```

---

`LICENSE` contains the software license for the project, for example the MIT license. Make sure to replace my name in the license with yours, or you can replace the whole thing with a different license.
 
---

`setup.py` contains info about the package version, author, dependencies, etc. In this example, our dependencies are the `numpy` and `scipy` packages. When making your own package, be sure to change all the values in this file.

---

The `pip_test` directory is the name of the package that people will import after installing the pip package. Rename this to your package name.

---

`pip_test/some_code.py` contains the actual code of the package. All the code in the example one is just to show that you can create whatever functions and classes you want in your package:
```python
import numpy
import scipy

def my_function():
  print("numpy:", numpy.__version__)
  print("scipy:", scipy.__version__)

class MyClass():
  def get_versions(self):
    my_function()
```
Replace this with your actual code you want to distruibute in the pip package.

---

`pip_test/__init__.py` contains some basic info about the package, which is duplicate info from `setup.py`. It also contains a very important line at the end:
```python
from pip_test.some_code import my_function, MyClass
```
This imports all the functions and classes you want to expose from `some_code.py` to the user
## Build
### Test
Once you are done modifying these files, run `pip install .` from inside the project directory to install the pip package. Then you can import it from any python file.
### Actual
Once you are happy with your build from `pip install .`, you can build the project into a `.tar.gz` archive. First, check if there are any problems with:
```bash
python setup.py check
```

If the check doesn't display any problems, it passed. Then run this command to build the archive:
```bash
python setup.py sdist
```

It will create a folder called `dist` with a file inside called `pip_test-0.1.0.tar.gz` or similar, depending on your package name and version.
## Upload
### Test
#TODO how to upload to test.pypi.org
### Actual
#TODO how to upload to pypi.org
