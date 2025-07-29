#!/usr/bin/env python3
"""
批处理工具 - GUI版本
提供友好的图形界面进行批量处理
"""
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import subprocess
import sys
import os
import threading
from datetime import datetime, timedelta
from pathlib import Path
import queue

# 尝试导入日期选择器，如果没有则使用普通输入框
try:
    from tkcalendar import DateEntry
    HAS_CALENDAR = True
except ImportError:
    HAS_CALENDAR = False
    print("提示: 安装 tkcalendar 可获得更好的日期选择体验")
    print("安装命令: pip install tkcalendar")

class BatchProcessorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("论文分析系统 - 批处理工具")
        self.root.geometry("800x700")
        self.root.resizable(True, True)
        
        # 设置图标（如果有的话）
        try:
            self.root.iconbitmap("icon.ico")
        except:
            pass
        
        # 创建队列用于线程通信
        self.output_queue = queue.Queue()
        
        # 当前运行的进程
        self.current_process = None
        self.is_running = False
        
        self.create_widgets()
        self.check_queue()
    
    def create_widgets(self):
        """创建界面组件"""
        # 主框架
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 配置网格权重
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # 标题
        title_label = ttk.Label(main_frame, text="📊 论文分析系统 - 批处理工具", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # 处理类型选择
        ttk.Label(main_frame, text="处理类型:", font=("Arial", 10, "bold")).grid(
            row=1, column=0, sticky=tk.W, pady=5)
        
        self.process_type = tk.StringVar(value="daily")
        type_frame = ttk.Frame(main_frame)
        type_frame.grid(row=1, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Radiobutton(type_frame, text="📅 Daily处理", variable=self.process_type, 
                       value="daily", command=self.on_type_change).pack(side=tk.LEFT, padx=(0, 20))
        ttk.Radiobutton(type_frame, text="🔍 Advanced处理", variable=self.process_type, 
                       value="advanced", command=self.on_type_change).pack(side=tk.LEFT, padx=(0, 20))
        ttk.Radiobutton(type_frame, text="🔄 完整流水线", variable=self.process_type, 
                       value="pipeline", command=self.on_type_change).pack(side=tk.LEFT)
        
        # 日期选择方式
        ttk.Label(main_frame, text="日期选择:", font=("Arial", 10, "bold")).grid(
            row=2, column=0, sticky=tk.W, pady=5)
        
        self.date_mode = tk.StringVar(value="range")
        date_mode_frame = ttk.Frame(main_frame)
        date_mode_frame.grid(row=2, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        self.range_radio = ttk.Radiobutton(date_mode_frame, text="📅 指定日期范围", 
                                          variable=self.date_mode, value="range",
                                          command=self.on_date_mode_change)
        self.range_radio.pack(side=tk.LEFT, padx=(0, 20))
        
        self.auto_radio = ttk.Radiobutton(date_mode_frame, text="🔍 自动检测", 
                                         variable=self.date_mode, value="auto",
                                         command=self.on_date_mode_change)
        self.auto_radio.pack(side=tk.LEFT)
        
        # 日期范围选择
        self.date_frame = ttk.LabelFrame(main_frame, text="日期范围", padding="10")
        self.date_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        self.date_frame.columnconfigure(1, weight=1)
        self.date_frame.columnconfigure(3, weight=1)
        
        # 开始日期
        ttk.Label(self.date_frame, text="开始日期:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        if HAS_CALENDAR:
            self.start_date = DateEntry(self.date_frame, width=12, background='darkblue',
                                       foreground='white', borderwidth=2, 
                                       date_pattern='yyyy-mm-dd')
        else:
            self.start_date = ttk.Entry(self.date_frame, width=15)
            self.start_date.insert(0, datetime.now().strftime('%Y-%m-%d'))
        self.start_date.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 20))
        
        # 结束日期
        ttk.Label(self.date_frame, text="结束日期:").grid(row=0, column=2, sticky=tk.W, padx=(0, 10))
        if HAS_CALENDAR:
            self.end_date = DateEntry(self.date_frame, width=12, background='darkblue',
                                     foreground='white', borderwidth=2,
                                     date_pattern='yyyy-mm-dd')
        else:
            self.end_date = ttk.Entry(self.date_frame, width=15)
            self.end_date.insert(0, datetime.now().strftime('%Y-%m-%d'))
        self.end_date.grid(row=0, column=3, sticky=(tk.W, tk.E))
        
        # 快速日期选择按钮
        quick_frame = ttk.Frame(self.date_frame)
        quick_frame.grid(row=1, column=0, columnspan=4, pady=(10, 0))
        
        ttk.Button(quick_frame, text="今天", command=self.set_today).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(quick_frame, text="昨天", command=self.set_yesterday).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(quick_frame, text="最近7天", command=self.set_last_week).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(quick_frame, text="最近30天", command=self.set_last_month).pack(side=tk.LEFT)
        
        # 选项
        options_frame = ttk.LabelFrame(main_frame, text="选项", padding="10")
        options_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        
        self.force_reprocess = tk.BooleanVar()
        ttk.Checkbutton(options_frame, text="强制重新处理已完成的任务", 
                       variable=self.force_reprocess).pack(anchor=tk.W)
        
        # 控制按钮
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=5, column=0, columnspan=3, pady=20)
        
        self.start_button = ttk.Button(button_frame, text="🚀 开始处理", 
                                      command=self.start_processing, style="Accent.TButton")
        self.start_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.stop_button = ttk.Button(button_frame, text="⏹️ 停止处理", 
                                     command=self.stop_processing, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Button(button_frame, text="📋 查看日志", command=self.open_logs).pack(side=tk.LEFT)
        
        # 输出区域
        output_frame = ttk.LabelFrame(main_frame, text="处理输出", padding="10")
        output_frame.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        output_frame.columnconfigure(0, weight=1)
        output_frame.rowconfigure(0, weight=1)
        main_frame.rowconfigure(6, weight=1)
        
        self.output_text = scrolledtext.ScrolledText(output_frame, height=15, width=80)
        self.output_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 进度条
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=7, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
        
        # 状态栏
        self.status_var = tk.StringVar(value="就绪")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.grid(row=8, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(5, 0))
        
        # 初始化界面状态
        self.on_type_change()
        self.on_date_mode_change()
    
    def on_type_change(self):
        """处理类型改变时的回调"""
        if self.process_type.get() == "advanced":
            self.auto_radio.config(state=tk.NORMAL)
        else:
            self.auto_radio.config(state=tk.DISABLED)
            if self.date_mode.get() == "auto":
                self.date_mode.set("range")
        self.on_date_mode_change()
    
    def on_date_mode_change(self):
        """日期模式改变时的回调"""
        if self.date_mode.get() == "auto":
            # 禁用日期选择
            for widget in self.date_frame.winfo_children():
                if isinstance(widget, (ttk.Entry, DateEntry if HAS_CALENDAR else ttk.Entry)):
                    widget.config(state=tk.DISABLED)
        else:
            # 启用日期选择
            for widget in self.date_frame.winfo_children():
                if isinstance(widget, (ttk.Entry, DateEntry if HAS_CALENDAR else ttk.Entry)):
                    widget.config(state=tk.NORMAL)
    
    def set_today(self):
        """设置为今天"""
        today = datetime.now().strftime('%Y-%m-%d')
        if HAS_CALENDAR:
            self.start_date.set_date(datetime.now().date())
            self.end_date.set_date(datetime.now().date())
        else:
            self.start_date.delete(0, tk.END)
            self.start_date.insert(0, today)
            self.end_date.delete(0, tk.END)
            self.end_date.insert(0, today)
    
    def set_yesterday(self):
        """设置为昨天"""
        yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        if HAS_CALENDAR:
            date = datetime.now().date() - timedelta(days=1)
            self.start_date.set_date(date)
            self.end_date.set_date(date)
        else:
            self.start_date.delete(0, tk.END)
            self.start_date.insert(0, yesterday)
            self.end_date.delete(0, tk.END)
            self.end_date.insert(0, yesterday)
    
    def set_last_week(self):
        """设置为最近7天"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=6)
        
        if HAS_CALENDAR:
            self.start_date.set_date(start_date.date())
            self.end_date.set_date(end_date.date())
        else:
            self.start_date.delete(0, tk.END)
            self.start_date.insert(0, start_date.strftime('%Y-%m-%d'))
            self.end_date.delete(0, tk.END)
            self.end_date.insert(0, end_date.strftime('%Y-%m-%d'))
    
    def set_last_month(self):
        """设置为最近30天"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=29)
        
        if HAS_CALENDAR:
            self.start_date.set_date(start_date.date())
            self.end_date.set_date(end_date.date())
        else:
            self.start_date.delete(0, tk.END)
            self.start_date.insert(0, start_date.strftime('%Y-%m-%d'))
            self.end_date.delete(0, tk.END)
            self.end_date.insert(0, end_date.strftime('%Y-%m-%d'))
    
    def validate_inputs(self):
        """验证输入参数"""
        if self.date_mode.get() == "range":
            try:
                if HAS_CALENDAR:
                    start_str = self.start_date.get()
                    end_str = self.end_date.get()
                else:
                    start_str = self.start_date.get()
                    end_str = self.end_date.get()
                
                start_date = datetime.strptime(start_str, '%Y-%m-%d')
                end_date = datetime.strptime(end_str, '%Y-%m-%d')
                
                if start_date > end_date:
                    messagebox.showerror("错误", "开始日期不能晚于结束日期")
                    return False
                
                if (end_date - start_date).days > 365:
                    messagebox.showerror("错误", "日期范围不能超过1年（365天）")
                    return False
                    
            except ValueError:
                messagebox.showerror("错误", "日期格式错误，请使用 YYYY-MM-DD 格式")
                return False
        
        return True
    
    def build_command(self):
        """构建命令行参数"""
        cmd = [sys.executable, "tools/batch_processor.py"]
        
        # 处理类型
        cmd.append(self.process_type.get())
        
        # 日期参数
        if self.date_mode.get() == "auto":
            cmd.append("--auto")
        else:
            if HAS_CALENDAR:
                cmd.extend(["--start", self.start_date.get()])
                cmd.extend(["--end", self.end_date.get()])
            else:
                cmd.extend(["--start", self.start_date.get()])
                cmd.extend(["--end", self.end_date.get()])
        
        # 强制重新处理
        if self.force_reprocess.get():
            cmd.append("--force")
        
        return cmd
    
    def start_processing(self):
        """开始处理"""
        if not self.validate_inputs():
            return
        
        # 清空输出区域
        self.output_text.delete(1.0, tk.END)
        
        # 更新界面状态
        self.is_running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.progress.start()
        self.status_var.set("处理中...")
        
        # 构建命令
        cmd = self.build_command()
        self.log_output(f"执行命令: {' '.join(cmd)}\n")
        
        # 在新线程中执行
        thread = threading.Thread(target=self.run_process, args=(cmd,))
        thread.daemon = True
        thread.start()
    
    def run_process(self, cmd):
        """在后台线程中运行进程"""
        try:
            # 设置环境变量以确保正确的编码处理
            env = os.environ.copy()
            if sys.platform.startswith('win'):
                # Windows下设置UTF-8编码
                env['PYTHONIOENCODING'] = 'utf-8'

            self.current_process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                universal_newlines=True,
                encoding='utf-8',
                errors='replace',  # 遇到无法解码的字符时替换而不是报错
                env=env
            )

            # 实时读取输出
            for line in iter(self.current_process.stdout.readline, ''):
                if not self.is_running:
                    break
                # 确保输出的字符串能够正确处理
                try:
                    # 尝试处理可能的编码问题
                    clean_line = line.encode('utf-8', errors='replace').decode('utf-8')
                    self.output_queue.put(('output', clean_line))
                except Exception as encoding_error:
                    # 如果还是有编码问题，使用安全的替换方式
                    safe_line = repr(line)[1:-1]  # 移除引号
                    self.output_queue.put(('output', f"[编码处理] {safe_line}\n"))

            self.current_process.wait()

            if self.is_running:
                if self.current_process.returncode == 0:
                    self.output_queue.put(('status', '处理完成'))
                    self.output_queue.put(('output', '\n🎉 批处理完成！\n'))
                else:
                    self.output_queue.put(('status', '处理失败'))
                    self.output_queue.put(('output', f'\n❌ 处理失败，退出码: {self.current_process.returncode}\n'))

        except Exception as e:
            self.output_queue.put(('status', '处理异常'))
            self.output_queue.put(('output', f'\n❌ 处理异常: {e}\n'))
        finally:
            self.output_queue.put(('finished', None))
    
    def stop_processing(self):
        """停止处理"""
        self.is_running = False
        if self.current_process:
            self.current_process.terminate()
        self.output_queue.put(('status', '已停止'))
        self.output_queue.put(('output', '\n⏹️ 处理已停止\n'))
    
    def log_output(self, text):
        """输出日志到文本框"""
        self.output_text.insert(tk.END, text)
        self.output_text.see(tk.END)
        self.root.update_idletasks()
    
    def check_queue(self):
        """检查队列中的消息"""
        try:
            while True:
                msg_type, data = self.output_queue.get_nowait()
                
                if msg_type == 'output':
                    self.log_output(data)
                elif msg_type == 'status':
                    self.status_var.set(data)
                elif msg_type == 'finished':
                    # 处理完成，恢复界面状态
                    self.is_running = False
                    self.start_button.config(state=tk.NORMAL)
                    self.stop_button.config(state=tk.DISABLED)
                    self.progress.stop()
                    break
                    
        except queue.Empty:
            pass
        
        # 继续检查队列
        self.root.after(100, self.check_queue)
    
    def open_logs(self):
        """打开日志目录"""
        import os
        import platform
        
        log_dir = Path("logs")
        if log_dir.exists():
            if platform.system() == "Windows":
                os.startfile(log_dir)
            elif platform.system() == "Darwin":  # macOS
                os.system(f"open {log_dir}")
            else:  # Linux
                os.system(f"xdg-open {log_dir}")
        else:
            messagebox.showinfo("提示", "日志目录不存在")

def main():
    root = tk.Tk()
    app = BatchProcessorGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
