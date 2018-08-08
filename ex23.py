# downloaded file
import sys
# Importing sys as we are using encode and decode
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()
# This if statement goes through each line, no lines, no if statement
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

# Calling of a separate function of print_line
# This does the actual encoding of each line
def print_line(line, encoding, errors):
    next_lang = line.strip()
    # DBES, decode bytes, encode strings
    # Use .encode with utf-8, utf-16, or big5 to encode it. It's specified in args
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # Decode using your format 
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")
# This is a giant loop program that goes all the way until the end and resets until no line
# is left.
main(languages, encoding, error)