rightname = "zhukenin"
rightpsw = "zkn73757280"

id = 0

while 1:
    name = input("请输入用户名")
    psw = input("请输入密码")
    if name == rightname and psw == rightpsw:
        print("pass")
        exit(0)
    else:
        print("Faulse")
        exit(0)
