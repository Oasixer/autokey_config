#Enter script code
import subprocess
import time
cls = 'slack.Slack'

window.activate(cls, matchClass=True)
time.sleep(0.3)
if window.get_active_class() != cls:
    subprocess.run(["slack"])