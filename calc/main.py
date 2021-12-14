import pandas as pd
import logging
from properties import Properties
from calculate import Calculator
import os
import numpy as np
import shutil
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import time


class Operation(Properties, Calculator):

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.logger_name)
        self.operations = {"+": self.addition, "-": self.subtraction, "*": self.multiply_numbers,
                           "/": self.division_numbers}

    def start_logs(self):
        handler = logging.FileHandler(self.log_file_path, encoding='utf-8')
        handler.setFormatter(self.log_format)
        if not self.logger.handlers:
            self.logger.propagate = False
            self.logger.setLevel(logging.DEBUG)
            self.logger.addHandler(handler)

    def exit_logs(self):
        for handler in self.logger.handlers:
            handler.close()

    def read_files(self):
        self.start_logs()
        files = os.listdir(self.input_folder)
        for file in files:
            if self.file_format in file:
                print(f"Processing {file}")
                path = os.path.join(self.input_folder, file)
                self.data_frame = pd.read_csv(path, index_col=False)
                self.data_frame.replace(to_replace=[np.nan, None], value=str(), inplace=True)
                self.data_frame_copy = self.data_frame.copy()
                list(map(lambda row: self.make_operation(row, file, self.data_frame.loc[row][1],
                                                         self.data_frame.loc[row][2], self.data_frame.loc[row][3],
                                                         self.data_frame.loc[row][0]),
                         [x for x in range(len(self.data_frame))]))
                self.data_frame_copy.to_csv(path, index=False)
                if not os.path.exists(self.outpt_folder):
                    os.mkdir(self.outpt_folder)
                if file not in os.listdir(self.outpt_folder):
                    shutil.move(path, self.outpt_folder)
                del self.data_frame

    def make_operation(self, row, file_name, value_1, value_2, operation, record_number):
        if str(value_1).strip() != str() and str(value_2).strip() != str() and str(operation).strip() != str():
            if str(operation).strip() in self.operations.keys():
                try:
                    result = self.operations.get(str(operation).strip())(int(value_1), int(value_2))
                    self.data_frame_copy.loc[row, self.result_column] = result
                    self.logger.info(
                        self.result_format.format(file=file_name, RECORD=str(record_number), value_1=value_1,
                                                  value_2=value_2, operation=operation, output=result))
                except Exception as exc:
                    self.logger.exception(
                        self.exception_log_format.format(file=file_name, RECORD=str(record_number), exc=str(exc)))
            else:
                self.logger.warning(self.warning_format.format(file=file_name, RECORD=str(record_number),
                                                               msg=f"No opertion Found on {operation}"))
        else:
            self.logger.warning(self.warning_format.format(file=file_name, RECORD=str(record_number),
                                                           msg=f"Incorect Values {value_1},{value_2},{operation}"))


def main(event):
    obj = Operation()
    obj.read_files()
    obj.exit_logs()


if __name__ == "__main__":
    print(
        "Warning: Please Don`t Open the Csv  File`s While Running..! which are in Input Folder and Close the Csv While before You run")
    main('e')
    event_handler = LoggingEventHandler()
    observer = Observer()
    event_handler.on_created = main
    observer.schedule(event_handler, Properties().input_folder, recursive=True)
    observer.start()
    print("Running.......")
    try:
        while True:
            # Set the thread sleep time
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
