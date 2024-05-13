
class Secrets:
    class Email:
        emailHost = 'smtp.qq.com'
        emailPort = 25
        emailAddr = '2027810474@qq.com'
        emailPasswd = 'uwgexoldafmpbgdc'# 邮箱 SMTP 授权码，此处为虚拟，须修改

    class DataBase:
        # database information

        host = '127.0.0.1'
        user = 'root'
        passwd = '123456'  # 修改为您本地或远程的 mysql数据库信息
        db = 'test'

    class Host:  # 修改为django允许运行的网址
        allowedHost = ['localhost', '127.0.0.1', 'xxxxx']

    class RootUrl:
        webFront = 'http://127.0.0.1:8080'

        # webBack = 'http://127.0.0.1:8000'
        webBack = 'http://127.0.0.1:8080/api/api/qs'
