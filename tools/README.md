# 批处理工具使用说明

## 📋 功能介绍

批处理工具提供两种使用方式：

- **GUI 版本** (`batch_processor_gui.py`)：图形界面，用户友好
- **命令行版本** (`batch_processor.py`)：命令行界面，适合脚本调用

## 🎨 GUI 版本使用 (推荐)

### 安装依赖

```bash
python tools/install_gui_deps.py
```

### 启动 GUI

```bash
python tools/batch_processor_gui.py
```

### GUI 功能特性

- ✅ **日期选择器**：可视化日期选择，支持快速选择（今天、昨天、最近 7 天等）
- ✅ **实时输出**：处理过程实时显示
- ✅ **进度指示**：进度条显示处理状态
- ✅ **参数验证**：自动验证输入参数
- ✅ **一键操作**：点击按钮即可开始处理
- ✅ **停止控制**：可随时停止处理过程

## 💻 命令行版本使用

## 🚀 使用方法

### 1. 批量 Daily 处理

```bash
# 处理指定日期范围
python tools/batch_processor.py daily --start 2024-05-15 --end 2024-05-20

# 强制重新处理已完成的日期
python tools/batch_processor.py daily --start 2024-05-15 --end 2024-05-20 --force
```

### 2. 批量 Advanced 处理

```bash
# 自动检测所有可处理的日期
python tools/batch_processor.py advanced --auto

# 处理指定日期范围
python tools/batch_processor.py advanced --start 2024-05-15 --end 2024-05-20

# 强制重新处理已完成的日期
python tools/batch_processor.py advanced --start 2024-05-15 --end 2024-05-20 --force
```

### 3. 完整流水线处理

```bash
# Daily + Advanced 一键完成
python tools/batch_processor.py pipeline --start 2024-05-15 --end 2024-05-20

# 强制重新处理
python tools/batch_processor.py pipeline --start 2024-05-15 --end 2024-05-20 --force
```

## ⚙️ 参数说明

- `--start`: 开始日期，格式：YYYY-MM-DD
- `--end`: 结束日期，格式：YYYY-MM-DD
- `--auto`: 自动检测可处理的日期（仅限 Advanced）
- `--force`: 强制重新处理已完成的日期

## 🛡️ 安全限制

- 日期范围最大不超过 1 年（365 天）
- 自动跳过已完成的任务（除非使用--force）
- Advanced 处理需要对应的 Daily 结果作为前置条件

## 📊 输出说明

批处理完成后会显示详细统计：

- 总处理数量
- 成功数量
- 跳过数量
- 失败数量
- 失败的具体日期

## 💡 使用建议

1. **首次使用**：建议先用小范围日期测试
2. **大批量处理**：建议分批处理，避免一次处理过多日期
3. **网络问题**：如遇网络问题导致失败，可重新运行（会自动跳过已完成的）
4. **监控进度**：工具会显示实时进度和预估剩余时间

## 🔧 故障排除

### 常见错误及解决方案

1. **"未找到对应的 HF 数据"**

   - 原因：该日期没有 HuggingFace 数据
   - 解决：选择有数据的日期

2. **"缺少 daily 结果"**

   - 原因：Advanced 处理需要先完成 Daily
   - 解决：先运行 Daily 处理或使用 pipeline 模式

3. **"API 调用失败"**

   - 原因：AI API 配置问题或网络问题
   - 解决：检查 config/models.yaml 配置

4. **日期格式错误**
   - 原因：日期格式不正确
   - 解决：使用 YYYY-MM-DD 格式

## 📝 示例

```bash
# 处理一周的数据
python tools/batch_processor.py pipeline --start 2024-05-13 --end 2024-05-19

# 重新处理失败的日期
python tools/batch_processor.py daily --start 2024-05-15 --end 2024-05-15 --force

# 批量分析所有已有的daily结果
python tools/batch_processor.py advanced --auto
```
