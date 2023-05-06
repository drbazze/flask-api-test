import pytest
from src import create_server

@pytest.fixture(scope='module')
def test_client():
    """
    Creates a Flask app client configured for testing
    """
    flask_app = create_server()
    flask_app.config.from_object('config.TestingConfig')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!

@pytest.fixture(scope='module')
def cli_test_client():
    """
    Creates a Flask cli app client configured for testing
    """
    flask_app = create_server()
    flask_app.config.from_object('config.TestingConfig')

    runner = flask_app.test_cli_runner()

    yield runner  # this is where the testing happens!
