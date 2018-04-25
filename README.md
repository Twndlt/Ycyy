# YCYY
优易数据协同项目

## Contributors

* [se7en](https://github.com/litt1eseven/Ycyy)
* [唐诚](https://github.com/woxingyiyi/Ycyy)
* [徐家琪](https://github.com/xujiaqi/Ycyy)
* [王鹏程](https://github.com/Twndlt/Ycyy.git)
* [辅小红](https://github.com/fxiaohong/Ycyy)
* [崔燕南](https://github.com/c502556190/Ycyy)
* [许明伟](https://github.com/CherishMIWD/Ycyy)
* [郭扛扛](https://github.com/631540886/Ycyy)
* [陈海源](https://github.com/chenhaiyuan53880/Ycyy)
* [李晶](https://github.com/irisvv/Ycyy)

## deploy（后期加）
**Docker部署**

- `将整个项目克隆，进入ycyy`

- `特别注意：数据库要配置正确`

- `执行 ./build_docker.sh`

- `等待执行完成，运行 http://localhost 查看即可`

## doc(如果不用docker)
**下载对应的库：** 
- `pip install -r requirements.txt`

**进入到目录:**
- `export FLASK_APP=manage.py`
- `export FLASK_DEBUG=1`

**初始化数据库:**
- `flask db init`
- `flask db migrate -m "init database"`
- `flask db upgrade`

**创建管理员:**
```
from flask.models import db,User
user = User(email='shiyanlou@admin.com',username='admin',password='admin123')
db.session.add(user)
db.session.commit()
exit() # 退出
```

**运行项目:**
- `flask run`
>-p port
 -h host

**管理员登录**
- `username: ycyy@admin.com | password: ycyy123`

**使用管理员登录后访问控制台**
>访问后将展示用户列表信息

**演示**
暂时删掉
暂不公开
