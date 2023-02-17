from setuptools import setup, find_packages

setup(
   name='seriesAuto',
   version='1.0',
   description='Series Admin setup automation',
   author='Serin Jeong',
   author_email='serin.jeong@nts-corp.com',
   packages=find_packages(),
   install_requires=[
      'PyQt5>=5.15.4',
      'Selenium>=4.1.0',
      'pyinstaller>=4.5.1'
   ],  # 프로젝트에서 추가한 패키지 이름은 여기에 작성해주세요.
)
