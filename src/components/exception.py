import sys
def error_message_detail(error,error_detail:sys):
    _,_,error_tb=error_detail.exc_info()
    file_name=error_tb.tb_frame.f_code.co_filename
    error_message="error occourced in python script names {0} in line number {1} and the error message is [{2}]".format(file_name,error_tb.tb_lineno,str(error))
class Custon_Exception(Exception):
    def __init__(self,error,error_details:sys):
        super().__init__()
        self.error_message=error_message_detail(error=error,error_detail=error_details)
    def __str__(self):
        return self.error_message
