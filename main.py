import platform


def main():

    print("##################################################################")
    print("#################### Your Platform ###############################")

    processor = platform.processor()
    system = platform.system()
    release = platform.release()
    machine = platform.machine()
    version = platform.version()

    res = processor + "," + system + "," + release + "," + machine + "," + version

    print(res)

    print("\n\n########## Copyright 2021. Eduardo Programador ##############")
    print("############## consultoria@eduardoprogramador.com ###############")


main()