import os
import re

STYLES_PATH = "bookable_styles.scss"


if __name__ == "__main__":
    with open(STYLES_PATH, "r") as f:
        styles = f.read()

    desk_matches = re.findall(
        r"(#CLUJ.*?{\s*margin-left: \d+px;\s*margin-top: \d+px;\s*})",
        styles,
        re.DOTALL,
    )
    room_matches = re.findall(
        r"(#(?!CLUJ)[\w-]+\s*{\s*margin-left: \d+px;\s*margin-top: \d+px;\s*})",
        styles,
        re.DOTALL,
    )

    for match in room_matches:
        print(match)
    with open("extracted_desks.txt", "w") as f:
        for match in desk_matches:
            lines = match.strip("#").split("\n")
            id = lines[0].split("{")[0]
            margin_left = lines[1].split(":")[1].split("px")[0]
            margin_top = lines[2].split(":")[1].split("px")[0]
            line = f"{id} {margin_left} {margin_top}\n"
            f.write(line)

    with open("extracted_rooms.txt", "w") as f:
        for match in room_matches:
            lines = match.strip("#").split("\n")
            id = lines[0].split("{")[0]
            margin_left = lines[1].split(":")[1].split("px")[0]
            margin_top = lines[2].split(":")[1].split("px")[0]
            line = f"{id} {margin_left} {margin_top}\n"
            f.write(line)
