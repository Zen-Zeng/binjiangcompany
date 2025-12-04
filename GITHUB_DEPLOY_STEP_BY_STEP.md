# GitHub部署详细步骤指南

## 步骤1：在GitHub上创建仓库

1. 打开浏览器，访问 GitHub 网站：https://github.com
2. 使用您的GitHub账号登录（用户名: Zen-Zeng）
3. 在右上角点击 `+` 图标，选择 `New repository`
4. 在创建仓库页面填写以下信息：
   - **Repository name**: `binjiangcompany` (必须与本地配置一致)
   - **Description** (可选): 滨江上市公司数据分析项目
   - **Visibility**: 选择 `Public` (公开)
   - **Initialize this repository with**: 取消所有勾选（不要初始化README、.gitignore或许可证）
5. 点击 `Create repository` 按钮

## 步骤2：推送本地代码到GitHub

1. 打开终端，进入项目目录
2. 运行以下命令推送代码：
   ```bash
   git push -u origin main
   ```
3. 如果提示输入GitHub凭据，请输入您的GitHub账号密码或个人访问令牌

## 步骤3：启用GitHub Pages

1. 推送成功后，回到GitHub仓库页面
2. 点击顶部的 `Settings` 选项卡
3. 在左侧菜单中点击 `Pages`
4. 在 `Source` 部分：
   - **Branch**: 选择 `main`
   - **Folder**: 选择 `/ (root)`
5. 点击 `Save` 按钮
6. 等待几分钟，GitHub Pages就会部署成功

## 步骤4：获取访问链接

部署成功后，您将在GitHub Pages设置页面看到访问链接，格式为：
```
https://Zen-Zeng.github.io/binjiangcompany/merged.html
```

您也可以直接访问：
- 包含地图的版本：https://Zen-Zeng.github.io/binjiangcompany/merged.html
- 不包含地图的版本：https://Zen-Zeng.github.io/binjiangcompany/merged_no_map.html

## 本地预览

在部署过程中，您可以通过本地服务器预览网站：
```bash
python3 -m http.server 8080
```

然后在浏览器中访问：
- http://localhost:8080/merged.html
- http://localhost:8080/merged_no_map.html

## 常见问题排查

1. **推送失败 - Repository not found**
   - 确保仓库名称与本地配置完全一致
   - 确保您已经在GitHub上创建了该仓库

2. **GitHub Pages部署失败**
   - 检查是否选择了正确的分支和文件夹
   - 确保仓库中包含merged.html文件
   - 等待几分钟后刷新页面

3. **访问链接显示404错误**
   - 检查URL是否正确
   - 确保GitHub Pages已完成部署
   - 尝试清除浏览器缓存

如果您在部署过程中遇到任何问题，可以随时参考此指南或联系支持。