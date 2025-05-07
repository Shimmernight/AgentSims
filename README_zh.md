# AgentSims：一个用于评估大型语言模型的开源沙盒

在 ChatGPT 等大型语言模型（LLM）盛行社区之后，如何评估其能力成为了一个开放性问题。现有评估方法存在以下缺点：（1）评估能力受限，（2）基准脆弱，（3）指标不客观。我们认为，基于任务的评估方法，即让 LLM 代理在模拟环境中完成任务，是解决上述所有问题的一站式解决方案。

我们推出了 <a href="https://www.agentsims.com/" title="AgentSims">AgentSims</a>，这是一个易于使用的基础设施，供各学科的研究人员测试他们感兴趣的特定能力。研究人员可以通过交互式 GUI 添加代理和建筑来构建他们的评估任务，或者通过几行代码部署和测试新的支持机制，例如记忆系统和规划系统。演示网站是 https://agentsims.com/。

***与其他类似系统相比，我们的系统具有更好的定制能力，因为它专为开源自定义任务构建而设计。请参阅我们的 <a href="https://arxiv.org/abs/2308.04026" title="arXiv">arXiv 论文</a>。***

![Image text](https://github.com/py499372727/AgentSims/blob/main/cover.png)

## 依赖
```
Python: 3.9.x
MySQL: 8.0.31
```
我们建议部署在 MacOS 或 Linux 上以获得更好的稳定性。

## API 密钥
为了您 API 密钥的安全，我们没有将参数文件包含在 git 中。请您自己创建以下文件：
```
config/api_key.json
```
并记住不要将其推送到 git。

文件参数示例：
```
{"gpt-4": "xxxx", "gpt-3.5": "xxxx"}
```
如果您想部署自己的模型，请参阅维基中的 <a href="https://github.com/py499372727/AgentSims/wiki" title="DOCS">文档</a>。

## 文件夹创建
运行前，请执行以下操作：
```
mkdir snapshot
mkdir logs
```
此外，我们建议在运行前修改 `config/app.json` 中的 `count_limit`（每次运行的循环次数）和 `cooldown`（运行之间的冷却时间）到合适的值，以便平衡您的 API 密钥保护和实验运行时效率。

如果在运行时遇到任何问题，请首先参考我们维基中的 <a href="https://github.com/py499372727/AgentSims/wiki" title="DOCS">文档</a>。如果问题仍未解决，请提交 issue 或直接联系我们。

--------------------------------------
要使用我们的系统，请按照以下步骤操作：

## 1. MySQL 初始化
MySQL 用于服务器端的数据存储。安装适当版本的 MySQL 后，启动 SQL 服务并按如下方式初始化：
```
use mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '';
flush privileges;

create database `llm_account` default character set utf8mb4 collate utf8mb4_unicode_ci;
create database `llm_game` default character set utf8mb4 collate utf8mb4_unicode_ci;
create database `llm_game0001` default character set utf8mb4 collate utf8mb4_unicode_ci;
create database `llm_game0002` default character set utf8mb4 collate utf8mb4_unicode_ci;
```

## 2. 安装

```bash
pip install tornado
pip install mysql-connector-python
pip install websockets
pip install openai_async
```

或
```bash
pip install -r requirements.txt
```
## 3. 设计任务
您现在可以构建任务。如果您只是想先试用系统，可以跳过此步骤。有关任务构建，请参阅维基中的 <a href="https://github.com/py499372727/AgentSims/wiki" title="DOCS">文档</a> 或我们的 <a href="https://arxiv.org/abs/2308.04026" title="arXiv">arXiv 论文</a>中的第 4.2 节开发者模式。

## 4. 运行服务器

启动服务器：
```bash
./restart.sh
```
当您在服务器终端看到
```
--------Server Started--------
```
时，服务器已成功启动。
## 5. 运行客户端
服务器成功启动后，请启动客户端。在当前版本中，我们提供了一个基于 Web 的客户端。请在浏览器中打开 `client/index.html`。

注意：有时 Web 客户端无法正确打开。我们建议您右键单击 Python IDE 中的 `index.html` 并选择"在浏览器中打开"。如果您熟悉 `nginx`，那也是一个不错的选择。

当您在服务器终端看到
```
somebody linked.
```
时，客户端已成功启动。

## 6. 创建代理和建筑
您现在可以创建代理和建筑。有关创建，请参阅维基中的 <a href="https://github.com/py499372727/AgentSims/wiki" title="DOCS">文档</a> 或我们的 <a href="https://arxiv.org/abs/2308.04026" title="arXiv">arXiv 论文</a>中的第 4.1 节用户模式。

## 7. 设置评估目标和测量方法
在 AgentSims 中，评估通过问答形式进行。每隔 k 个 tick，系统会向目标代理提出一个评估问题。您可以在 config/eval.json 中自定义目标代理、评估问题和响应测量方法。
config/eval.json 中的示例展示了一个名为"know pH"的实验。该实验会每隔 1 个 tick 询问代理 Alan"你熟悉 pH 吗？"，如果响应中包含"Yes"，则评估函数返回 True。
```
{
  "id": "know pH", # 评估的人类可读名称
  "target_nickname": "Alan", # 目标代理的名称
  "query": "Are you acquainted with pH ?", # 评估问题
  "measurement": " 'Yes' in response" # 测量方法
  "interval": 1 # 每隔 1 个 tick 评估
}
```

## 8. 运行模拟

您可以通过 Web 客户端上的按钮启动 `tick` 或 `mayor`。您也可以通过以下方式启动：
```bash
python -u tick.py
```
```bash
python -u mayor.py
```

有关 `tick` 和 `mayor` 之间的区别，请参阅我们的 <a href="https://arxiv.org/abs/2308.04026" title="arXiv">arXiv 论文</a>。

## 9. 重启
每次重启后需要执行以下重置步骤：
```
  rm -rf snapshot/app.json
```
```
  sudo mysql
  drop database llm_account;
  drop database llm_game0001;
  create database `llm_game0001` default character set utf8mb4 collate utf8mb4_unicode_ci;
  create database `llm_account` default character set utf8mb4 collate utf8mb4_unicode_ci;
```
```
 ./restart.sh
```
-------------------------------
## 作者和引用
***作者***：林嘉驹、<a href="https://twitter.com/zhaohao919041" title="twitter">赵浩然</a>*、张奥驰、吴易庭、平胡秋月、陈沁

***关于我们***：PTA Studio 是一家致力于为 NLP 社区提供更好的开源架构并为玩家带来更有趣的 AI 游戏的初创公司。

***联系我们***：zhaohaoran@buaa.edu.cn

如果您使用本仓库中的代码或数据，请引用我们的论文：
```
@misc{lin2023agentsims,
      title={AgentSims: An Open-Source Sandbox for Large Language Model Evaluation},
      author={Jiaju Lin and Haoran Zhao and Aochi Zhang and Yiting Wu and Huqiuyue Ping and Qin Chen},
      year={2023},
      eprint={2308.04026},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}
``` 