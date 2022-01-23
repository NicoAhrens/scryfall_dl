import subprocess
import sys

def install_scrython_package():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "scrython"]
    subprocess.check_call([sys.executable, "-m", "pip", "install", "asyncio"]
    subprocess.check_call([sys.executable, "-m", "pip", "install", "aiohttp"]
