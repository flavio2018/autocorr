# python utils/convert.py
jupyter nbconvert ./ipynb/*.ipynb --to python --output-dir=./py
echo Done...
python utils/auto_finder.py 
python utils/extract_code_cells_ipynb.py ipynb/*.ipynb
