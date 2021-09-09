#Enter script code
import subprocess
cls = 'autokey-qt.autokey-qt'
window.activate(cls, matchClass=True)
if window.get_active_class() != cls:
    subprocess.run(["autokey-qt"])