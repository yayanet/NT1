import os
from subprocess import Popen
from n1 import N1
from t1 import T1

def check_install():
    print("\033[36m[*] Checking whether HomeBrew is installed...\033[0m")
    p = Popen("brew -v >/dev/null 2>&1", shell=True)
    p.wait()
    if p.returncode == 0:
        print("\033[33m[*] HomeBrew is already installed.\033[0m")
    else:
        print("\033[34m[*] Installing HomeBrew...\033[0m")
        p = Popen("echo | ruby -e \"$(curl -fsSL http://raw.githubusercontent.com/Homebrew/install/master/install)\" > /dev/null 2>&1", shell=True)
        p.wait()
        if p.returncode == 0:
            print("\033[32m[+] Install HomeBrew Successfully.\033[0m")
        else:
            print("\033[31m[-] Install HomeBrew Failed.\033[0m")
    print("\033[36m[*] Installing adb tools...\033[0m")
    p = Popen("export HOMEBREW_NO_AUTO_UPDATE=true && brew cask install android-platform-tools > /dev/null 2>&1", shell=True)
    p.wait()
    if p.returncode == 0:
        print("\033[32m[+] Install adb tools Successfully\033[0m")
    else:
        print("\033[31m[-] Install adb tools Failed\033[0m")

def banner():
    print("""
 ______   __  __     ______     __     __     ______     __   __     _____     ______     ______     __     __   __     ______     ______     ______     ______     __        
/\__  _\ /\ \_\ \   /\  ___\   /\ \  _ \ \   /\  __ \   /\ "-.\ \   /\  __-.  /\  ___\   /\  == \   /\ \   /\ "-.\ \   /\  ___\   /\  ___\   /\  __ \   /\  ___\   /\ \       
\/_/\ \/ \ \  __ \  \ \  __\   \ \ \/ ".\ \  \ \  __ \  \ \ \-.  \  \ \ \/\ \ \ \  __\   \ \  __<   \ \ \  \ \ \-.  \  \ \ \__ \  \ \ \____  \ \ \/\ \  \ \  __\   \ \ \____  
   \ \_\  \ \_\ \_\  \ \_____\  \ \__/".~\_\  \ \_\ \_\  \ \_\\"\_\  \ \____-  \ \_____\  \ \_\ \_\  \ \_\  \ \_\\"\_\  \ \_____\  \ \_____\  \ \_____\  \ \_____\  \ \_____\ 
    \/_/   \/_/\/_/   \/_____/   \/_/   \/_/   \/_/\/_/   \/_/ \/_/   \/____/   \/_____/   \/_/ /_/   \/_/   \/_/ \/_/   \/_____/   \/_____/   \/_____/   \/_____/   \/_____/ 
""")

def choice():
    choose = int(input("选项列表:\n1.T1降级\n2.N1降级\n3.N1进入刷机模式\n4.N1激活U盘启动\n5.退出\n请选择: "))
    if choose == 5:
        os._exit(0)
    elif choose < 0 or choose > 5:
        print("\033[31m[-] No such option!\033[0m")
        choice()

    print("\033[36m[*] Killing adb server...\033[0m")
    os.system("adb kill-server")
    ip = input("\033[34m[*] IP Address: \033[0m")
    print("\033[36m[*] Connecting to device...\033[0m")
    os.system(f"adb connect {ip}")
    print("\033[36m[*] Remounting device...\033[0m")
    os.system("adb remount")
    if choose == 1:
        T1().downgrade()
    elif choose == 2:
        N1().downgrade()
    elif choose == 3:
        N1().flash()
    elif choose == 4:
        N1().udisk()


if __name__ == "__main__":
    banner()
    check_install()
    while True:
        choice()

