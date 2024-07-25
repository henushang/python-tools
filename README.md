# 分享各种各样的小工具

## 文件助手

### 主要功能
- code： file-assistant
- 帮助您快速把一个目录里面的大量文件可以按照文件生成日期或者月份进行聚合后移动到新的目录里面（深浅色会随着系统变化）
- <img width="218" alt="image" src="https://github.com/user-attachments/assets/822fb755-2515-4306-9564-c9c829058076">

### 百度网盘直接下载
- 链接: https://pan.baidu.com/s/1BA7QpIPQ7a59AP4dYRZtTA?pwd=1tys 提取码: 1tys 复制这段内容后打开百度网盘手机App，操作更方便哦

### 开发者助手
- 首先假设你是有python开发经验的，如果没有先学习一下基础语法
- 环境准备，安装依赖：pip install -r requirements.txt
- 代码介绍
  - file_organizer.py 读取文件日期并且执行移动的核心代码
  - organizer_gui.py 可视化界面
- 生成可执行文件
  - for MacOS：python3 setup.py py2app 
  - for Windows: 待完善
- 如何使用？
  - dist下面会生成：organizer_gui.app，可以像正常打开APP一样打开  
  - 如果需要进行二次开发和debug，可以使用该命令打开，Error信息会输出到控制台：dist/organizer_gui.app/Contents/MacOS/organizer_gui

 


