#!/usr/bin/python3.8

# Awesome Time Based Wallpaper Changer
# I personnaly use 12 wallpaper located in the same folder and named from 1.jpg to 12.jpg
#

import subprocess
import datetime
import sys


wallpaper_path = "/home/pashmi/Pictures/wallpapers/"

# Js code used by the PlasmaShell in order to change the wallpaper


def change_paper_command(file):
    command = ['qdbus', 'org.kde.plasmashell',
               '/PlasmaShell', 'org.kde.PlasmaShell.evaluateScript']

    command.append("""
    desktops().forEach(d => {
        d.wallpaperPlugin = "org.kde.image";
        d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");
        d.writeConfig("Image", "%s")
    });
    """)
    command[-1] = command[-1] % file
    return command

# Get the current hour edited (since I've 12 file named from 1 to 12 I used a //2 +1)


def get_hour():
    return int(datetime.datetime.now().time().hour)//2 + 1

# Return the correct file based on the hour (not the true one but the resolved one)


def resolve_file_with_hour(file_number):
    file = wallpaper_path + '%d.jpg' % file_number
    return file


# Every time the hour change (check with prev which stands for the last hour)
# The wallpaper is changed with the previous functions
if __name__ == "__main__":
    subprocess.run(change_paper_command(resolve_file_with_hour(get_hour())))
