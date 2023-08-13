import os
import tomllib

for root, dirs, files in os.walk('C:\\Users\\Spencer.Brown\\OneDrive - Sophos Ltd\\Documents\\spenProjects\\Python\\Detection Engineering\\detection_rules'):
    for file in files:
        if file.endswith(".toml"):
            with(open(file,"rb")) as toml:
                alert = tomllib.load(toml)