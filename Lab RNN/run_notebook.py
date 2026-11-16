"""Повторный запуск выполненного ноутбука из того же Python-окружения."""
from pathlib import Path
import argparse
import nbformat
from nbclient import NotebookClient

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('notebook', nargs='?', default='02_elman_rnn_language_model_completed.ipynb')
args = parser.parse_args()
path = Path(args.notebook).resolve()
notebook = nbformat.read(path, as_version=4)
NotebookClient(notebook, timeout=3600, kernel_name='python3',
               resources={'metadata': {'path': str(path.parent)}}).execute()
nbformat.write(notebook, path)
print(f'Выполнено и сохранено: {path}')
