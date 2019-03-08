import subprocess


if __name__ == "__main__":

    subprocess.run(["pip", "install", "--upgrade", "pip"])
    subprocess.run(["pip3", "install", "-r", "setup/requirements.txt"])

    from setup.mongo_init import load_data_to_mongo
    load_data_to_mongo()