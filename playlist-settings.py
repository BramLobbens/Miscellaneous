from sys import argv
import re

def main(args):

    path = args[0]
    timestamp = f"<vlc:option>start-time={args[1]}</vlc:option>"
    lines = []

    with open(path, 'r+') as infile:
        for line in infile.readlines():
            if re.match(r"\s*<\w*:id>\d*<\S\w*:id>", line):
                lines.append(line.strip() + timestamp)
            else:
                lines.append(line)

    out = path.split(".")
    newpath = out[0] + "_copy." + out[1]

    with open(newpath, "w") as outfile:
        outfile.writelines(lines)

if __name__ == '__main__':
    main(argv[1:])