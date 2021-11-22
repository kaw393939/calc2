"""Testing pandas class"""
import pytest
from tests.panda_extract_data import PandaExtractData


def test_pandas_file_type_csv_check():
    """Testing the file type check"""
    #Arrange
    file_name = "addition_15values.csv"
    #Act
    df_test_csv_data = PandaExtractData.read_file(file_name)
    #Assert
    assert df_test_csv_data is not None

def test_pandas_file_type_xlsx_check():
    """Testing df creating after extracting data from excel file"""
    #Arrange
    file_name = "subtraction_15values.xlsx"
    #Act
    df_test_xlsx_data = PandaExtractData.read_file(file_name)
    #Assert
    assert df_test_xlsx_data is not None

def test_pandas_file_type_txt_check():
    """Testing df creating after extracting data from excel file"""
    #Arrange
    file_name = "subtraction_15values.txt"
    #Act
    with pytest.raises(ValueError):
        #Assert
        assert PandaExtractData.read_file(file_name)
