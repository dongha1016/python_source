import sys
sys.stdout.reconfigure(encoding = 'utf-8')
s1 = "자료1"
s2 = "두번째 자료"

print('Content-Type:text/html;charset=utf-8\n')

print("""
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>world</title>
</head>
<body>
    <h1>월드 페이지</h1>
    자료출력 : {0}, {1}
    <br/>
    <img src="../images/cat.jpg" />
    <br/>
    <a href="../index.html">메인으로</a>
</body>
</html>
""".format(s1, s2))
