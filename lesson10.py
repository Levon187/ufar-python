import os
path = r"C:\Users\ufar\IdeaProjects\lesson10"
path2 = r"C:\Users\ufar"

def list_all_dir(path):
    files = os.listdir(path)
    print('=================')
    for file in files:
        low_path = os.path.join(path, file)
    if file.endswith(".ps"):
        print("DELETE!!!!", file)
    # os.remove(low_path)
    print(file)
    if os.path.isdir(low_path):
        print('-----------------')
    list_all_dir(low_path)



list_all_dir(path)