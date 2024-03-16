import os
import re

STYLES_PATH = "bookable_styles.scss"


if __name__ == "__main__":
    with open(STYLES_PATH, "r") as f:
        styles = f.read()

    # Extract bookable styles
    matches = re.findall(
        r"(\.CLUJ.*?{\s*margin-left: \d+px;\s*margin-top: \d+px;\s*})",
        styles,
        re.DOTALL,
    )
    with open("extracted_lines.txt", "w") as f:
        for match in matches:
            lines = match.split("\n")
            id = lines[0].split("{")[0]
            margin_left = lines[1].split(":")[1].split("px")[0]
            margin_top = lines[2].split(":")[1].split("px")[0]
            line = f"{id} {margin_left} {margin_top}\n"
            f.write(line)

    # Write bookable styles to file
    # with open("bookable_styles_extracted.scss", "w") as f:
    #     f.write("\n".join(bookable_styles))
