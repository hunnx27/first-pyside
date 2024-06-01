import time
from PySide6.QtCore import QThread, Signal
class WorkerThread(QThread):
    def __init__(self):
        super().__init__()
        self._is_running = True

    def run(self):
        from selenium.webdriver.chrome.options import Options
        from selenium import webdriver
        from urllib import parse
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        import time
        from selenium.webdriver.common.keys import Keys

        arg_blogURL = 'https://policy.tddiary.com'

        option = Options()
        option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        driver = webdriver.Chrome(options=option)
        from googleSC import GoogleSC
        sc = GoogleSC(blog_url=arg_blogURL , driver=driver)

        f = open("main_5_index_list.txt", 'r')
        lines = f.readlines()
        targets = []
        for line in lines:
            line = line.rstrip('\n')
            if line.find('#', 0, 1)!=0 and line!='':
                targets.append(line)
            
        print(targets)
        print('# 타겟 갯수 : {}'.format(len(targets)))
        f.close()
        errorlist = []
        for (idx, target) in enumerate(targets):
            try:
                print('')
                print('# [{}/{}] 시도 : {}'.format(idx+1, len(targets), target))
                sc.indexUri(target)
                print('# [{}/{}] 완료 : {}'.format(idx+1, len(targets), target))
            except Exception as e:
                print('# [{}/{}] 에러 : {} - e:{}'.format(idx+1, len(targets), target, e))
                errorlist.append(target)
            finally:
                time.sleep(2)

        print('#### 에러 리스트 일괄 출력')
        for errortarget in errorlist:
            print(errortarget)

    def stop(self):
        self._is_running = False
        self.quit()
        self.wait(5000)