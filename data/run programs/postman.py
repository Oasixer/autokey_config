#Enter script codeEnter script code
import subprocess
cls = 'postman.Postman'
window.activate(cls, matchClass=True)
if window.get_active_class() != cls:
    subprocess.run(["postman"])