from cx_Freeze import setup, Executable

includes=[]
includefiles = ["mounts.sqlite","ddPak.ini","imageformats","User Manual"]

exe = Executable(
    script="ddPakSQLite.pyw",
    base="Win32GUI",
    targetName = "ddPak.exe" 
    )

setup(
    name = "ddPak",
    version = "0.1",
    description = "Packing Software for Mounts",
    options = {"build_exe": {"includes":includes,"include_files":includefiles,"icon":"plane box.ico"}},
    executables = [exe]
    )
