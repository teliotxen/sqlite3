from sqlalchemy import create_engine

  engine = create_engine('sqlite://"/지정하고 싶은 파일명.db"', echo=True)
  # 위 명령이 DB에 바로 연결시키는건 아니고, 이제 메모리에 인식 시키는 상황이다.
  # echo=True는 찍히는 쿼리를 볼 수 있다.