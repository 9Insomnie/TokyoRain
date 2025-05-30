
---

# TokyoRain

[![GitHub stars](https://img.shields.io/github/stars/9Insomnie/TokyoRain?style=social)](https://github.com/9Insomnie/TokyoRain/stargazers)
[![License](https://img.shields.io/github/license/9Insomnie/TokyoRain)](https://github.com/9Insomnie/TokyoRain/blob/main/LICENSE)

---

## 项目简介

**TokyoRain** 是一款专注于生成隐蔽、混淆强且具有多种规避能力的 PowerShell 载荷的工具，适用于红队渗透测试和攻击模拟。该项目致力于帮助安全研究人员绕过终端检测与响应（EDR）、杀毒软件和防火墙，提升渗透效果和隐蔽性。

灵感来自东京的细雨，TokyoRain 载荷如同细雨般隐秘，悄无声息地渗透目标系统。

---

## 核心功能

* **多重混淆技术**：对 PowerShell 脚本进行多层混淆，防止静态分析和签名检测。
* **多种载荷模板**：支持反向Shell、命令执行、持久化后门等多种载荷类型。
* **内存执行支持**：支持将载荷直接注入内存执行，降低磁盘痕迹。
* **自动化参数配置**：通过命令行参数灵活配置攻击载荷（目标IP、端口、类型等）。
* **主流 EDR/AV 规避**：集成多种已知规避手法，提升攻击成功率。
* **兼容性强**：支持 Windows PowerShell 5.1 及以上版本，兼容多数企业环境。

---

## 环境要求

* Windows 系统
* PowerShell 5.1 及以上版本
* Git（用于克隆项目）

---

## 安装步骤

1. 克隆仓库到本地：

   ```bash
   git clone https://github.com/9Insomnie/TokyoRain.git
   cd TokyoRain
   ```

2. 确保 PowerShell 环境可用（Windows 默认自带）。

---

## 使用说明

### 基础用法

生成默认配置的 PowerShell 载荷文件：

```powershell
.\TokyoRain.ps1 -GeneratePayload -OutputPath ./payload.ps1
```

### 参数详解

| 参数                 | 说明                  | 示例               |
| ------------------ | ------------------- | ---------------- |
| `-GeneratePayload` | 生成载荷                | 必填               |
| `-OutputPath`      | 输出载荷的文件路径           | `./payload.ps1`  |
| `-Type`            | 载荷类型（ReverseShell等） | `ReverseShell`   |
| `-Lhost`           | 监听IP（反向连接目标IP）      | `192.168.1.100`  |
| `-Lport`           | 监听端口                | `4444`           |
| `-Obfuscate`       | 是否启用混淆（默认启用）        | `true` 或 `false` |
| `-MemoryExecution` | 是否支持内存执行            | `true` 或 `false` |

### 生成反向Shell示例

```powershell
.\TokyoRain.ps1 -GeneratePayload -Type ReverseShell -Lhost 192.168.1.100 -Lport 4444 -OutputPath ./rev_shell.ps1
```

### 查看帮助

```powershell
.\TokyoRain.ps1 -Help
```

---

## 注意事项

* 请确保您有合法授权后使用本工具，禁止未授权的攻击行为。
* 运行载荷时可能触发杀软报警，建议在测试环境验证。
* 载荷混淆级别越高，生成时间可能稍长。
* PowerShell执行策略可能限制脚本运行，建议调整为合适的执行策略，如 `RemoteSigned`。

---

## 贡献指南

欢迎贡献代码、报告问题或提出功能建议！
请先阅读并遵守 [行为准则](CODE_OF_CONDUCT.md) 和 [贡献指南](CONTRIBUTING.md)。

---

## 许可证

本项目采用 MIT 许可证，详见 [LICENSE](LICENSE) 文件。

---

## 免责声明

本项目仅限授权渗透测试和红队演练使用，严禁非法使用。使用者需对自身行为负责，造成的任何后果与项目作者无关。

---
