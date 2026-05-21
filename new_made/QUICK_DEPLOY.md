# Ghost Castle 部署指南 - Render 快速部署

## 📋 部署准备清单

### ✅ 已自动完成的准备（我已为你做好的文件

| 文件 | 说明 |
|------|------|
| `requirements.txt` | Python依赖 (flask + gunicorn) |
| `Procfile` | Render启动命令 |
| `.gitignore` | Git忽略文件 |
| `README.md` | 项目说明 |

## 🚀 你需要手动执行的操作

---

### 第一步：创建 GitHub 仓库

1. 访问 https://github.com/new

2. 创建新仓库：
   - Repository name: `ghost-castle` (或你喜欢的名字)
   - Public/Private: 任意选择
   - ✅ 不要勾选 "Initialize this repository"（重要！

3. 点击 "Create repository"

---

### 第二步：初始化并推送到 GitHub

在 `new_made` 目录下打开 PowerShell 或命令提示符，依次执行：

```bash
# 1. 进入项目目录
cd d:\1A\AIfucking_buiding\new_made

# 2. 初始化 Git
git init

# 3. 添加所有文件
git add .

# 4. 提交
git commit -m "Initial commit: Ghost Castle website"

# 5. 连接到你的 GitHub 仓库（替换 YOUR_USERNAME）
git remote add origin https://github.com/YOUR_USERNAME/ghost-castle.git

# 6. 推送代码
git branch -M main
git push -u origin main
```

⚠️ **注意**：将 `YOUR_USERNAME` 替换为你实际的 GitHub 用户名

---

### 第三步：在 Render 上部署

1. 访问 https://render.com 并注册/登录（用 GitHub 登录推荐

2. 点击 **"+ New"** → 选择 **"Web Service"**

3. 选择你刚创建的 `ghost-castle` 仓库 → 点击 **"Connect"**

4. 填写以下配置：

   | 配置项 | 填写内容 |
   |--------|----------|
   | Name | `ghost-castle` |
   | Region | **Singapore** (选择离中国近) |
   | Branch | `main` |
   | Runtime | `Python 3` |
   | Build Command | `pip install -r requirements.txt` |
   | Start Command | `gunicorn app:app` |
   | Instance Type | **Free** (免费)** |

5. 点击 **"Create Web Service"**

---

### 第四步：等待部署完成

- 大约需要 2-5 分钟
- 状态显示 "Live" 就成功了！
- 你的网站地址类似：`https://ghost-castle.onrender.com`

---

## 📌 关键文件说明

### [requirements.txt
```txt
flask
gunicorn
```

### [Procfile](Procfile)
```
web: gunicorn app:app --preload
```

### [app.py](app.py) - 已优化过的应用，已关闭 Debug 模式

---

## 🔄 更新网站

以后要更新网站，只需要：

```bash
git add .
git commit -m "你的更新说明"
git push
```

Render 会自动检测并自动重新部署！

---

## ❓ 常见问题

**Q: 免费版有什么限制？**  
A: 免费版足够个人使用，只是闲置15分钟后会休眠（首次访问稍慢）。

**Q: 可以自定义域名吗？**  
A: 可以，在 Render Settings → Custom Domains 中添加。

**Q: 部署失败怎么办？**  
A: 检查日志在 Render 控制台 → Logs 标签页。
