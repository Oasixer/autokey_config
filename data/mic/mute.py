#Enter script code
import subprocess
subprocess.call(['pactl', 'set-source-mute', 'alsa_input.pci-0000_00_1b.0.analog-stereo', 'true'])
subprocess.call(['paplay', '/home/k/Documents/sounds/stealthy-beep-100.ogg'])
