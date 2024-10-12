import os
from module.color import color

# Creating the fake structure
def struct():
    try:
        os.mkdir('honeypot')
        print(f'{color.fr_yellow} [!] Creating the honeypot file structure ...{color.reset}')
        try:
            os.mkdir('honeypot/ftp')
            print(f'{color.fr_yellow} [!] Honeypot file structure succesfully created.{color.reset}')
        except:
            pass
    except FileExistsError:
        print(f'{color.fr_yellow} [!] The FTP honeypot file structure is correct{color.reset}')