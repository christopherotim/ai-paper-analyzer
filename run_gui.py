#!/usr/bin/env python3
"""
论文分析系统 - GUI版本
提供友好的图形界面进行论文分析
"""
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
import subprocess
import sys
import threading
from datetime import datetime, timedelta
from pathlib import Path
import queue
import json
import os
import platform

# 尝试导入日期选择器
try:
    from tkcalendar import DateEntry
    HAS_CALENDAR = True
except ImportError:
    HAS_CALENDAR = False

class APIKeyDialog:
    def __init__(self, parent, model_name, current_key=""):
        self.result = None
        self.model_name = model_name
        self.parent = parent

        # 创建对话框窗口 - 更大的尺寸确保所有内容都能显示
        self.dialog = tk.Toplevel(parent)
        self.dialog.title(f"配置 {model_name} API密钥")
        self.dialog.geometry("600x500")
        self.dialog.resizable(True, True)  # 允许调整大小
        self.dialog.transient(parent)
        self.dialog.grab_set()

        # 居中显示对话框
        self.center_dialog()

        self.create_widgets(current_key)

    def center_dialog(self):
        """将对话框居中显示"""
        # 更新对话框以获取实际尺寸
        self.dialog.update_idletasks()

        # 获取屏幕尺寸
        screen_width = self.dialog.winfo_screenwidth()
        screen_height = self.dialog.winfo_screenheight()

        # 对话框尺寸
        dialog_width = 600
        dialog_height = 500

        # 计算居中位置
        x = (screen_width - dialog_width) // 2
        y = (screen_height - dialog_height) // 2

        # 确保对话框在屏幕范围内
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        if x + dialog_width > screen_width:
            x = screen_width - dialog_width
        if y + dialog_height > screen_height:
            y = screen_height - dialog_height

        # 设置对话框位置
        self.dialog.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")

    def create_widgets(self, current_key):
        """创建对话框组件"""
        # 使用grid布局管理整个对话框
        self.dialog.columnconfigure(0, weight=1)
        self.dialog.rowconfigure(0, weight=1)

        # 主容器
        main_frame = ttk.Frame(self.dialog, padding="30")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        main_frame.columnconfigure(0, weight=1)

        # 标题
        title_label = ttk.Label(main_frame, text=f"🔑 配置 {self.model_name} API密钥",
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, pady=(0, 30), sticky=tk.W)

        # 说明文本
        info_text = f"""请输入您的 {self.model_name} API密钥。

配置后将会：
• 临时设置环境变量（立即生效，无需重启）
• 永久保存到系统环境变量（下次启动自动加载）

注意：API密钥将以加密形式保存到系统中。"""

        info_label = ttk.Label(main_frame, text=info_text, justify=tk.LEFT,
                              font=("Arial", 10))
        info_label.grid(row=1, column=0, pady=(0, 30), sticky=(tk.W, tk.E))

        # API密钥输入区域
        key_frame = ttk.LabelFrame(main_frame, text="API密钥", padding="15")
        key_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 20))
        key_frame.columnconfigure(0, weight=1)

        self.key_var = tk.StringVar(value=current_key)
        self.key_entry = ttk.Entry(key_frame, textvariable=self.key_var,
                                  show="*", font=("Consolas", 11))
        self.key_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))

        # 显示/隐藏密钥选项
        self.show_key = tk.BooleanVar()
        show_check = ttk.Checkbutton(key_frame, text="显示密钥",
                                    variable=self.show_key, command=self.toggle_key_visibility)
        show_check.grid(row=1, column=0, sticky=tk.W)

        # 测试连接区域
        test_frame = ttk.Frame(main_frame)
        test_frame.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=(0, 30))
        test_frame.columnconfigure(1, weight=1)

        self.test_button = ttk.Button(test_frame, text="🔍 测试连接",
                                     command=self.test_connection, width=15)
        self.test_button.grid(row=0, column=0, sticky=tk.W)

        self.test_status = ttk.Label(test_frame, text="点击测试连接",
                                    font=("Arial", 10))
        self.test_status.grid(row=0, column=1, sticky=tk.W, padx=(15, 0))

        # 分隔线
        separator = ttk.Separator(main_frame, orient='horizontal')
        separator.grid(row=4, column=0, sticky=(tk.W, tk.E), pady=(0, 20))

        # 按钮区域 - 使用简单的pack布局
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=5, column=0, sticky=(tk.W, tk.E))

        # 按钮 - 右对齐
        cancel_btn = ttk.Button(button_frame, text="❌ 取消",
                               command=self.cancel_clicked, width=12)
        cancel_btn.pack(side=tk.RIGHT, padx=(10, 0))

        ok_btn = ttk.Button(button_frame, text="✅ 确定",
                           command=self.ok_clicked, width=12)
        ok_btn.pack(side=tk.RIGHT)

        # 绑定键盘事件
        self.dialog.bind('<Return>', lambda e: self.ok_clicked())
        self.dialog.bind('<Escape>', lambda e: self.cancel_clicked())

        # 设置焦点
        self.key_entry.focus_set()

        # 确保对话框在最前面
        self.dialog.lift()
        self.dialog.attributes('-topmost', True)
        self.dialog.after_idle(lambda: self.dialog.attributes('-topmost', False))

    def toggle_key_visibility(self):
        """切换密钥显示/隐藏"""
        if self.show_key.get():
            self.key_entry.config(show="")
        else:
            self.key_entry.config(show="*")

    def test_connection(self):
        """测试API连接"""
        api_key = self.key_var.get().strip()
        if not api_key:
            self.test_status.config(text="❌ 请先输入API密钥", foreground="red")
            return

        self.test_button.config(state=tk.DISABLED, text="测试中...")
        self.test_status.config(text="正在测试连接...", foreground="blue")

        # 在新线程中测试连接
        def test_thread():
            try:
                # 根据模型类型进行实际的API测试
                success, message = self.test_api_key(self.model_name, api_key)

                # 更新UI（需要在主线程中执行）
                if success:
                    self.dialog.after(0, lambda: self.test_status.config(text=f"✅ {message}", foreground="green"))
                else:
                    self.dialog.after(0, lambda: self.test_status.config(text=f"❌ {message}", foreground="red"))

                self.dialog.after(0, lambda: self.test_button.config(state=tk.NORMAL, text="🔍 测试连接"))

            except Exception as e:
                self.dialog.after(0, lambda: self.test_status.config(text=f"❌ 测试异常: {str(e)}", foreground="red"))
                self.dialog.after(0, lambda: self.test_button.config(state=tk.NORMAL, text="🔍 测试连接"))

        threading.Thread(target=test_thread, daemon=True).start()

    def test_api_key(self, model_name, api_key):
        """测试API密钥有效性"""
        try:
            model_lower = model_name.lower()
            if model_lower == 'zhipu':
                return self.test_zhipu_api(api_key)
            elif model_lower == 'doubao':
                return self.test_doubao_api(api_key)
            elif model_lower == 'openai':
                return self.test_openai_api(api_key)
            elif model_lower == 'qwen':
                return self.test_qwen_api(api_key)
            elif model_lower == 'ernie':
                return self.test_ernie_api(api_key)
            elif model_lower == 'hunyuan':
                return self.test_hunyuan_api(api_key)
            else:
                return False, f"不支持的模型: {model_name}"
        except Exception as e:
            return False, f"测试失败: {str(e)}"

    def test_zhipu_api(self, api_key):
        """测试智谱AI API密钥"""
        try:
            import requests
            import json

            # 智谱AI API测试端点
            url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }

            # 使用配置文件中的默认模型进行测试
            data = {
                "model": "GLM-4.5-Air",  # 使用配置文件中的默认模型
                "messages": [
                    {"role": "user", "content": "测试连接"}
                ],
                "max_tokens": 5,
                "temperature": 0.1
            }

            response = requests.post(url, headers=headers, json=data, timeout=15)

            if response.status_code == 200:
                try:
                    result = response.json()
                    if 'choices' in result and len(result['choices']) > 0:
                        return True, "连接成功，API密钥有效"
                    else:
                        return True, "连接成功，但响应格式异常"
                except json.JSONDecodeError:
                    return True, "连接成功，但响应解析失败"
            elif response.status_code == 401:
                return False, "API密钥无效或已过期"
            elif response.status_code == 403:
                return False, "API密钥权限不足，请检查模型访问权限"
            elif response.status_code == 429:
                return False, "请求频率过高，请稍后再试"
            elif response.status_code == 400:
                try:
                    error_info = response.json()
                    error_msg = error_info.get('error', {}).get('message', '请求参数错误')
                    return False, f"请求错误: {error_msg}"
                except:
                    return False, "请求参数错误"
            else:
                try:
                    error_info = response.json()
                    error_msg = error_info.get('error', {}).get('message', f'HTTP {response.status_code}')
                    return False, f"连接失败: {error_msg}"
                except:
                    return False, f"连接失败 (状态码: {response.status_code})"

        except requests.exceptions.Timeout:
            return False, "连接超时，请检查网络连接"
        except requests.exceptions.ConnectionError:
            return False, "网络连接失败，请检查网络设置"
        except ImportError:
            return False, "缺少requests库，请安装: pip install requests"
        except Exception as e:
            return False, f"测试失败: {str(e)}"

    def test_doubao_api(self, api_key):
        """测试豆包AI API密钥"""
        try:
            import requests
            import json

            # 豆包AI API测试端点（使用配置文件中的信息）
            url = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"

            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }

            # 使用配置文件中的默认模型进行测试
            data = {
                "model": "doubao-pro-32k",  # 使用配置文件中的默认模型
                "messages": [
                    {"role": "user", "content": "测试连接"}
                ],
                "max_tokens": 5,
                "temperature": 0.1
            }

            response = requests.post(url, headers=headers, json=data, timeout=15)

            if response.status_code == 200:
                try:
                    result = response.json()
                    if 'choices' in result and len(result['choices']) > 0:
                        return True, "连接成功，API密钥有效"
                    else:
                        return True, "连接成功，但响应格式异常"
                except json.JSONDecodeError:
                    return True, "连接成功，但响应解析失败"
            elif response.status_code == 401:
                return False, "API密钥无效或已过期"
            elif response.status_code == 403:
                return False, "API密钥权限不足，请检查模型访问权限"
            elif response.status_code == 429:
                return False, "请求频率过高，请稍后再试"
            elif response.status_code == 400:
                try:
                    error_info = response.json()
                    error_msg = error_info.get('error', {}).get('message', '请求参数错误')
                    return False, f"请求错误: {error_msg}"
                except:
                    return False, "请求参数错误"
            else:
                try:
                    error_info = response.json()
                    error_msg = error_info.get('error', {}).get('message', f'HTTP {response.status_code}')
                    return False, f"连接失败: {error_msg}"
                except:
                    return False, f"连接失败 (状态码: {response.status_code})"

        except requests.exceptions.Timeout:
            return False, "连接超时，请检查网络连接"
        except requests.exceptions.ConnectionError:
            return False, "网络连接失败，请检查网络设置"
        except ImportError:
            return False, "缺少requests库，请安装: pip install requests"
        except Exception as e:
            return False, f"测试失败: {str(e)}"

    def test_openai_api(self, api_key):
        """测试OpenAI API密钥"""
        try:
            import requests
            import json

            # OpenAI API测试端点
            url = "https://api.openai.com/v1/chat/completions"

            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }

            # 使用配置文件中的默认模型进行测试
            data = {
                "model": "gpt-4",  # 使用配置文件中的默认模型
                "messages": [
                    {"role": "user", "content": "测试连接"}
                ],
                "max_tokens": 5,
                "temperature": 0.1
            }

            response = requests.post(url, headers=headers, json=data, timeout=15)

            if response.status_code == 200:
                try:
                    result = response.json()
                    if 'choices' in result and len(result['choices']) > 0:
                        return True, "连接成功，API密钥有效"
                    else:
                        return True, "连接成功，但响应格式异常"
                except json.JSONDecodeError:
                    return True, "连接成功，但响应解析失败"
            elif response.status_code == 401:
                return False, "API密钥无效或已过期"
            elif response.status_code == 403:
                return False, "API密钥权限不足，请检查模型访问权限"
            elif response.status_code == 429:
                return False, "请求频率过高，请稍后再试"
            elif response.status_code == 400:
                try:
                    error_info = response.json()
                    error_msg = error_info.get('error', {}).get('message', '请求参数错误')
                    return False, f"请求错误: {error_msg}"
                except:
                    return False, "请求参数错误"
            else:
                try:
                    error_info = response.json()
                    error_msg = error_info.get('error', {}).get('message', f'HTTP {response.status_code}')
                    return False, f"连接失败: {error_msg}"
                except:
                    return False, f"连接失败 (状态码: {response.status_code})"

        except requests.exceptions.Timeout:
            return False, "连接超时，请检查网络连接"
        except requests.exceptions.ConnectionError:
            return False, "网络连接失败，请检查网络设置"
        except ImportError:
            return False, "缺少requests库，请安装: pip install requests"
        except Exception as e:
            return False, f"测试失败: {str(e)}"

    def test_qwen_api(self, api_key):
        """测试通义千问API密钥"""
        try:
            import requests
            import json

            # 通义千问API测试端点
            url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"

            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }

            # 使用配置文件中的默认模型进行测试
            data = {
                "model": "qwen-plus",  # 使用配置文件中的默认模型
                "input": {
                    "messages": [
                        {"role": "user", "content": "测试连接"}
                    ]
                },
                "parameters": {
                    "max_tokens": 5,
                    "temperature": 0.1
                }
            }

            response = requests.post(url, headers=headers, json=data, timeout=15)

            if response.status_code == 200:
                try:
                    result = response.json()
                    if 'output' in result and 'text' in result['output']:
                        return True, "连接成功，API密钥有效"
                    else:
                        return True, "连接成功，但响应格式异常"
                except json.JSONDecodeError:
                    return True, "连接成功，但响应解析失败"
            elif response.status_code == 401:
                return False, "API密钥无效或已过期"
            elif response.status_code == 403:
                return False, "API密钥权限不足，请检查模型访问权限"
            elif response.status_code == 429:
                return False, "请求频率过高，请稍后再试"
            elif response.status_code == 400:
                try:
                    error_info = response.json()
                    error_msg = error_info.get('message', '请求参数错误')
                    return False, f"请求错误: {error_msg}"
                except:
                    return False, "请求参数错误"
            else:
                try:
                    error_info = response.json()
                    error_msg = error_info.get('message', f'HTTP {response.status_code}')
                    return False, f"连接失败: {error_msg}"
                except:
                    return False, f"连接失败 (状态码: {response.status_code})"

        except requests.exceptions.Timeout:
            return False, "连接超时，请检查网络连接"
        except requests.exceptions.ConnectionError:
            return False, "网络连接失败，请检查网络设置"
        except ImportError:
            return False, "缺少requests库，请安装: pip install requests"
        except Exception as e:
            return False, f"测试失败: {str(e)}"

    def test_ernie_api(self, api_key):
        """测试文心一言API密钥"""
        try:
            import requests
            import json

            # 文心一言需要通过access_token进行认证，这里简化处理
            # 实际使用时需要先获取access_token
            return False, "文心一言API需要额外的secret_key，请参考百度文档配置"

        except Exception as e:
            return False, f"测试失败: {str(e)}"

    def test_hunyuan_api(self, api_key):
        """测试腾讯混元API密钥"""
        try:
            import requests
            import json

            # 腾讯混元需要特殊的签名认证，这里简化处理
            # 实际使用时需要实现腾讯云的签名算法
            return False, "腾讯混元API需要额外的secret_key和签名算法，请参考腾讯云文档配置"

        except Exception as e:
            return False, f"测试失败: {str(e)}"

    def ok_clicked(self):
        """确定按钮点击"""
        api_key = self.key_var.get().strip()
        if not api_key:
            messagebox.showerror("错误", "请输入API密钥")
            return

        self.result = api_key
        self.dialog.destroy()

    def cancel_clicked(self):
        """取消按钮点击"""
        self.result = None
        self.dialog.destroy()

class EnvironmentManager:
    """环境变量管理器"""

    @staticmethod
    def get_env_var_name(model_name):
        """根据模型名称获取环境变量名"""
        # 根据配置文件中的环境变量名称
        env_names = {
            'zhipu': 'ZHIPUAI_API_KEY',
            'doubao': 'ARK_API_KEY',  # 豆包AI使用ARK_API_KEY
            'openai': 'OPENAI_API_KEY',
            'qwen': 'DASHSCOPE_API_KEY',
            'ernie': 'QIANFAN_ACCESS_KEY',
            'hunyuan': 'HUNYUAN_SECRET_ID'
        }
        return env_names.get(model_name.lower(), f'{model_name.upper()}_API_KEY')

    @staticmethod
    def get_current_api_key(model_name):
        """获取当前的API密钥"""
        env_var = EnvironmentManager.get_env_var_name(model_name)
        return os.environ.get(env_var, "")

    @staticmethod
    def set_temporary_env_var(model_name, api_key):
        """设置临时环境变量（当前进程）"""
        env_var = EnvironmentManager.get_env_var_name(model_name)
        os.environ[env_var] = api_key
        return True

    @staticmethod
    def set_permanent_env_var(model_name, api_key):
        """设置永久环境变量（系统级别）"""
        env_var = EnvironmentManager.get_env_var_name(model_name)
        system = platform.system()

        try:
            if system == "Windows":
                # Windows系统 - 使用更安全的方法
                try:
                    import winreg
                except ImportError:
                    # Python 2 兼容
                    import _winreg as winreg

                # 设置用户环境变量
                try:
                    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                       "Environment", 0, winreg.KEY_SET_VALUE)
                    winreg.SetValueEx(key, env_var, 0, winreg.REG_SZ, api_key)
                    winreg.CloseKey(key)

                    # 尝试通知系统环境变量已更改，但不阻塞程序
                    try:
                        import ctypes
                        # 使用超时机制，避免程序挂起
                        result = ctypes.windll.user32.SendMessageTimeoutW(
                            0xFFFF, 0x001A, 0, "Environment", 0x0002, 5000, None)
                        print(f"环境变量通知结果: {result}")
                    except Exception as notify_error:
                        print(f"通知系统环境变量更改失败（不影响功能）: {notify_error}")

                    return True

                except Exception as reg_error:
                    print(f"设置Windows注册表失败: {reg_error}")
                    return False

            elif system == "Darwin":  # macOS
                # 写入到 ~/.zshrc 和 ~/.bash_profile
                home = os.path.expanduser("~")

                try:
                    # 更新 .zshrc
                    zshrc_path = os.path.join(home, ".zshrc")
                    EnvironmentManager._update_shell_file(zshrc_path, env_var, api_key)

                    # 更新 .bash_profile
                    bash_profile_path = os.path.join(home, ".bash_profile")
                    EnvironmentManager._update_shell_file(bash_profile_path, env_var, api_key)

                    return True
                except Exception as mac_error:
                    print(f"设置macOS环境变量失败: {mac_error}")
                    return False

            elif system == "Linux":
                # Linux系统
                home = os.path.expanduser("~")

                try:
                    # 更新 .bashrc
                    bashrc_path = os.path.join(home, ".bashrc")
                    EnvironmentManager._update_shell_file(bashrc_path, env_var, api_key)

                    # 更新 .profile
                    profile_path = os.path.join(home, ".profile")
                    EnvironmentManager._update_shell_file(profile_path, env_var, api_key)

                    return True
                except Exception as linux_error:
                    print(f"设置Linux环境变量失败: {linux_error}")
                    return False
            else:
                print(f"不支持的操作系统: {system}")
                return False

        except Exception as e:
            print(f"设置永久环境变量失败: {e}")
            return False

    @staticmethod
    def _update_shell_file(file_path, env_var, api_key):
        """更新shell配置文件"""
        export_line = f'export {env_var}="{api_key}"\n'

        # 读取现有内容
        lines = []
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

        # 检查是否已存在该环境变量
        found = False
        for i, line in enumerate(lines):
            if line.strip().startswith(f'export {env_var}='):
                lines[i] = export_line
                found = True
                break

        # 如果不存在，添加到文件末尾
        if not found:
            lines.append(export_line)

        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)

class PaperAnalysisGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("📊 论文分析系统")
        self.root.geometry("1200x800")
        self.root.resizable(True, True)

        # 居中显示主窗口
        self.center_window(self.root, 1200, 800)

        # 设置图标
        try:
            self.root.iconbitmap("icon.ico")
        except:
            pass

        # 创建队列用于线程通信
        self.output_queue = queue.Queue()

        # 当前运行的进程
        self.current_process = None
        self.is_running = False

        # 加载配置
        self.load_config()

        self.create_widgets()
        self.check_queue()

    def center_window(self, window, width, height):
        """将窗口居中显示"""
        # 获取屏幕尺寸
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # 计算居中位置
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        # 设置窗口位置
        window.geometry(f"{width}x{height}+{x}+{y}")

        # 确保窗口在屏幕范围内
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        if x + width > screen_width:
            x = screen_width - width
        if y + height > screen_height:
            y = screen_height - height

        window.geometry(f"{width}x{height}+{x}+{y}")
    
    def load_config(self):
        """加载系统配置"""
        try:
            with open('config/models.yaml', 'r', encoding='utf-8') as f:
                import yaml
                self.config = yaml.safe_load(f)
        except:
            self.config = {
                'ai_models': {
                    'zhipu': {'name': '智谱AI'},
                    'doubao': {'name': '豆包AI'},
                    'openai': {'name': 'OpenAI'},
                    'qwen': {'name': '通义千问'},
                    'ernie': {'name': '文心一言'},
                    'hunyuan': {'name': '腾讯混元'}
                }
            }
    
    def create_widgets(self):
        """创建界面组件"""
        # 创建主框架
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 配置网格权重
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # 创建顶部标题
        self.create_header(main_frame)
        
        # 创建主要内容区域
        content_frame = ttk.Frame(main_frame)
        content_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        content_frame.columnconfigure(1, weight=1)
        content_frame.rowconfigure(0, weight=1)
        
        # 左侧控制面板
        self.create_control_panel(content_frame)
        
        # 右侧输出面板
        self.create_output_panel(content_frame)
        
        # 底部状态栏
        self.create_status_bar(main_frame)
    
    def create_header(self, parent):
        """创建顶部标题区域"""
        header_frame = ttk.Frame(parent)
        header_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        header_frame.columnconfigure(1, weight=1)
        
        # 标题
        title_label = ttk.Label(header_frame, text="📊 论文分析系统", 
                               font=("Arial", 20, "bold"))
        title_label.grid(row=0, column=0, sticky=tk.W)
        
        # 版本信息
        version_label = ttk.Label(header_frame, text="v2.0 GUI版本", 
                                 font=("Arial", 10), foreground="gray")
        version_label.grid(row=0, column=1, sticky=tk.E)
    
    def create_control_panel(self, parent):
        """创建左侧控制面板"""
        control_frame = ttk.LabelFrame(parent, text="控制面板", padding="10")
        control_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10))
        control_frame.columnconfigure(0, weight=1)
        
        # 功能选择
        func_frame = ttk.LabelFrame(control_frame, text="功能选择", padding="10")
        func_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        func_frame.columnconfigure(0, weight=1)
        
        self.function_type = tk.StringVar(value="basic")
        ttk.Radiobutton(func_frame, text="📅 基础分析 (Basic)", 
                       variable=self.function_type, value="basic",
                       command=self.on_function_change).grid(row=0, column=0, sticky=tk.W, pady=2)
        ttk.Radiobutton(func_frame, text="🔍 进阶分析 (Advanced)", 
                       variable=self.function_type, value="advanced",
                       command=self.on_function_change).grid(row=1, column=0, sticky=tk.W, pady=2)
        
        # 日期选择
        date_frame = ttk.LabelFrame(control_frame, text="日期选择", padding="10")
        date_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        date_frame.columnconfigure(1, weight=1)
        
        ttk.Label(date_frame, text="分析日期:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        
        if HAS_CALENDAR:
            self.date_entry = DateEntry(date_frame, width=12, background='darkblue',
                                       foreground='white', borderwidth=2,
                                       date_pattern='yyyy-mm-dd')
        else:
            self.date_entry = ttk.Entry(date_frame, width=15)
            self.date_entry.insert(0, datetime.now().strftime('%Y-%m-%d'))
        self.date_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=2)
        
        # 快速日期选择
        quick_frame = ttk.Frame(date_frame)
        quick_frame.grid(row=1, column=0, columnspan=2, pady=(5, 0))
        
        ttk.Button(quick_frame, text="今天", command=self.set_today, width=8).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(quick_frame, text="昨天", command=self.set_yesterday, width=8).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(quick_frame, text="前天", command=self.set_day_before_yesterday, width=8).pack(side=tk.LEFT)
        
        # 模型选择
        model_frame = ttk.LabelFrame(control_frame, text="AI模型选择", padding="10")
        model_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        model_frame.columnconfigure(1, weight=1)

        ttk.Label(model_frame, text="AI模型:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))

        self.model_var = tk.StringVar(value="zhipu")
        model_combo = ttk.Combobox(model_frame, textvariable=self.model_var,
                                  values=list(self.config.get('ai_models', {}).keys()),
                                  state="readonly", width=15)
        model_combo.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=2)
        model_combo.bind('<<ComboboxSelected>>', lambda e: self.update_api_status())

        # API密钥配置按钮
        api_button_frame = ttk.Frame(model_frame)
        api_button_frame.grid(row=1, column=0, columnspan=2, pady=(10, 0), sticky=(tk.W, tk.E))
        api_button_frame.columnconfigure(1, weight=1)

        config_button = ttk.Button(api_button_frame, text="🔑 配置API密钥",
                                  command=self.configure_api_key, width=15)
        config_button.grid(row=0, column=0, sticky=tk.W, pady=2)

        self.api_status_label = ttk.Label(api_button_frame, text="")
        self.api_status_label.grid(row=0, column=1, sticky=tk.W, padx=(10, 0))

        # 检查当前API密钥状态
        self.update_api_status()
        
        # 高级选项
        options_frame = ttk.LabelFrame(control_frame, text="高级选项", padding="10")
        options_frame.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.silent_mode = tk.BooleanVar()
        ttk.Checkbutton(options_frame, text="静默模式（减少输出）", 
                       variable=self.silent_mode).grid(row=0, column=0, sticky=tk.W, pady=2)
        
        self.force_reprocess = tk.BooleanVar()
        ttk.Checkbutton(options_frame, text="强制重新处理", 
                       variable=self.force_reprocess).grid(row=1, column=0, sticky=tk.W, pady=2)
        
        # 控制按钮
        button_frame = ttk.Frame(control_frame)
        button_frame.grid(row=4, column=0, sticky=(tk.W, tk.E), pady=(10, 0))
        button_frame.columnconfigure(0, weight=1)
        
        self.start_button = ttk.Button(button_frame, text="🚀 开始分析", 
                                      command=self.start_analysis, style="Accent.TButton")
        self.start_button.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 5))
        
        self.stop_button = ttk.Button(button_frame, text="⏹️ 停止分析", 
                                     command=self.stop_analysis, state=tk.DISABLED)
        self.stop_button.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 5))
        
        ttk.Button(button_frame, text="📁 打开输出目录", 
                  command=self.open_output_dir).grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 5))
        
        ttk.Button(button_frame, text="🔧 批处理工具", 
                  command=self.open_batch_tool).grid(row=3, column=0, sticky=(tk.W, tk.E))
    
    def create_output_panel(self, parent):
        """创建右侧输出面板"""
        output_frame = ttk.LabelFrame(parent, text="实时输出", padding="10")
        output_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        output_frame.columnconfigure(0, weight=1)
        output_frame.rowconfigure(0, weight=1)
        
        # 输出文本框
        self.output_text = scrolledtext.ScrolledText(output_frame, height=25, width=60,
                                                    font=("Consolas", 9))
        self.output_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # 进度条
        self.progress = ttk.Progressbar(output_frame, mode='indeterminate')
        self.progress.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # 输出控制按钮
        output_control_frame = ttk.Frame(output_frame)
        output_control_frame.grid(row=2, column=0, sticky=(tk.W, tk.E))
        
        ttk.Button(output_control_frame, text="清空输出", 
                  command=self.clear_output).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(output_control_frame, text="保存日志", 
                  command=self.save_log).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(output_control_frame, text="📋 查看日志目录", 
                  command=self.open_logs).pack(side=tk.LEFT)
    
    def create_status_bar(self, parent):
        """创建底部状态栏"""
        status_frame = ttk.Frame(parent)
        status_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))
        status_frame.columnconfigure(1, weight=1)
        
        # 状态标签
        self.status_var = tk.StringVar(value="就绪")
        status_label = ttk.Label(status_frame, textvariable=self.status_var, 
                                relief=tk.SUNKEN, padding="5")
        status_label.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 10))
        
        # 时间显示
        self.time_var = tk.StringVar()
        time_label = ttk.Label(status_frame, textvariable=self.time_var, 
                              relief=tk.SUNKEN, padding="5")
        time_label.grid(row=0, column=1, sticky=tk.E)
        
        # 更新时间
        self.update_time()
    
    def on_function_change(self):
        """功能类型改变时的回调"""
        # 可以根据不同功能调整界面
        pass
    
    def set_today(self):
        """设置为今天"""
        if HAS_CALENDAR:
            self.date_entry.set_date(datetime.now().date())
        else:
            self.date_entry.delete(0, tk.END)
            self.date_entry.insert(0, datetime.now().strftime('%Y-%m-%d'))
    
    def set_yesterday(self):
        """设置为昨天"""
        yesterday = datetime.now() - timedelta(days=1)
        if HAS_CALENDAR:
            self.date_entry.set_date(yesterday.date())
        else:
            self.date_entry.delete(0, tk.END)
            self.date_entry.insert(0, yesterday.strftime('%Y-%m-%d'))
    
    def set_day_before_yesterday(self):
        """设置为前天"""
        day_before = datetime.now() - timedelta(days=2)
        if HAS_CALENDAR:
            self.date_entry.set_date(day_before.date())
        else:
            self.date_entry.delete(0, tk.END)
            self.date_entry.insert(0, day_before.strftime('%Y-%m-%d'))
    
    def validate_inputs(self):
        """验证输入参数"""
        try:
            if HAS_CALENDAR:
                date_str = self.date_entry.get()
            else:
                date_str = self.date_entry.get()
            
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            messagebox.showerror("错误", "日期格式错误，请使用 YYYY-MM-DD 格式")
            return False
    
    def build_command(self):
        """构建命令行参数"""
        cmd = [sys.executable, "run.py"]
        
        # 功能类型
        cmd.append(self.function_type.get())
        
        # 日期
        if HAS_CALENDAR:
            cmd.append(self.date_entry.get())
        else:
            cmd.append(self.date_entry.get())
        
        # 模型选择（通过环境变量或配置文件）
        # 这里可以根据需要添加模型参数
        
        return cmd
    
    def start_analysis(self):
        """开始分析"""
        if not self.validate_inputs():
            return
        
        # 清空输出区域
        if not self.silent_mode.get():
            self.output_text.delete(1.0, tk.END)
        
        # 更新界面状态
        self.is_running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.progress.start()
        self.status_var.set("分析中...")
        
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
                if not self.silent_mode.get():
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
                    self.output_queue.put(('status', '分析完成'))
                    self.output_queue.put(('output', '\n🎉 分析完成！\n'))
                else:
                    self.output_queue.put(('status', '分析失败'))
                    self.output_queue.put(('output', f'\n❌ 分析失败，退出码: {self.current_process.returncode}\n'))

        except Exception as e:
            self.output_queue.put(('status', '分析异常'))
            self.output_queue.put(('output', f'\n❌ 分析异常: {e}\n'))
        finally:
            self.output_queue.put(('finished', None))
    
    def stop_analysis(self):
        """停止分析"""
        self.is_running = False
        if self.current_process:
            self.current_process.terminate()
        self.output_queue.put(('status', '已停止'))
        self.output_queue.put(('output', '\n⏹️ 分析已停止\n'))
    
    def log_output(self, text):
        """输出日志到文本框"""
        self.output_text.insert(tk.END, text)
        self.output_text.see(tk.END)
        self.root.update_idletasks()
    
    def clear_output(self):
        """清空输出"""
        self.output_text.delete(1.0, tk.END)
    
    def save_log(self):
        """保存日志"""
        content = self.output_text.get(1.0, tk.END)
        if content.strip():
            filename = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")],
                initialname=f"analysis_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            )
            if filename:
                try:
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(content)
                    messagebox.showinfo("成功", f"日志已保存到: {filename}")
                except Exception as e:
                    messagebox.showerror("错误", f"保存失败: {e}")
        else:
            messagebox.showwarning("警告", "没有日志内容可保存")
    
    def open_output_dir(self):
        """打开输出目录"""
        import os
        import platform
        
        # 根据功能类型选择目录
        if self.function_type.get() == "basic":
            output_dir = Path("data/daily_reports")
        else:
            output_dir = Path("data/analysis_results")
        
        if output_dir.exists():
            if platform.system() == "Windows":
                os.startfile(output_dir)
            elif platform.system() == "Darwin":  # macOS
                os.system(f"open {output_dir}")
            else:  # Linux
                os.system(f"xdg-open {output_dir}")
        else:
            messagebox.showinfo("提示", f"输出目录不存在: {output_dir}")
    
    def open_batch_tool(self):
        """打开批处理工具"""
        try:
            subprocess.Popen([sys.executable, "tools/batch_processor_gui.py"])
        except Exception as e:
            messagebox.showerror("错误", f"无法启动批处理工具: {e}")
    
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
    
    def update_time(self):
        """更新时间显示"""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_var.set(current_time)
        self.root.after(1000, self.update_time)

    def configure_api_key(self):
        """配置API密钥"""
        try:
            model_name = self.model_var.get()
            current_key = EnvironmentManager.get_current_api_key(model_name)

            # 显示配置对话框
            dialog = APIKeyDialog(self.root, model_name, current_key)
            self.root.wait_window(dialog.dialog)

            if dialog.result:
                api_key = dialog.result

                # 立即设置临时环境变量
                EnvironmentManager.set_temporary_env_var(model_name, api_key)

                # 在后台线程中设置永久环境变量，避免阻塞UI
                def set_permanent_env():
                    try:
                        success = EnvironmentManager.set_permanent_env_var(model_name, api_key)

                        # 在主线程中显示结果
                        def show_result():
                            if success:
                                messagebox.showinfo("成功",
                                                  f"API密钥配置成功！\n\n"
                                                  f"• 临时环境变量已设置（立即生效）\n"
                                                  f"• 永久环境变量已保存（下次启动自动加载）\n\n"
                                                  f"现在可以开始使用 {model_name} 进行分析了。")
                            else:
                                messagebox.showwarning("部分成功",
                                                     f"API密钥临时设置成功，但永久保存失败。\n\n"
                                                     f"• 临时环境变量已设置（当前会话有效）\n"
                                                     f"• 永久环境变量保存失败（可能需要管理员权限）\n\n"
                                                     f"建议手动设置系统环境变量：\n"
                                                     f"{EnvironmentManager.get_env_var_name(model_name)}")

                            # 更新API状态显示
                            self.update_api_status()

                        # 在主线程中执行UI更新
                        self.root.after(0, show_result)

                    except Exception as e:
                        def show_error():
                            messagebox.showerror("错误", f"配置API密钥失败：{e}")
                            self.update_api_status()

                        self.root.after(0, show_error)

                # 启动后台线程
                import threading
                thread = threading.Thread(target=set_permanent_env, daemon=True)
                thread.start()

        except Exception as e:
            messagebox.showerror("错误", f"打开配置对话框失败：{e}")

    def update_api_status(self):
        """更新API密钥状态显示"""
        model_name = self.model_var.get()
        current_key = EnvironmentManager.get_current_api_key(model_name)

        if current_key:
            # 显示密钥的前几位和后几位
            masked_key = f"{current_key[:8]}...{current_key[-4:]}" if len(current_key) > 12 else "***"
            self.api_status_label.config(text=f"✅ 已配置 ({masked_key})", foreground="green")
        else:
            self.api_status_label.config(text="❌ 未配置", foreground="red")

def main():
    # 检查依赖
    if not HAS_CALENDAR:
        print("提示: 安装 tkcalendar 可获得更好的日期选择体验")
        print("安装命令: pip install tkcalendar")
    
    root = tk.Tk()
    app = PaperAnalysisGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
