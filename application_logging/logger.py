from datetime import datetime
from colored import fg, bg, attr


class App_Logger:
    def __init__(self):
        pass

    def log(self, file_object, log_message):
        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime("%H:%M:%S")
        file_object.write(
            str(self.date) + "/" + str(self.current_time) + "\t\t" + log_message +"\n")
        print(fg('green_3b') + str(self.date)+"/"+ str(self.current_time)+"\t\t" +attr('reset')+ fg('red')+log_message+attr('reset'))
