import subprocess

print('Unmapping Started!')

# Disconnect anything on M
subprocess.call(r'net use *: /del /Y', shell=True)

print('Unmapping Finished!')