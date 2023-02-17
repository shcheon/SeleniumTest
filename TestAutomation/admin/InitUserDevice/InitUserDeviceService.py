from time import sleep

from TestAutomation.admin.InitUserDevice.InitUserDeviceVO import InitUserDeviceVO
from TestAutomation.common.WebDriverConfig import ChromeWebDriver
from TestAutomation.common.LoggerUtil import LoggerUtil


class InitUserDeviceService(ChromeWebDriver, LoggerUtil):
    def __init__(self, console, param : InitUserDeviceVO, mode=''):
        ChromeWebDriver.__init__(self, mode)
        LoggerUtil.__init__(self, console)

        self.userId = param.userId
        self.userPassword = param.userPassword
        self.resetUserId = param.resetUserId

    def execute(self):
        self.driver.implicitly_wait(5)
        self._print_console(self.resetUserId + ' 사용자에 등록된 기기 중 첫번쨰로 조회되는 기기를 초기화 시작합니다.')
        self.driver.get("https://alpha-iims.navercorp.com/")  # ADMIN 사이트 진입
        self.driver.find_element_by_xpath("/html/body/div/div[1]/form/ul[1]/li[1]/div[1]/input").send_keys(self.userId)  # Login ID 입력
        self.driver.find_element_by_xpath("/html/body/div/div[1]/form/ul[1]/li[2]/input").send_keys(self.userPassword)  # Password 입력
        self.driver.find_element_by_xpath("/html/body/div/div[1]/form/p/button").click()  # Login 버튼 클릭

        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[1]/div/div[2]/div[2]/ul/li[1]/a/div").click()  # [COM]만화(Comic) 클릭
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/div[2]/div[1]/ul/li[5]/div/a").click()  # 기기조회(개발) 클릭
        self._print_console("[COM]만화(Comic) > 기기조회(개발) 진입 성공")
        sleep(2)

        # 사용자 기기조회 / 관리 화면이 동적로딩 완료되어야 html tag  조회가 가능하여 사이트가 정상적으로 로딩되었는지 3번 시도함
        isLoad = False
        for i in range(1, 5):
            try:
                document = self.driver.find_elements_by_tag_name('iframe')[0]
                self.driver.switch_to.frame(document)
                name = self.driver.find_element_by_xpath('/html/body/h3').text
                if name == '사용자 기기조회 / 관리':
                    isLoad = True
                    break
            except:
                self._print_console('사용자 기기조회 화면이 로딩되지 않았습니다. 2초 뒤에 재시도 합니다...')
                self.driver.switch_to.default_content()
                sleep(2)
                pass
        if not isLoad:
            self._print_console('사용자 기기조회 / 관리화면을 찾지 못하였습니다')
            return

        user_list = [self.resetUserId]

        for user in user_list:
            self.driver.find_element_by_xpath(
                '/html/body/div[2]/form/fieldset/table/tbody/tr/td[1]/table/tbody/tr/td/input').clear()
            self.driver.find_element_by_xpath(
                '/html/body/div[2]/form/fieldset/table/tbody/tr/td[1]/table/tbody/tr/td/input').send_keys(
                user)  # 사용자 ID 입력
            self.driver.find_element_by_xpath(
                '/html/body/div[2]/form/fieldset/table/tbody/tr/td[2]/input').click()  # 조회 클릭

            # 조회된 데이터 읽기 및 초기화 진행
            table = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/table")
            tbody = table.find_element_by_tag_name("tbody")

            # 테이블 row 데이터 읽기
            str = ''
            for td in tbody.find_elements_by_tag_name("tr")[0].find_elements_by_tag_name("td"):
                if td.get_attribute("innerText") == "초기화":
                    td.click()
                    self._print_console(str + "를 초기화 하였습니다.")
                    self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/button[1]').click()
                    break;
                str += '/' + td.get_attribute("innerText")
            sleep(2)
        self._print_console("테스트가 종료되었습니다.")
        self.driver.close()
