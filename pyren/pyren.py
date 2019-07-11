import argparse
import os
import re

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
  for old,new in ren_list:
    print("{:30}{:30}".format(os.path.basename(old),os.path.basename(new)))

def main():

  # Parse arguments
  args = parse_args()

  find_pat = args.find
  ren_pat = args.rename
  directory = args.directory

  # Set icase flag
  if args.ignore_case:
    icase = re.I
  else:
    icase = 0

  # Create list of old and new paths
  ren_list = []

  # Create regex object
  ro = re.compile(pattern = find_pat, flags = icase)

  # Create rename list for files in directory
  for old_str in os.listdir(directory):

    # Check for matching file
    if(ro.match(string = old_str)):

      # Create rename string by using patterns
      new_str = ro.sub(repl = ren_pat, string = old_str, count=1)

      # Store results
      ren_list.append((os.path.join(directory,old_str), os.path.join(directory,new_str)))

  # Display results
  print("\nThe following files will be renamed:")
  disp_res(ren_list)

  # Ask for confirmation before renaming
  if not args.no_confirm:
    if(prompt()):
      perf_ren(ren_list)
  else:
    perf_ren(ren_list)

if __name__ == "__main__":
  main()
