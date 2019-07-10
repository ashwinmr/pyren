import argparse
import os

def parse_args():
  """ Parse arguments for program
  """
  parser = argparse.ArgumentParser(description="Program for renaming files")
  parser.add_argument("find",help="Find pattern")
  parser.add_argument("-i","--ignore_case", action="store_true",  help = "Ignore case")
  parser.add_argument("rename",help="Rename pattern")
  parser.add_argument("-d","--directory",default=os.getcwd(), help = "Directory")
  parser.add_argument("-y","--no_confirm", action="store_true", help="Don't ask for confirmation")

  return parser.parse_args()

def perf_ren(ren_list):
  """ Rename files from a list of old and new paths
  """
  print("\nRenaming...\n")
  for old,new in ren_list:
    print("{} -> {}".format(os.path.basename(old),os.path.basename(new)))
    os.rename(old,new)

def prompt():
  """ Prompt whether to continue or not
  """
  while True:
    resp = input("\nContinues? [y/n]\n")
    if resp=="y":
      return True
    if resp=="n":
      return False

def disp_res(ren_list):
  """ Display results of renaming
  """
  print("\nThe following files will be renamed:")
  for old,new in ren_list:
    print("{:30}{:30}".format(os.path.basename(old),os.path.basename(new)))

def main():

  # Parse arguments
  # args = parse_args()
  ren_list = []
  for f in os.listdir("./temp"):
    ren_list.append((f,f))

  disp_res(ren_list)

if __name__ == "__main__":
  main()
