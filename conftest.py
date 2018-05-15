import pytest
import os

@pytest.fixture()
def reset_app():
    os.system("adb shell pm clear com.hub.mentifi")
