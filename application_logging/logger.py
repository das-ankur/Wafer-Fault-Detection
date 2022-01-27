from datetime import datetime   # To get current date and time of system
class App_Logger:
    """
    The class is used to log messages in the file
    """

    def __init__(self):
        """
        Description: Empty Constructor
        """
        pass

    def log(self, file_object, log_message):
        """
        Description: The methods log messages in file
        :param file_object: file object in which message to be logged
        :param log_message: message to be logged
        """
        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime("%H:%M:%S")
        file_object.write(
            str(self.date) + "/" + str(self.current_time) + "\t\t" + log_message +"\n")