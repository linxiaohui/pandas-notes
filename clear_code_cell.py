# -*- coding:UTF-8 -*-
"""
输入Jupyter Notebook，清除其中的代码单元格中的代码
"""
import sys
import nbformat as nbf
input_book = sys.argv[1]
output_book = sys.argv[2]

ntbk = nbf.read(input_book, nbf.NO_CONVERT)
cells_to_keep = []
for cell in ntbk.cells:
    if cell.cell_type == "code":
        cell.source = ""
    cells_to_keep.append(cell)

new_ntbk = ntbk
new_ntbk.cells = cells_to_keep
nbf.write(new_ntbk, output_book, version=nbf.NO_CONVERT)
