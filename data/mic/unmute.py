#Enter script code
import subprocess
subprocess.call(['pactl', 'set-source-mute', 'alsa_input.pci-0000_00_1b.0.analog-stereo', 'false'])
subprocess.call(['paplay', '/home/k/Documents/sounds/clearly-602.ogg'])
