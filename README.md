# Automatically correcting DL homeworks

To extract the answers, place jupyter notebooks in `ipynb/` and then run the `extract.sh` script. A csv with automatically extracted answers for all notebooks will be created in `results/`.
These answers have to be delimited by the strings `%STARTEXT` and `%ENDTEXT`.
Code-only versions of the notebooks with the cells containg students' answers will also be created in `code_only_notebooks`. The code cells have to be delimited by the strings `%STARTCODE` and `%ENDCODE`.
