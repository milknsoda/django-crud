가상환경 생성/실행

.gitignore

git init

django 설치

requirements.txt 설정 (pip freeze > requirements.txt

추후에 pip install -r requirements.txt 설치



django-admin startproject

app 만들고 등록

model 정의

    - models.py (스키마)
    - makemigrations (마이그레이션 파일 생성)
    - migrate (db 반영)





```python
a = Article(title='제목', content='내용')
a.save()
# 저장을 해야만 DB에 반영
a = Article.objects.create(title='제목', content='내용')
# 따로 저장하지 않아도 반영됨
```





ORM - object-relational mapping (중요!)



Article.objects.filter(kwrd=' ') # => 무조건 리스트로 반환/ 없으면 빈 리스트

Article.objects.get(kwrd= ' ') # => 무조건 개체 반환/ 없거나 한개보다 많으면 오류