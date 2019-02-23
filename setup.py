from cx_Freeze import setup,Executable

options = {
    'include_files': ['bin/boehm_walk/walk_boehm{}.png'.format(i) for i in range(6)]\
            + ['bin/gold/gold0.png', 'bin/title.png'],
    'includes': ['pyglet', 'pyglet.resource', 'pyglet.clock']
}

setup(
    name = 'game',
    version = '0.1',
    description = 'demo game',
    author = 'me',
    author_email = 'le...@null.com',
    options = {'build_exe': options},
    executables = [Executable('game.py')]
)
