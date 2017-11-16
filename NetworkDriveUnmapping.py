import subprocess

print('Unmapping Started!')

subprocess.call(r'net use *: /del /Y', shell=True)

print('Unmapping Finished!')