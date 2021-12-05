"""Testing pandas"""
import pytest
from calc.utilities.csv import CSVReader

def test_pandas_read_file():
    """Testing the file check"""

def test_pandas_file_type_csv_check(addition_file_fixture):
    """Testing extraction of data from csv file"""
    file_name = "addition.csv"
    df_test_csv_data = CSVReader(file_name).read_file()
    assert df_test_csv_data is not None

def test_pandas_file_type_txt_check():
    """Testing incorrect file type check"""
    file_name = "test.txt"
    with pytest.raises(ValueError):
        assert CSVReader(file_name).read_file() is True
