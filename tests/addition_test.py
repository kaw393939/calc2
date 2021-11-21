"""Testing Addition"""
import os

import pandas as pd

from calc.calculations.addition import Addition

BASE_DIR = os.path.dirname(os.path.realpath(__file__)) # Get Current Working Directory


def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    #Arrange
    file_path = os.path.join(BASE_DIR, "addition_15values.xlsx")
    df = pd.read_excel(io=file_path, index_col=None, names=["value_1",	"value_2",	"result"], dtype='float')
    for index, row in df.iterrows():
        tuple_values = (row.value_1, row.value_2)
        #print(tuple_values)
        addition = Addition.create(tuple_values)
        assert addition.get_result() == df['result'][index]

    with pd.ExcelWriter('addition_15values.xlsx', mode='a') as writer:
        df.to_excel(writer, sheet_name='Tested_output', index=False)
        writer.save()


