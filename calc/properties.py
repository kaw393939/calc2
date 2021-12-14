import os
import logging
class Properties:
    """
    Properties Class
        To define few configurations.
    """
    def __init__(self):
        self.input_folder=os.path.join(os.getcwd(),"do")
        self.outpt_folder=os.path.join(os.getcwd(),"done")
        self.file_format=".csv"
        self.log_file_path="calculater.log"
        self.result_column="Result"
        self.logger_name="main"
        self.log_format=logging.Formatter("%(asctime)s %(name)s %(levelname)s:%(message)s")
        self.result_format="FileName :-{file} Record :- {RECORD}  Value 1 :- {value_1} Value 2 :- {value_2}  Operation :- {operation}  RESULT :- {output}"
        self.exception_log_format="FileName :-{file} Record :- {RECORD} EXC:- {exc}"
        self.warning_format="FileName :-{file} Record :- {RECORD} Message :- {msg}"