# Developing Python Applications


## The VS Code development environment

Install the Python extension

Select an interpreter

Install Python 3.9 or Python 3.10


## Create a virtual environment

```sh
> python3.9 -m venv .venv
> 
```

Select this interpreter in VS Code, or activate virtual env if working in terminal.

See <https://code.visualstudio.com/docs/python/environments>


## Python package management

### using pip

```sh
> python3.9 -m pip install --upgrade pip
> python3.9 -m pip install {package}
> python3.9 -m pip freeze  >> requirements.txt
```

```sh
> python3 -m pip install -r requirements.txt
```

Ideally we should use ```pip freeze > requirements.txt``` but this will likely have more packages than are needed.


## Resources

pip <https://pip.pypa.io/en/stable/getting-started/>

wheels <https://realpython.com/python-wheels/>

venv <https://docs.python.org/3/library/venv.html>
