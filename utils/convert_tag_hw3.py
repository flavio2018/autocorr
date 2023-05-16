"""Convert last TEXT tag in Homework3 to a CODE tag."""


from pathlib import Path
import json
import os


def main():
	# Get proper paths
	project_path = Path(__file__).parent.parent
	ipynb_files_path = (project_path / "ipynb").resolve()
	ipynb_files_path.mkdir(exist_ok=True, parents=True)
	ipynb_files = sorted(ipynb_files_path.glob('*.ipynb'))
	
	for filepath in ipynb_files:
		print(f"Loading file {filepath}...")
		with open(filepath, 'r', encoding="utf-8") as ipynb:
			ipynb_dict = json.loads(ipynb.read())

		print("Converting tag...")
		extracted_cells = []
		in_section_to_extract = False
		text_tag_counter = 0
		for cell_idx, cell in enumerate(ipynb_dict['cells']):
			if 'STARTEXT' in ''.join(cell['source']):
				text_tag_counter += 1

				if text_tag_counter == 3:
					cell['source'] = [line.replace('STARTEXT', 'STARTCODE') for line in cell['source']]
					ipynb_dict['cells'][cell_idx]['source'] = cell['source']

			if 'ENDTEXT' in ''.join(cell['source']) and text_tag_counter == 3:
				cell['source'] = [line.replace('ENDTEXT', 'ENDCODE') for line in cell['source']]
				ipynb_dict['cells'][cell_idx]['source'] = cell['source']

		print("Saving file...")
		filename = filepath.name
		with open((ipynb_files_path/filename).resolve(), 'w') as new_ipynb:
			new_ipynb.write(json.dumps(ipynb_dict))
		print("Done.")


if __name__ == '__main__':
	main()