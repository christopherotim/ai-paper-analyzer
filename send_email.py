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

def check_data_availability():
    """Check if there's data available for today by looking at cleaned data file"""
    today_str = datetime.now().strftime('%Y-%m-%d')
    cleaned_file = os.path.join("data", "daily_reports", "cleaned", f"{today_str}_clean.json")
    
    print(f"Checking for cleaned data file: {cleaned_file}")
    
    if not os.path.exists(cleaned_file):
        print("Cleaned data file not found")
        return False, "No cleaned data file found"
    
    try:
        with open(cleaned_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list) and len(data) > 0:
                print(f"Found {len(data)} papers in cleaned data")
                return True, len(data)
            else:
                print("Cleaned data file is empty or not a list")
                return False, "Empty data"
    except Exception as e:
        print(f"Error reading cleaned data file: {e}")
        return False, f"Error reading file: {e}"

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

    # Check data availability first
    has_data, data_info = check_data_availability()

    # Prepare email content based on job status and data availability
    if job_status.lower() == 'success':
        if has_data:
            # Success with data - look for analysis report
            subject = f"Daily AI Paper Briefing Success - {today_str}"
            
            report_filename = f"{today_str}_report.json"
            report_filepath = os.path.join("data", "daily_reports", "reports", report_filename)
            
            print(f"Looking for analysis report: {report_filepath}")
            
            if os.path.exists(report_filepath):
                print("Analysis report found, reading...")
                try:
                    with open(report_filepath, 'r', encoding='utf-8') as f:
                        report_data = json.load(f)
                        body = f"""Hello,

Daily AI Paper Briefing generated successfully!

Statistics:
- Analysis Date: {today_str}
- Paper Count: {data_info}
- Generated Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Analysis Report Summary:
{json.dumps(report_data, indent=2, ensure_ascii=False)[:2000]}...

The complete analysis has been processed and saved.

---
AI Briefing Bot"""
                    print("Analysis report read successfully")
                except Exception as e:
                    print(f"Failed to read analysis report: {e}")
                    body = f"""Hello,

Daily AI Paper Briefing completed successfully!

Statistics:
- Analysis Date: {today_str}
- Paper Count: {data_info}
- Generated Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

The papers have been processed, but there was an issue reading the final analysis report.
Error: {e}

---
AI Briefing Bot"""
            else:
                print("Analysis report not found, but data was processed")
                body = f"""Hello,

Daily AI Paper Briefing completed successfully!

Statistics:
- Analysis Date: {today_str}
- Paper Count: {data_info}
- Generated Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

The papers have been processed successfully. The analysis report may still be generating or saved in a different location.

---
AI Briefing Bot"""
        else:
            # Success but no data available
            subject = f"Daily AI Paper Briefing - No Data Available - {today_str}"
            body = f"""Hello,

Daily AI Paper Briefing task completed successfully.

Status:
- Analysis Date: {today_str}
- Data Status: No papers available for analysis today
- Reason: {data_info}
- Completed Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

This is normal and can happen on weekends or when no new papers are published in the monitored categories.

---
AI Briefing Bot"""
    else:
        # Job failed
        subject = f"Daily AI Paper Briefing Failed - {today_str}"
        body = f"""Hello,

Daily AI Paper Briefing task execution failed.

Status:
- Analysis Date: {today_str}
- Job Status: Failed
- Data Available: {'Yes' if has_data else 'No'}
- Failed Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Please check GitHub Actions logs for detailed error information.

---
AI Briefing Bot"""

    # Create and send email - Following successful format from reference
    try:
        print(f"Connecting to email server {SMTP_HOST}:{SMTP_PORT}...")
        
        # Create email message
        msg = MIMEMultipart()
        msg['From'] = SMTP_USER
        msg['To'] = TO_EMAIL
        msg['Subject'] = Header(subject, 'utf-8')
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        # Connect to SMTP server
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        server.starttls()
        print("Logging in...")
        server.login(SMTP_USER, SMTP_PASSWORD)
        print("Sending email...")
        
        # Send email using the format from successful example
        text = msg.as_string()
        server.sendmail(SMTP_USER, [TO_EMAIL], text)
        server.quit()
        print(f"Email sent successfully! Subject: {subject}")
        
    except Exception as e:
        print(f"Email sending failed! Error: {e}")
        # Print more detailed error information for debugging
        import traceback
        print(f"Detailed error: {traceback.format_exc()}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python send_email.py <job_status>")
        sys.exit(1)
    
    status = sys.argv[1]
    send_notification(status)