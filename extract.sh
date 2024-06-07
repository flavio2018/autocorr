# python utils/convert.py
# Remove all the ipynb files in the ipynb folder
rm -rfv ipynb/*.ipynb
# Remove all the py files in the py folder
rm -rfv py/*.py
# Remove all the ipynb files in the code_only_notebooks folder
rm -rfv code_only_notebooks/*.ipynb

# Use HW_splitter to make the splits and move files
echo Use HW_splitter to make the splits and move files first

# Convert and extract
jupyter nbconvert ./ipynb/*.ipynb --to python --output-dir=./py
python utils/auto_finder.py
python utils/extract_code_cells_ipynb.py ipynb/*.ipynb
echo Done...
