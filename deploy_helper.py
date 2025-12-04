#!/usr/bin/env python3
"""
GitHub部署助手脚本
帮助用户自动执行GitHub远程仓库设置和推送命令
"""

import subprocess
import sys
import os

def run_command(cmd, cwd=None, capture_output=True):
    """执行系统命令并返回结果"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            cwd=cwd,
            capture_output=capture_output,
            text=True
        )
        return result
    except Exception as e:
        print(f"执行命令时出错: {e}")
        return None

def get_git_config():
    """获取当前Git配置信息"""
    config = {}
    result = run_command("git config --list")
    if result and result.returncode == 0:
        for line in result.stdout.strip().split('\n'):
            if '=' in line:
                key, value = line.split('=', 1)
                config[key] = value
    return config

def check_git_status():
    """检查Git仓库状态"""
    result = run_command("git status")
    if result and result.returncode == 0:
        return "working tree clean" in result.stdout
    return False

def main():
    """主函数"""
    print("=" * 50)
    print("        GitHub部署助手脚本")
    print("=" * 50)
    print()
    
    # 检查当前目录是否为Git仓库
    if not os.path.exists(".git"):
        print("❌ 当前目录不是Git仓库！")
        print("请先初始化Git仓库: git init")
        sys.exit(1)
    
    # 获取当前Git配置
    git_config = get_git_config()
    user_name = git_config.get("user.name", "")
    user_email = git_config.get("user.email", "")
    
    print("📋 当前Git配置:")
    print(f"   用户名: {user_name if user_name else '未设置'}")
    print(f"   邮箱: {user_email if user_email else '未设置'}")
    print()
    
    # 检查工作目录是否干净
    if not check_git_status():
        print("⚠️  警告: 工作目录有未提交的更改！")
        print("请先提交所有更改: git add . && git commit -m \"Initial commit\"")
        sys.exit(1)
    
    # 获取GitHub信息
    github_username = input("请输入您的GitHub用户名: ").strip()
    if not github_username:
        print("❌ 用户名不能为空！")
        sys.exit(1)
    
    repo_name = input("请输入您要创建/使用的仓库名称: ").strip()
    if not repo_name:
        print("❌ 仓库名称不能为空！")
        sys.exit(1)
    
    print()
    print("📦 正在设置远程仓库...")
    
    # 构建远程仓库URL
    remote_url = f"https://github.com/{github_username}/{repo_name}.git"
    
    # 检查是否已存在远程仓库
    result = run_command("git remote -v")
    if result and "origin" in result.stdout:
        print("⚠️  已存在远程仓库！")
        update = input("是否要更新远程仓库URL？(y/n): ").strip().lower()
        if update == "y":
            run_command(f"git remote set-url origin {remote_url}")
            print("✅ 远程仓库URL已更新")
        else:
            print("❌ 操作已取消")
            sys.exit(1)
    else:
        # 添加远程仓库
        result = run_command(f"git remote add origin {remote_url}")
        if result and result.returncode == 0:
            print("✅ 远程仓库已添加")
        else:
            print(f"❌ 添加远程仓库失败: {result.stderr if result else '未知错误'}")
            sys.exit(1)
    
    print()
    print("🚀 正在推送代码到GitHub...")
    print("   (注意：如果是第一次推送，可能需要输入GitHub凭据)")
    print()
    
    # 推送代码
    result = run_command("git push -u origin main", capture_output=False)
    
    if result and result.returncode == 0:
        print()
        print("✅ 代码推送成功！")
        print()
        print("🌐 您的仓库地址:")
        print(f"   https://github.com/{github_username}/{repo_name}")
        print()
        print("📄 接下来请配置GitHub Pages:")
        print("1. 访问上述仓库地址")
        print("2. 点击'Settings'选项卡")
        print("3. 在左侧菜单中点击'Pages'")
        print("4. 在'Source'部分选择'Deploy from a branch'")
        print("5. 选择分支'main'和文件夹'/(root)'")
        print("6. 点击'Save'")
        print()
        print("🔗 部署完成后，您的网站将可通过以下链接访问:")
        print(f"   https://{github_username}.github.io/{repo_name}/merged.html")
        print(f"   https://{github_username}.github.io/{repo_name}/merged_no_map.html")
    else:
        print()
        print("❌ 代码推送失败！")
        print("可能的原因:")
        print("1. 仓库不存在 - 请先在GitHub上创建仓库")
        print("2. 凭据错误 - 请检查GitHub用户名和密码/令牌")
        print("3. 网络问题 - 请检查网络连接")
        print()
        print("请参考DEPLOY_GITHUB.md文件了解详细部署步骤")

if __name__ == "__main__":
    main()
