#!/usr/local/bin/python
import argparse
import os
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("template", help="The name of the template to generate.")
parser.add_argument("dest", help="The destination path to generate the template in.")
parser.add_argument("--template_directory", help="The path containing templates which can be used for scaffolding.", default="/usr/local/share/scaffolding/")

arguments = parser.parse_args()

# Get arguments as strings.
source_directory_path = os.path.join(arguments.template_directory, arguments.template)
dest = arguments.dest
basename = os.path.basename(source_directory_path)

# Create the template directory if it does not exist.
if not os.path.exists(source_directory_path):
    print("Created scaffolding directory at {}".format(source_directory_path))
    os.makedirs(source_directory_path)

# Check for valid paths.
if not os.path.exists(source_directory_path):
    print ("Scaffold {} could not be found.".format(basename))
    exit(1)


if os.path.exists(dest):
    print("Deleting {}".format(dest))
    shutil.rmtree(dest)
    if os.path.exists(dest):
        print("Failed to delete {}".format(dest))
        exit(-1)

shutil.copytree(source_directory_path, dest)

if not os.path.exists(dest):
    print("Scaffolding failed!")
else:
    print("Generated scaffold: {}".format(basename))
