import psycopg2

conn = psycopg2.connect(
    host="jelani.db.elephantsql.com",
    database="ezmacslm",
    user="ezmacslm",
    password="6rxnACEKjiwR_xOhI5lYvz60qwSwH-Ed")

cur = conn.cursor()
cur.execute('''
CREATE TABLE mvcompany(
    _id VARCHAR(160) NOT NULL PRIMARY KEY,
    companyCd VARCHAR(60),
    companyNm VARCHAR(160),
    companyNmEn VARCHAR(160),
    companyPartNames VARCHAR(60),
    ceoNm VARCHAR(60),
    filmoNames VARCHAR(160)
    );''')

cur.execute('''
CREATE TABLE mvcontents(
    _id VARCHAR(160) NOT NULL PRIMARY KEY,
    movieCd VARCHAR(20),
    movieNm VARCHAR(160),
    movieNmEn VARCHAR(160),
    prdtYear VARCHAR(10),
    openDt VARCHAR(10),
    typeNm VARCHAR(20),
    prdtStatNm VARCHAR(20),
    nationAlt VARCHAR(40),
    repNationNm VARCHAR(40),
    repGenreNm VARCHAR(40),
    directors VARCHAR(40),
    peopleNm VARCHAR(60),
    companys VARCHAR(40),
    companyCd VARCHAR(40),
    companyNm VARCHAR(60)
    );''')

cur.execute('''
CREATE TABLE mvactors(
    _id VARCHAR(160) NOT NULL PRIMARY KEY,
    peopleCd VARCHAR(60),
    peopleNm VARCHAR(60),
    peopleNmEn VARCHAR(60),
    repRoleNm VARCHAR(60),
    filmoNames VARCHAR(160)
    );''')

conn.commit()