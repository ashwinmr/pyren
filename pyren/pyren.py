import argparse

def parse_args():
  """ Parse arguments for program
  """
    parser = argparse.ArgumentParser(description="Program for renaming files")
    parser.add_argument("find",help="Find pattern")
    parser.add_argument("-i","--ignore_case", action="store_true",  help = "Ignore case")
    parser.add_argument("rename",help="Rename pattern")
    parser.add_argument("-d","--directory", help = "Directory")
    parser.add_argument("-y","--no_confirm", action="store_true", help="Don't ask for confirmation")

    return parser.parse_args()

def main():
  parse_args()

if __name__ == "__main__":
  main()
