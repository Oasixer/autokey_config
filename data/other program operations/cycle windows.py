#Enter script code
import subprocess
#import cycle_windows2
try:
    title = window.get_active_title()
    if 'nvim' in window.get_active_title():
        nvim = True
    else:
        nvim = False
        
    classs = window.get_active_class().split(".")[0]

    subprocess.call(['python3', '/home/k/.config/scripts/cycle_windows2.py', classs])
except:
    pass
#time.sleep(0.3)

#if nvim:
 #   if 'nvim' in window.get_active_title():
  #      subprocess.call(['python3', '/home/k/.config/scripts/cycle_windows2.py', window.get_active_class().split(".")[0]])
#str = ['python3', '~/.config/scripts/cycle_windows2.py', ]
#str = ['python3', '~/.config/scripts/cycle_windows2.py', 'termite']

#call(str, shell=True)

