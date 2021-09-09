#Enter script code
import subprocess
cls = 'discord.discord'
window.activate(cls, matchClass=True)
if window.get_active_class() != cls:
    subprocess.run(["discord"])