import re
import os
import pandas as pd


def main():
  py_files_path = os.path.join(os. getcwd(), 'py')
  files = list(filter(lambda x:".py" in x, os.listdir(py_files_path)))

  if os.path.exists("results/results.csv"):
    results = pd.read_csv("results/results.csv")
  else:
    results = pd.DataFrame()

  for f_idx, f in enumerate(files):
    name = f.split("/")[-1].split(".")[0]
    answers = get_with_re(os.path.join(py_files_path, f))
    columns = ["Q"+str(n_col+1) for n_col in range(len(answers))]

    ans_df = pd.DataFrame({
      col: ans.replace("%START", "").replace("%END", "")
      for col, ans in zip(columns, answers)
  }, index=[name])
    results = results.append(ans_df)
  results.to_csv("results/results.csv") #Rewirting


def get_with_re(path):
  answers = []
  with open(path, 'r') as f:
    hw = f.read()
    Match = re.findall(r'%START.*?%END', hw, flags=re.DOTALL)
    seperator = '\n'+'-'*25 + '\n'
    answer = seperator
    for ans in Match:
      answers += [ans]
    return answers


if __name__ == '__main__':
  main()
