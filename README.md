# tunet_py
Python命令行版TUNET

没有烦人的“联网成功”弹框，而且不需要图形界面。

参考 https://net.tsinghua.edu.cn/wired/login.js 编写

## 使用方法
- `tunet_login.py` 用于直接验证
- `tunet_login_daemon.py` 常驻内存，每5分钟检查一次连接状态，防止超时掉线
- 双击运行，按提示输入用户名密码
- 如需记住用户名或密码，请自行编辑 `.py` 文件中的 getUserInfo 函数

## License
暂无
