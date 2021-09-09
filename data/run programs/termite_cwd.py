#Enter script code
if 'nvim' not in window.get_active_title():
    exit()
import subprocess
keyboard.send_key('<escape>')
keyboard.send_keys(':CopyCWD')
time.sleep(0.01)
keyboard.send_key('<enter>')
#keyboard.send_keys(':
#time.sleep(0.1)
#keyboard.send_key('<enter>')
time.sleep(0.1)
subprocess.Popen(['termite'])
cb = clipboard.get_clipboard()
time.sleep(0.1)
keyboard.send_keys(f'cd {cb}')
keyboard.send_key('<enter>')