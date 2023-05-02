# Python API layer for the blueprint projects
venv is used for managing the dependencies

## Installation
- First you make sure the venv is installed
```
virtualenv --version
```
- Create the virtual environment in the root folder
```
virtualenv venv
```
- Activate the venv
```
source venv/bin/activate
```
- Check if the pip points to this environment
```
pip -V
```
- Install the dependencies
```
pip install -r requirements.txt
```

## Run the project
```
python app.py
```