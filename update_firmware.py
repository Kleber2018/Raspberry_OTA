#!/usr/bin/env python3

from datetime import datetime, timedelta
import time
import subprocess
import git

def update():
    try:
        try:
            #resetando qualquer alteração que tenha no código do Raspberry
            subprocess.run(["sudo", "rm", "-f", "/home/seu_projeto/.git/index.lock"])
        except Exception as e:
            print('erro no git reset', e)
        repo = git.Repo('/home/seu_projeto')
        repo.git.reset('--hard')
        repo_heads = repo.heads
        try:
            print(repo_heads)
            repo_heads['master'].checkout()
        except Exception as e:
            print('erro no git reset', e)
        repo.git.reset('--hard')
        repo.git.clean('-xdf')
        repo.remotes.origin.pull() #puxando os código do GitHub
        print("atualizado")
        time.sleep(10.0)
        #Atribuindo permissões para o brojeto atualizado
        subprocess.run(["sudo", "chmod", "-R", "777", "/home/seu_projeto"]) 
        time.sleep(10.0)
        #Reinicia o Raspberry
        subprocess.run(["sudo", "reboot"])
    except Exception as e:
        print('erro atualização', e)
        return 0

#resetando qualquer alteração que tenha no código do Raspberry
def resetar_fila():
    try:
        subprocess.run(["git", "checkout", "--", "."])
        subprocess.run(["git", "clean", "-f", "-d"])
        return 1
    except Exception as e:
        print('erro no git reset', e)
        return 0

def backup():
    try:
        clear_bkp()
        import time
        time.sleep(5.0)
        now = datetime.now()
        print(now.year)
        subprocess.run(["sudo", "cp", "-fR", "/home/seu_projeto", "/home/seu_projeto_bkp"])
        return 1
    except Exception as e:
        print('erro backup', e)
        return 0

def clear_bkp():
    try:
        now = datetime.now()
        print(now.year)
        subprocess.run(["sudo", "rm", "-fR", "/home/seu_projeto_bkp"])
        return 1
    except Exception as e:
        print('erro clear_bkp', e)
        return 0


if __name__ == "__main__":
    update()