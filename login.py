from selenium import webdriver
import configparser
import os

config = configparser.RawConfigParser()

config.read("./configuration/config.ini")


url = config.get("COMMON INFO","baseurl")

# Get the current file name
current_file = __file__

# Extract the file name without the path
file_name = os.path.basename(current_file)
def logfile(original_file):
    if original_file.endswith(".py"):
        new_file = os.path.splitext(original_file)[0] + ".log"
        # with open(new_file, 'a') as file:
        #     file.write('\nThis is additional content.')
        return new_file
    else:
        print(f"The file {original_file} does not have a '.py' extension.")

def check_url(self,actual_url):
        expected_url="https://demo.guru99.com/test/newtours/"
        if (self.actual_url == expected_url):
            print("exect match")
        else:
            print("actual url and expected url are different")


logfile1 = logfile(file_name)
file=open(logfile1, 'a')
a='logfile Created ::'+file+'\n'
file.write(a)

driver = webdriver.Chrome()
file.write("'Creat driver :: \'+driver+\'\n'")

file.write("'open browser with url::\'+url+\'\n'")
driver.get(url)


# driver.get("https://demo.guru99.com/test/newtours/")
# actual_url = driver.current_url
# print(actual_url)