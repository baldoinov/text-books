import os

for dirpath, dirnames, filenames in os.walk('think-python-2e-exercises'):
    
    for file in filenames:

        print(file)


if __name__ == '__main__':
    pass