# send_email.py (新版本)
import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from datetime import datetime
import json

# --- 从环境变量中读取机密信息 ---
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

# --- 邮件服务器配置 (以QQ邮箱为例) ---
SMTP_HOST = "smtp.qq.com"
SMTP_PORT = 587

def send_notification(job_status):
    """根据任务状态发送邮件通知"""
    print(f"📧 开始处理邮件通知，任务状态: {job_status}")
    print(f"📂 当前工作目录: {os.getcwd()}")
    
    if not all([SMTP_USER, SMTP_PASSWORD, TO_EMAIL]):
        print("❌ 错误：邮件发送所需的环境变量不完整")
        print(f"   SMTP_USER: {'✅' if SMTP_USER else '❌'}")
        print(f"   SMTP_PASSWORD: {'✅' if SMTP_PASSWORD else '❌'}")
        print(f"   TO_EMAIL: {'✅' if TO_EMAIL else '❌'}")
        sys.exit(1)
    
    print(f"✅ 环境变量检查通过")

    today_str = datetime.now().strftime('%Y-%m-%d')
    subject = ""
    body = ""

    # 1. 根据任务状态，准备邮件主题和正文内容
    if job_status.lower() == 'success':
        subject = f"✅ 每日AI简报生成成功 - {today_str}"
        
        # 构造成功报告的文件路径
        # 如: data/daily_reports/reports/2025-08-01_report.json
        report_filename = f"{today_str}_report.json"
        report_filepath = os.path.join("data", "daily_reports", "reports", report_filename)
        
        print(f"🔍 查找报告文件: {report_filepath}")
        
        if os.path.exists(report_filepath):
            print(f"✅ 找到报告文件，正在读取...")
            try:
                with open(report_filepath, 'r', encoding='utf-8') as f:
                    # 读取JSON并格式化，使其在邮件中更易读
                    report_data = json.load(f)
                    paper_count = len(report_data) if isinstance(report_data, list) else "未知"
                    body = f"""你好，

今日AI论文简报生成成功！

📊 统计信息:
• 分析日期: {today_str}
• 论文数量: {paper_count}篇
• 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📋 详细报告:
<pre>{json.dumps(report_data, indent=2, ensure_ascii=False)}</pre>

---
AI简报机器人 🤖"""
                # 使用HTML格式发送，以便<pre>标签生效
                email_format = 'html'
                print(f"✅ 报告文件读取成功，论文数量: {paper_count}")
            except Exception as e:
                print(f"❌ 读取报告文件失败: {e}")
                body = f"任务执行成功，但读取报告文件时出错：\n\n错误信息: {e}\n文件路径: {report_filepath}"
                email_format = 'plain'
        else:
            print(f"⚠️ 未找到报告文件")
            # 列出可能的文件，帮助调试
            reports_dir = os.path.join("data", "daily_reports", "reports")
            if os.path.exists(reports_dir):
                existing_files = os.listdir(reports_dir)
                print(f"📁 reports目录中的文件: {existing_files}")
            else:
                print(f"📁 reports目录不存在: {reports_dir}")
            
            body = f"""任务状态显示成功，但未找到预期的报告文件。

预期文件路径: {report_filepath}
当前工作目录: {os.getcwd()}

这可能是因为:
1. 今天没有可分析的论文数据
2. 文件生成路径与预期不符
3. 任务执行过程中出现了问题

请检查 GitHub Actions 的详细日志以确定具体原因。

---
AI简报机器人 🤖"""
            email_format = 'plain'

    else: # 任务状态为 'failure'
        subject = f"❌ 每日AI简报生成失败 - {today_str}"
        body = (
            "你好，\n\n"
            "每日AI简报生成任务执行失败。\n"
            "这可能是因为今天（例如周末）没有可供分析的数据，或者发生了其他错误。\n\n"
            "请登录到 GitHub Actions 后台查看详细的运行日志以确定原因。"
        )
        email_format = 'plain'

    # 2. 构造邮件对象
    msg = MIMEMultipart()
    msg['From'] = Header(f"AI简报机器人 <{SMTP_USER}>", 'utf-8')
    msg['To'] = Header(TO_EMAIL, 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg.attach(MIMEText(body, email_format, 'utf-8'))

    # 3. 发送邮件
    try:
        print(f"正在连接邮件服务器 {SMTP_HOST}:{SMTP_PORT}...")
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        server.starttls()
        print("正在登录邮箱...")
        server.login(SMTP_USER, SMTP_PASSWORD)
        print("正在发送邮件...")
        server.sendmail(SMTP_USER, [TO_EMAIL], msg.as_string())
        server.quit()
        print(f"邮件已成功发送！主题: {subject}")
    except Exception as e:
        print(f"邮件发送失败！错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # 这个脚本现在只接收一个参数：任务状态 ('success' 或 'failure')
    if len(sys.argv) != 2:
        print("使用方法: python send_email.py <job_status>")
        sys.exit(1)
    
    status = sys.argv[1]
    send_notification(status)