# 🌧️ TokyoRain

让PowerShell载荷像东京细雨般隐秘

## 🚀 核心功能

- **动态混淆**：每次生成不同指纹的载荷
- **隧道穿透**：Ngrok支持内网连接
- **多会话管理**：同时处理5个连接
- **终端美化**：彩色命令行界面

## 🛠️ 快速开始

1. 克隆仓库
```bash
git clone https://github.com/9Insomnie/TokyoRain.git
cd TokyoRain
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 启动监听
```bash
# 基础模式
python tokyo.py -l 你的IP -p 端口

# 显示原始载荷
python tokyo.py -r raw

# Ngrok模式
python tokyo.py -n ngrok
```

## 🌧️ 使用示例

```
[+] 新连接: 192.168.1.15:55328  
输入会话编号 (1-3) 或 0 退出: 1

192.168.1.15:55328 > whoami
desktop-9ins0m\admin
```

## ⚠️ 注意事项

- 仅限授权测试使用
- 建议在虚拟机环境运行
- 遵守当地法律法规

## 📜 开源协议

MIT Licensed | 开发者 [9Insomnie](https://github.com/9Insomnie)
```

🖇️ 让安全测试像东京夜雨般优雅隐秘
