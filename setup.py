from cx_Freeze import setup, Executable

target = Executable(
        script='login_.py',
        base='Win32GUI',
        icon='tokidoki.ico'
        )

files = ['tokidoki.ico', 'images']

setup(
        name='app',
        version='1.0',
        description='no description',
        author='Nguyen Nhu Tai',
        options={'build_exe' : {'include_files': files}},
        executables=[target]
        )