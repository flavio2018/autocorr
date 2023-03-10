from pathlib import Path
import json
import os


def main():
	# Get proper paths
	project_path = Path(__file__).parent.parent
	py_files_path = (project_path / "ipynb").resolve()
	py_files_path.mkdir(exist_ok=True, parents=True)
	py_files = sorted(py_files_path.glob('*.ipynb'))
	results_path = (project_path / "code_only_notebooks").resolve()
	results_path.mkdir(exist_ok=True, parents=True)

	for filepath in py_files:
		print(f"Loading file {filepath}...")
		with open(filepath, 'r') as ipynb:
			ipynb_dict = json.loads(ipynb.read())

		print("Extracting cells...")
		extracted_cells = []
		in_section_to_extract = False
		for cell in ipynb_dict['cells']:
			if in_section_to_extract:
				if 'ENDCODE' in ''.join(cell['source']):
					in_section_to_extract = False
				else:
					extracted_cells.append(cell)
			else:
				if 'STARTCODE' in ''.join(cell['source']):
					in_section_to_extract = True
		ipynb_dict['cells'] = extracted_cells

		print("Saving file...")
		filename = filepath.name
		with open((results_path / filename).resolve(), 'w') as new_ipynb:
			new_ipynb.write(json.dumps(ipynb_dict))

		print("Done.")


if __name__ == '__main__':
	main()
