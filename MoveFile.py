import time
import os
import shutil
import argparse

def mkdir_path(path):
    if not os.access(path, os.F_OK):
        os.mkdir(path)

def _movefile(src, dst, filename):
	imgCreatedOn = time.strftime('%m/%d/%Y', time.gmtime(os.path.getmtime(src)))
	splitCreateOn = imgCreatedOn.split("/")
	yyyy_mm = splitCreateOn[2] + "_" + splitCreateOn[0] 
   
	dst = "".join((dst, "\\", yyyy_mm))
	if not os.path.isdir(dst):
		mkdir_path(dst)
	
	dst = "".join((dst, "/", filename))
	shutil.move(src, dest)
	
def movefile(src, dest):
    # Walk the tree.
    for root, directories, files in os.walk(src):
        for filename in files:
            filepath = os.path.join(root, filename)
	    if filepath.lower().endswith(('.png', '.jpg', '.jpeg')):
		_movefile(filepath, dest, filename)


if __name__ == "__main__":   
	parser = argparse.ArgumentParser(description='Program to move *.jpg, *.jpeg, *.png file to destination directory of yyyy_mm')
	parser.add_argument('-s','--src', help='Specify the source directory', required=True)
	parser.add_argument('-d','--dst', help='Specify the destination directory', required=True)
	args = vars(parser.parse_args())

	if not os.path.isdir(args['src']):
		print "Source directory not found"
		exit(1)

	movefile(args['src'], args['dst'])
