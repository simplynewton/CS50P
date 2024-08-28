import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # s? makes it optional, :// means there must be a litteral :// after http
    # (?:www\.)?, (?:...) means this will be match but not captured group, www\. matches the optional www.
    #[a-zA-Z0-9_-](taken from the email script we made previously) is a captured group, I added _ and - incase there are litteral _ and - in the video id
    match = re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"', s)

    if match:
        return f"https://youtu.be/{match.group(1)}"
    else:
        return None

if __name__ == "__main__":
    main()
