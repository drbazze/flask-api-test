# Python API layer for the blueprint projects
Flask API bluprint project in order to touch the basics of the API development, config management and TDD.

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
flask run
```

### Run the app in debug mode
```
flask run --debug
```

### Changing the environment
```
export CONFIGURATION_SETUP="config.ProductionConfig"
```
Possible config values:
- config.ProductionConfig
- config.DevelopmentConfig (Default)
- config.TestingConfig

## Unit testing
```
pytest -v
```