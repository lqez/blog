Title: php - mssql with freetds
Time: 21:28:00

php에서 freetds를 통해 MSSQL서버와 통신하는 과정에서, VARBINARY 컬럼이 255글자로 잘려 들어오는 문제가 있어,
구글링을 해보았다.

해결 방법은 tds protocol의 버전을 높이는 것. freetds 기본 값은 4.2 인데, MSSQL2000이상에서는 8.0으로
설정해주면 된다. (97이전 버전은 7.0)

데비안의 경우 /etc/freetds/freetds.conf에 해당 값을 설정해주고, 추가로 [global]내의 client charset
= '...' 까지 설정해주면 OK.

