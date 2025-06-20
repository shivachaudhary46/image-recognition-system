import sys
import os 

# Add the app directory to the system path
sys.path.insert(0, os.path.abspath("app"))

from app import app 

## importing function 
def test_home():
    response=app.test_client().get("/")
    assert response.status_code==200
    assert response.data==b"Hello World"