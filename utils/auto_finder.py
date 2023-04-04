import re
from pathlib import Path

import pandas as pd


def get_with_re(path):
    answers = []
    with open(path, 'r', encoding="utf-8") as f:
        hw = f.read()
        match = re.findall(r"(?<=`%STARTEXT`)(.*?)(?=`%ENDTEXT`)", hw, flags=re.DOTALL)
        # What's the point of this? I don't get it
        # seperator = '\n' + '-' * 25 + '\n'
        # answer = seperator
        for ans in match:
            ans = ans.replace('\n', '').replace('\r', '').replace('#', '').replace('*', '')
            answers += [ans]
        return answers


def main():
    # Get proper paths
    project_path = Path(__file__).parent.parent
    py_files_path = (project_path / "py").resolve()
    py_files_path.mkdir(exist_ok=True, parents=True)
    py_files = sorted(py_files_path.glob('*.py'))

    # Store results
    results_path = (project_path / "results/results.csv").resolve()
    if results_path.exists():
        results = pd.read_csv(results_path)
    else:
        results = pd.DataFrame()

    for f in py_files:
        name = f.stem.replace('_', ' ').upper()
        answers = get_with_re(f)
        columns = ["Q" + str(n_col + 1) for n_col in range(len(answers))]

        ans_df = pd.DataFrame({col: ans for col, ans in zip(columns, answers)}, index=[name])
        results = pd.concat([results, ans_df])
    results.to_csv(results_path)  # Rewriting


if __name__ == '__main__':
    main()
    print("All finished!")
