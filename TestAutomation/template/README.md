# Series Test Automation Project 코딩 가이드
- 본 프로젝트는 Python 기반으로 작성되었으며, PyQt, selenium 를 활용하였음
- Qt UI 파이썬 소스파일에 셀레니움 API를 작성하면, 소스 파일은 비대해지고 관리의 어려움이 발생하고, 심지어 여러 사람이 협업할 경우 git과 같은 형상을 사용 시 conflict가 자주 발생할 가능성이 높음
- 소스 파일 충돌을 없애고 UI 파이썬 코드가 커지지 않도록 하고자, 3개의 클래스(Controller, Service, VO)를 이용하여 셀레니움 테스트 코드를 작성하도록 가이드 문서를 작성함

## 프로그래밍 Tip
UI에서 파이선 코드 실행 중 오류로 인해 프로그램이 종료되면 오류 원인이 출력되지 않으므로,
Controller, Service, VO 클래스를 먼저 작성하고 Python Console 모드로 실행하면서 테스트 코드를 작성하는게 좋음


## 클래스 호출 순서 예시
1. UI Class에서 Controller 객체 생성 및 실행 
2. Controller클래스에서 Service 객체를 생성하고 실행함 
   1. Controller는 쓰레드로 실행되어 GUI(메인 쓰레드)에 영향을 주지 않음
   2. UI Class에서 넘겨받은 parameter를 Service 객체 실행 시 전달함
3. Service 클래스에 셀레니움 테스트 코드를 작성함

## UI 파이썬 코드
Qt Desiner로 그린 UI를 Python 코드로 전환된 코드를 UI 파이썬 코드라고 부름.

 UI의 컴포넌트의 이벤트는 아래와 같이 파이썬 코드를 작성해야 동작함


    def executeClicked(self):
        if self.alphaButton.isChecked():
            InitUserDeviceController(self,
                                     self.stateBrowser,
                                     self.UserID.text(),
                                     self.UserPW.text(),
                                     self.TestID.text(),
                                     "headless"
                                     ).start()
        pass

- executeClicked함수는 Qt UI 컴포넌트에 등록된 이벤트 함수
- self는 QThread로 실행하기 위한 Argument (테스트 실행 중에도 GUI의 화면을 갱신하기 위해 쓰레드로 실행해야 함)  
- self.stateBrowser는 GUI의 TextMessagebox에 메세지를 출력하기 위함
- self.UserID, self.UserPW, self.TestID는 GUI에서 입력 받은 데이터, 즉 테스트에 필요한 데이터
- "headless" 는 브라우저 창을 띄울것인지 모드를 결정함. 입력하지 않으면, 브라우저가 출력됨

## Controller
Controller의 역할은 UI에서 넘겨 받은 데이터를 정재하고 조합하여 Service 클래스를 실행할 떄 데이터를 넘겨주는 역할을 한다.

테스트 시나리오에 따라 하나의 Controller에서 여러개의 Service를 호출해도 무방함


    class TemplateController(QThread):
        def __init__(self, parent, console, arg1, arg2, mode=''):
            QThread.__init__(self, parent)
            self.console = console
            self.mode = mode
            self.vo = TemplateVO(arg1, arg2)

    def run(self):
        TemplateService(self.console, self.vo, self.mode).execute()

- Controller는 쓰레드로 동작함
- self.console은 UI에서 출력할 메세지 박스 변수
- self.mode는 브라우저 실행 시 headless모드 모드로 할 것이지 아닌지를 판단하기 위함
- self.vo는 Service 클래스에게 전달한 데이터

# VO 
VO는 Value Object라고 부르며, 주로 read only 속성을 지닌 객체임

UI 또는 사용자가 구성하고 싶은 데이터는 아래와 같이 VO 클래스에 정의함


    class TemplateVO:
        def __init__(self, arg1='', arg2='' ):
            self.arg1 = arg1
            self.arg2 = arg2

- arg1, arg2는 VO 클래스의 변수
- 만약, VO 객체에서 데이터가 수정되어야 하는 경우엔 자유롭게 수정해도 무방함

# Service
Service 클래스는 셀레니움 드라이버를 실행하여 실제 테스트를 수행하는 코드를 작성하는 클래스


    class TemplateService(ChromeWebDriver, LoggerUtil):
        def __init__(self, console, param : TemplateVO, mode=''):
            ChromeWebDriver.__init__(self, mode)
            LoggerUtil.__init__(self, console)
    
            self.arg1 = param.arg1
            self.arg2 = param.arg2

- Service클래스는 ChromeWebdriver, LoggerUtil을 상속받아서 구현 필요
- ChromeWebdriver는 크롬 드라이버 실행 및 설정관련 클래스
- LoggerUtil은 콘솔창 또는 UI에 메세지를 출력하는 역할을 수행


본격적으로 수행할 테스트 코드는 아래 execute로 구현한다. 


    def execute(self):
        self.driver.get("https://www.naver.com")
        self._print_console("naver 화면 출력")


