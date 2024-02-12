# Python Meetings

The following is a series of steps to consider for our meetings on Python topics. Besides the theoretical knowledge 
we will cover some practical cases in live coding. Observe the practices of this guide:

### Set environment

The right way to work with Python project is to create environments for each project. I suggest to go for one of the 
following:
1. Create a `conda` environment
2. Create a virtual `venv` environment

The suggested Pyton version for the environments is `3.9.X`. **Note**: Make sure you activate the environment to 
work on it

### Choose IDE

Choose a nice IDE and get familiar with it. The IDE provides comprehensive facilities for software development. It
makes nicer the experience of sharing code. I have used (and recommend) the following two:
1. The universal `VS Code`
2. A Python specific IDE `PyCharm`

### Use Notebooks

Python coding experience might be more enjoyable if we use a `Jupyter` notebooks. Please, enable `jupyter` notebooks
in your environments (or projects) to share the code and make nicer outputs when possible. 

Save your work using a naming convention. For example: `YYYYMMDD_python_class.ipynb` for the class held on 
`YYYY-MM-DD` day.

**Note**: Both of the mentioned IDE supports the use of `Jupyter` notebooks natively. They don't need the web browser
to be running. Enable this features if possible.

### Directory structure

For the Python classes I suggest to use the following directory structure.

```
└─── __docs__
    |+-- notes_on_class.txt
    |+-- references.txt
└─── data
    |+-- file_1.txt
    |+-- data_set.csv
    |+-- summary.xml
    |+-- phonebook.json
└─── notebooks
    | +-- 20240201_python_class.ipyn
    | +-- 20240201_python_class.ipyn
└─── scripts
    |+-- __init__.py
    |+-- 20240201_python_class.py
    |+-- 20240202_python_class.py
└─── test
    | +-- __init__.py
    | +-- test_application_1.py
    | +-- test_application_2.py
|+-- environment.yml
|+-- README.md
|+-- .env
```

where:
- `__docs` is a directory to store notes, references, or any other sort of complementary information for the classes.
- `data` is a directory to store files (any format) that will be called by a notebook, script or test in the python 
  classes.
- `notebooks` the directory with the `Jupyter` notebooks corresponding to the class.
- `scripts` the python module with the scripts correspondig to the classes. **Note**: The empty file `__init__.py` 
   makes the scripts exportables.
- `test` directory to test some functions or scripts. It follows the `pytest` framework.
- `environment.yml` is the environment requirements to reproduce code. **Note**: I use `.yml` for my `conda` 
   environments.
- `README.md` a readme file indicating the least amount of instructions to run your project.
- `.env` a environment variable file. This is defined scope level and contains sensible data.