# 🌐 网站部署完全免费指南

> 将你的《幽灵城堡》莎士比亚戏剧网站部署到公网，让全世界都能访问！

---

## 📋 目录
- [为什么选择 Render](#为什么选择-render)
- [准备工作](#准备工作)
- [第一步：创建 GitHub 仓库](#第一步创建-github-仓库)
- [第二步：使用 Render 部署](#第二步使用-render-部署)
- [第三步：访问与分享](#第三步访问与分享)
- [其他免费方案](#其他免费方案)
- [常见问题](#常见问题)

---

## ✨ 为什么选择 Render

| 特性 | 说明 |
|------|------|
| 🆓 完全免费 | 个人项目每月有 750 小时免费额度 |
| 🚀 一键部署 | 连接 GitHub，自动构建和部署 |
| 🔐 自动 HTTPS | 免费 SSL 证书，安全加密 |
| 🌍 CDN 加速 | 全球内容分发网络 |
| 📈 自动扩容 | 访问量增加时自动扩容 |

---

## 📦 准备工作

### 需要的东西

1. ✅ 一个 GitHub 账号（免费）
2. ✅ 你的网站代码（已在 `new_made` 文件夹中）
3. ✅ 约 15 分钟时间

### 已配置好的文件

这个项目已经准备好了部署所需的文件：

| 文件 | 用途 |
|------|------|
| `requirements.txt` | Python 依赖包列表 |
| `Procfile` | Render 启动命令 |
| `app.py` | Flask 应用程序 |

---

## 🚀 第一步：创建 GitHub 仓库

### 1.1 初始化 Git

在 `new_made` 文件夹中打开命令行（PowerShell 或 CMD）：

```bash
cd d:\1A\AIfucking_buiding\new_made
```

初始化 Git 仓库：

```bash
git init
```

### 1.2 添加并提交代码

```bash
git add .
git commit -m "Initial commit: Ghost Castle Shakespeare play website"
```

### 1.3 在 GitHub 创建新仓库

1. 访问：https://github.com/new
2. 填写信息：
   - **Repository name**: `ghost-castle-play` (或你喜欢的名字)
   - **Description**: 莎士比亚风格悲剧《幽灵城堡》网站
   - **Public/Private**: 选择 Public（推荐，免费）或 Private
3. 不要勾选 "Initialize this repository" 选项
4. 点击 "Create repository"

### 1.4 推送到 GitHub

按照 GitHub 页面上的说明操作：

```bash
git remote add origin https://github.com/你的用户名/ghost-castle-play.git
git branch -M main
git push -u origin main
```

输入你的 GitHub 用户名和密码（或 Personal Access Token）。

---

## 🌟 第二步：使用 Render 部署

### 2.1 注册 Render 账号

1. 访问：https://render.com
2. 点击 "Get Started"
3. 使用 GitHub 账号登录（推荐）

### 2.2 创建新的 Web Service

1. 登录后，点击右上角的 "+ New"
2. 选择 "Web Service"
3. 找到并选择你的 `ghost-castle-play` 仓库
4. 点击 "Connect"

### 2.3 配置部署设置

填写以下配置：

| 配置项 | 填写内容 |
|--------|----------|
| **Name** | `ghost-castle-play` (或你的项目名) |
| **Region** | 选择 `Singapore` (新加坡，离中国近，速度快) |
| **Branch** | `main` |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app --preload` |
| **Instance Type** | 选择 `Free` (免费) |

**高级设置**（可选）：
- 点击 "Advanced" 可以添加环境变量
- 本项目不需要额外配置

### 2.4 开始部署

1. 检查所有配置是否正确
2. 点击 "Create Web Service" 按钮
3. Render 将开始自动构建和部署
4. 等待 2-5 分钟，首次部署需要一些时间

### 2.5 部署成功！

当看到：
- 状态显示 "Live"
- 有一个类似 `https://ghost-castle-play.onrender.com` 的网址

恭喜！你的网站已经上线了！

---

## 🎉 第三步：访问与分享

### 访问网站

点击 Render 控制台中的链接，或直接在浏览器中访问：

```
https://ghost-castle-play.onrender.com
```

### 分享给朋友

你可以将这个链接分享给任何人，他们可以随时访问你的网站！

### 自定义域名（可选）

Render 支持绑定自定义域名：

1. 在 Render 控制台，点击 "Settings"
2. 找到 "Custom Domains" 部分
3. 点击 "Add Custom Domain"
4. 输入你的域名（如 `ghost-castle.yourdomain.com`）
5. 按照提示配置 DNS 记录

免费方案也支持自定义域名！

---

## 🔄 自动部署

### 后续更新

以后每次你将代码推送到 GitHub 的 main 分支，Render 都会自动重新部署：

```bash
git add .
git commit -m "更新内容描述"
git push
```

Render 会检测到更新，自动构建并部署最新版本！

---

## 🎯 其他免费方案

如果你想尝试其他平台，这里还有一些选择：

### 方案 B：Railway

**网址**：https://railway.app

**优点**：
- 非常简单易用
- 免费额度慷慨
- 支持 PostgreSQL 等数据库

**部署步骤**：
1. 连接 GitHub 仓库
2. 一键部署
3. 完成！

### 方案 C：Fly.io

**网址**：https://fly.io

**优点**：
- 全球 CDN 加速
- 支持 CLI 部署
- 免费额度充足

### 方案 D：Vercel

**网址**：https://vercel.com

**优点**：
- 部署超快
- 免费额度大
- 主要适合前端/Next.js

---

## 🔧 常见问题

### Q: 免费版有限制吗？

**A**: Render 免费版：
- 每月 750 小时运行时间（足够个人使用）
- 闲置 15 分钟后会休眠（首次访问会有 1-2 秒启动时间）
- 带宽和存储足够个人项目使用

### Q: 网站访问速度慢怎么办？

**A**: 
- 在 Render 选择离你近的区域（如 Singapore）
- 后续访问会很快，因为有 CDN 缓存

### Q: 我想使用自己的域名？

**A**: Render 免费版也支持自定义域名！在 Settings → Custom Domains 中添加即可。

### Q: 部署失败了怎么办？

**A**: 
1. 检查 `requirements.txt` 是否正确
2. 查看 Render 控制台的日志（Logs 标签）
3. 确保没有语法错误
4. 如果问题持续，可以尝试重新部署

### Q: 如何查看访问日志？

**A**: 在 Render 控制台：
- 点击你的 Web Service
- 选择 "Logs" 标签
- 可以看到实时的访问和错误日志

---

## 📞 获取帮助

- Render 文档：https://render.com/docs
- Flask 文档：https://flask.palletsprojects.com/
- GitHub 帮助：https://docs.github.com/

---

## 🎊 总结

你现在拥有：
✅ 完全免费的网站托管
✅ 全球可访问的公网链接
✅ 自动 HTTPS 加密
✅ GitHub 自动部署
✅ CDN 内容加速

现在就去分享你的《幽灵城堡》网站吧！🎭

---

**文档版本**: 1.0  
**最后更新**: 2026-05-21  
**维护者**: 你的名字
