import os
os.system("jupyter nbconvert ./ipynb/*.ipynb --to python --output-dir='./py'")
print("Done...")
