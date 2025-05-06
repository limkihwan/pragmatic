# Docker Hub에서 Python 검색
# python 3.11.8을 사용 할꺼라고 선언
FROM python:3.11.8

# 리눅스 환경 설정
WORKDIR /home/

RUN echo "testing"

# home에서 소스 코드 가져옴
# git hub에 <>Code를 누르면 Local탭 > HTTPS 주소를 복사하여 붙여 넣는다.
# git hub에 있는 소스코드사 이미지에 들어가게 됨
RUN git clone https://github.com/limkihwan/pragmatic.git


#RUN을 하면 home 폴더 아래에 pragmatic 폴더가 생성됨
#/home/pragmatic/ 폴더로 다시 경로 이동 해야함
WORKDIR /home/pragmatic/

# 개발환경에 설치 및 사용했던, 라이브러리를 모두 설치함.
# 개발할때 저장 했던, requirements.txt 파일
RUN pip install -r requirements.txt

RUN pip install gunicorn

#Mysql, Mariadb 사용하기위하여 라이브러리 설치
RUN pip install mysqlclient

# 임시로 사용 ENV 파일
RUN echo "SECRET_KEY=django-insecure-md#1p*j%tip&f8(7-(bre!v&p@^0ea!i*6+!o1knj!_5#$=vmf" > .env

RUN python manage.py collectstatic

# 포트 열기 : 8000번 포트로 통신할수 있도록 설정
EXPOSE 8000

# 장고컨테이너가 생성될때마다, 실행할 기본 명령어
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# Gunicorm으로 실행 명령어 작성
CMD ["bash", "-c", "python manage.py migrate --settings=pragmatic.settings.deploy && gunicorn pragmatic.wsgi --env DJANGO_SETTINGS_MODULE=pragmatic.settings.deploy --bind 0.0.0.0:8000"]
