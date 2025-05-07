# AgentSims 项目启动和关闭步骤

**启动步骤：**

1. **环境准备：** 确保安装了 Python (推荐 3.9.x) 和 MySQL (推荐 8.0.31)。
2. **创建配置文件：** 手动创建 `config/api_key.json` 文件，并填入你的 API 密钥。
3. **创建目录：** 执行命令 `mkdir snapshot logs` 创建必要的目录。
4. **初始化数据库：** 连接到 MySQL，并执行 README 中提供的 SQL 命令创建数据库和设置用户权限。
5. **激活虚拟环境并安装依赖：** 执行命令 `source .venv/bin/activate && pip install -r requirements.txt` 来激活虚拟环境并安装所需的 Python 库。
6. **添加脚本执行权限：** 执行命令 `chmod +x restart.sh` 为服务器启动脚本添加执行权限。
7. **启动服务器：** 执行命令 `source .venv/bin/activate && ./restart.sh` 启动后端服务器。等待看到 "----------Server Started----------" 输出。
8. **启动 Web 服务器提供客户端文件：** 在 `client` 目录下，执行命令 `python3 -m http.server 8000` 启动一个简单的 HTTP 服务器来提供客户端文件（通常在后台运行）。
9. **访问客户端：** 在浏览器中打开 `http://localhost:8000` 来访问 Web 客户端。

**关闭步骤：**

1. **停止主服务器进程：** 找到并终止运行主服务器的进程。可以使用 `pgrep -f app.py` 或 `pgrep -f restart.sh` 查找 PID，然后使用 `kill <PID>` 终止。或者尝试使用 `pkill -f app.py` 或 `pkill -f restart.sh`。
2. **停止客户端 HTTP 服务器（如果运行）：** 如果启动了客户端 HTTP 服务器，找到并终止其进程。可以使用 `pgrep -f "python3 -m http.server 8000"` 查找 PID，然后使用 `kill <PID>` 终止。或者尝试使用 `pkill -f "python3 -m http.server 8000"`
