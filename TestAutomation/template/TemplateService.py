from time import sleep

from TestAutomation.template.TemplateVO import TemplateVO
from TestAutomation.common.WebDriverConfig import ChromeWebDriver
from TestAutomation.common.LoggerUtil import LoggerUtil


class TemplateService(ChromeWebDriver, LoggerUtil):
    def __init__(self, console, param : TemplateVO, mode=''):
        ChromeWebDriver.__init__(self, mode)
        LoggerUtil.__init__(self, console)

        self.arg1 = param.arg1
        self.arg2 = param.arg2

    def execute(self):
        self.driver.get("https://www.naver.com")
        self._print_console("naver 화면 출력")
        sleep(1)
        self._print_console("테스트 종료")
        self.driver.close()
        # Webdriver로 Chrome을 제어할 코드를 작성한다
        # self._print_console : UI의 메세지 박스에 내용을 출력
        # self.driver.get : 브라우저를 실행하여 URL 실행
        # self.driver.find_element_by_xpath("XPATH").send_keys("입력값") : HTML의 form에 입력할 값 지정
        # self.driver.find_element_by_xpath("XPATH").click() : html 태그를 클릭
        # self.driver.switch_to.frame('iframe') : HTML문서에서 또다른 HTML문서를 불러올 경우, iframe으로 html을 출력하는데, iframe 내부의 태그를 지정하려면 iframe으로 DOM을 전환해야 함
        # self.driver.switch_to.default_content() : iframe의 상위 태그로 다시 돌아갈 경우, 해당 함수 실행
        # self.driver.close() : 브라우저 테스트가 종료되면, driver을 닫아줌


