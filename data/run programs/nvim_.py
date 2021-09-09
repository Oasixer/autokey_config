#Enter script code
import subprocess, os

try:
    window.activate('nvim')
    time.sleep(0.15)

    if ('nvim' not in window.get_active_title() and 'neovim' not in window.get_active_title()) or 'chrome' in window.get_active_class():
        my_env = os.environ.copy()
        my_env['TMPDIR']='/tmp'
        subprocess.Popen(["/usr/local/bin/termite", "-e", "nvim"],env=my_env)
except:
    print('aaaaa')
    pass