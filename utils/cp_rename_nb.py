import argparse
from pathlib import Path
from shutil import copyfile


def main(args):
	src_folder = Path(args.src).resolve()
	dest_folder = Path(args.dest).resolve()

	for folder in src_folder.iterdir():
		if folder.is_dir():
			student_name = folder.name.split("_")[0]
			notebook_name = student_name.replace(' ', '_').lower()
		for file in folder.iterdir():
			if file.is_file() and file.suffix == '.ipynb':
				copyfile(str(file), str(dest_folder) + '/' + notebook_name + '.ipynb')


if __name__ == '__main__':
	parser = argparse.ArgumentParser(
                    prog='Copy+Rename_NB',
                    description='Copies homeworks renaming them with students names.')
	parser.add_argument('src')
	parser.add_argument('dest')
	args = parser.parse_args()
	main(args)
