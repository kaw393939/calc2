"""Testing pandas class"""
import pytest
from calc.utils.file_reader import PandasFileReader


def test_pandas_file_type_csv_check():
    """Testing the file type check"""
    #Arrange
    file_name = "addition_15values.csv"
    #Act
    df_test_csv_data = PandasFileReader(file_name).read_file()
    #Assert
    assert df_test_csv_data is not None

def test_pandas_file_type_xlsx_check():
    """Testing df creating after extracting data from excel file"""
    #Arrange
    file_name = "subtraction_15values.xlsx"
    #Act
    df_test_xlsx_data = PandasFileReader(file_name).read_file()
    #Assert
    assert df_test_xlsx_data is not None

def test_pandas_file_type_txt_check():
    """Testing df creating after extracting data from excel file"""
    #Arrange
    file_name = "subtraction_15values.txt"
    #Act
    with pytest.raises(ValueError):
        #Assert
        assert PandasFileReader(file_name).read_file()
