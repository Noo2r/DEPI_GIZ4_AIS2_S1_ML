import os

def create_folders(path:str):
    if not os.path.exist(path):
        os.makedirs(path)
    for i in range(10):
        inner_path = os.path.join(path,"dir_"+str(i))
        if not os.path.exists(inner_path):
            os.makedirs(inner_path)

if __name__ == "__main__":
    path = ""
    create_folders(path)
