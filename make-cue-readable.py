#!/usr/bin/python3

# Converting a *.cue file to an readable tracklist

import re
import sys
#file_path = "tracklist.txt"
track_count = 1
# The pattern are orded after their occurence
track_pattern = r"TRACK\s(\d+)\sAUDIO"
title_pattern = r"TITLE\s\"(.*)\""
performer_pattern = r"PERFORMER\s\"(.*)\""
index_pattern = r"INDEX\s[\d]*\s(\d{2}:\d{2}:\d{2})"

num = ""
title = ""
performer = ""
index = ""

try:
    file_path = sys.argv[1]
    with open(file_path) as f:
        for line in f:
            track_match = re.findall(track_pattern, line)
            if(track_match):
                num = track_match[0]
                print(num)
                continue

            title_match = re.findall(title_pattern, line)
            if(title_match):
                title = title_match[0]
                print(title)
                continue

            performer_match = re.findall(performer_pattern, line)
            if(performer_match):
                performer = performer_match[0]
                print(performer)
                continue

            index_match = re.findall(index_pattern, line)
            if(index_match):
                index = index_match[0]
                print(index)
                # append file and set all vars to ""
                with open("newtracklist.txt", "a") as newfile:
                    newfile.writelines("[{}] {}, {}, {} \n"
                            .format(num, title, performer, index))
                    num = ""
                    title = ""
                    performer = ""
                    index = ""
                
                continue
except:
    print("Give in the path to *.cue as an argument.")


