#Enter script code
import subprocess
cls = 'lotion.Lotion'
window.activate(cls, matchClass=True)
if window.get_active_class() != cls:
    subprocess.run(["lotion"])