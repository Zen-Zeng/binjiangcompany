# GitHub部署指南

## 步骤1：创建GitHub仓库

1. 登录GitHub账号
2. 点击右上角的「+」号，选择「New repository」
3. 填写仓库信息：
   - 仓库名称：建议使用 `binjiang-listed-companies` 或其他有意义的名称
   - 描述：可选，例如「杭州市滨江区上市公司发展报告」
   - 选择「Public」或「Private」
   - 不要勾选「Initialize this repository with a README」（因为我们已经有了README.md）
4. 点击「Create repository」

## 步骤2：添加远程仓库

在本地仓库目录下运行以下命令，替换 `<your-username>` 和 `<repository-name>` 为实际值：

```bash
git remote add origin https://github.com/<your-username>/<repository-name>.git
```

## 步骤3：推送代码到GitHub

```bash
git push -u origin main
```

## 步骤4：启用GitHub Pages

1. 进入GitHub仓库页面
2. 点击「Settings」选项卡
3. 在左侧菜单中点击「Pages」
4. 在「Source」部分：
   - 选择「Deploy from a branch」
   - 在「Branch」下拉菜单中选择「main」
   - 在「Folder」下拉菜单中选择「/(root)」
5. 点击「Save」

## 步骤5：获取网页链接

GitHub Pages部署完成后，你将在「Pages」设置页面看到类似以下的链接：

```
https://<your-username>.github.io/<repository-name>/merged.html
https://<your-username>.github.io/<repository-name>/merged_no_map.html
```

## 示例链接格式

- 完整版本：`https://username.github.io/repo-name/merged.html`
- 简化版本：`https://username.github.io/repo-name/merged_no_map.html`

## 注意事项

1. 第一次部署GitHub Pages可能需要几分钟时间，请耐心等待
2. 部署完成后，你可以通过浏览器访问生成的链接
3. 后续更新代码后，只需运行 `git push` 即可自动更新GitHub Pages

## 本地预览

```bash
# 启动本地HTTP服务器
python3 -m http.server 8080
```

访问地址：
- 完整版本：http://localhost:8080/merged.html
- 简化版本：http://localhost:8080/merged_no_map.html