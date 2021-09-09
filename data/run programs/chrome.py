# Enter script code
import subprocess
import time
cls = 'google-chrome.Google-chrome'
window.activate(cls, matchClass=True)
time.sleep(0.4)
if window.get_active_class() != cls:
    subprocess.run(["google-chrome"])