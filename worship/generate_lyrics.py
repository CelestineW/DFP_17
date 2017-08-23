import sys


def main(argv):

        print(argv[0])
        content = []

        with open(argv[0]) as f:
                content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content] 

        content = filter(None, content)
        print(content)


if __name__ == "__main__":
   main(sys.argv[1:])
