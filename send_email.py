# send_email.py - Email notification for GitHub Actions
import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from datetime import datetime
import json

# Read credentials from environment variables
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

# Email server configuration (QQ Mail example)
SMTP_HOST = "smtp.qq.com"
SMTP_PORT = 587

def send_notification(job_status):
    """Send email notification based on job status"""
    print(f"Starting email notification process, job status: {job_status}")
    print(f"Current working directory: {os.getcwd()}")
    
    if not all([SMTP_USER, SMTP_PASSWORD, TO_EMAIL]):
        print("ERROR: Missing required environment variables for email")
        print(f"   SMTP_USER: {'OK' if SMTP_USER else 'MISSING'}")
        print(f"   SMTP_PASSWORD: {'OK' if SMTP_PASSWORD else 'MISSING'}")
        print(f"   TO_EMAIL: {'OK' if TO_EMAIL else 'MISSING'}")
        sys.exit(1)
    
    print("Environment variables check passed")

    today_str = datetime.now().strftime('%Y-%m-%d')
    subject = ""
    body = ""

    # Prepare email subject and body based on job status
    if job_status.lower() == 'success':
        subject = f"Daily AI Paper Briefing Success - {today_str}"
        
        # Look for report file
        report_filename = f"{today_str}_report.json"
        report_filepath = os.path.join("data", "daily_reports", "reports", report_filename)
        
        print(f"Looking for report file: {report_filepath}")
        
        if os.path.exists(report_filepath):
            print("Report file found, reading...")
            try:
                with open(report_filepath, 'r', encoding='utf-8') as f:
                    report_data = json.load(f)
                    paper_count = len(report_data) if isinstance(report_data, list) else "unknown"
                    body = f"""Hello,

Daily AI Paper Briefing generated successfully!

Statistics:
- Analysis Date: {today_str}
- Paper Count: {paper_count}
- Generated Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Detailed Report:
{json.dumps(report_data, indent=2, ensure_ascii=False)}

---
AI Briefing Bot"""
                email_format = 'plain'
                print(f"Report file read successfully, paper count: {paper_count}")
            except Exception as e:
                print(f"Failed to read report file: {e}")
                body = f"Task completed successfully, but failed to read report file.\n\nError: {e}\nFile path: {report_filepath}"
                email_format = 'plain'
        else:
            print("Report file not found")
            # List existing files for debugging
            reports_dir = os.path.join("data", "daily_reports", "reports")
            if os.path.exists(reports_dir):
                existing_files = os.listdir(reports_dir)
                print(f"Files in reports directory: {existing_files}")
            else:
                print(f"Reports directory does not exist: {reports_dir}")
            
            body = f"""Task status shows success, but expected report file not found.

Expected file path: {report_filepath}
Current working directory: {os.getcwd()}

This might be because:
1. No paper data available for analysis today
2. File generation path differs from expected
3. Issues occurred during task execution

Please check GitHub Actions detailed logs for specific reasons.

---
AI Briefing Bot"""
            email_format = 'plain'

    else:  # Job status is 'failure'
        subject = f"Daily AI Paper Briefing Failed - {today_str}"
        body = """Hello,

Daily AI Paper Briefing task execution failed.
This might be because there's no data available for analysis today (e.g., weekends) or other errors occurred.

Please check GitHub Actions backend for detailed execution logs to determine the cause.

---
AI Briefing Bot"""
        email_format = 'plain'

    # Create email message
    msg = MIMEMultipart()
    msg['From'] = Header(f"AI Briefing Bot <{SMTP_USER}>", 'utf-8')
    msg['To'] = Header(TO_EMAIL, 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg.attach(MIMEText(body, email_format, 'utf-8'))

    # Send email
    try:
        print(f"Connecting to email server {SMTP_HOST}:{SMTP_PORT}...")
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        server.starttls()
        print("Logging in...")
        server.login(SMTP_USER, SMTP_PASSWORD)
        print("Sending email...")
        server.sendmail(SMTP_USER, [TO_EMAIL], msg.as_string())
        server.quit()
        print(f"Email sent successfully! Subject: {subject}")
    except Exception as e:
        print(f"Email sending failed! Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # This script accepts one parameter: job status ('success' or 'failure')
    if len(sys.argv) != 2:
        print("Usage: python send_email.py <job_status>")
        sys.exit(1)
    
    status = sys.argv[1]
    send_notification(status)