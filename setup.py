import subprocess

from setup.mongo_init import load_data_to_mongo

if __name__ == "__main__":

    subprocess.run(["pip", "install", "--upgrade", "pip"])
    subprocess.run(["pip3", "install", "-r", "setup/requirements.txt"])
    load_data_to_mongo()