# applicatio-name

# target
for test

#### 安装与启动方法

virtualenv .venv
source .venv/bin/activate
(.venv)$pip install .



### 工具版本
---
：python：3
:pip:     1.5.6
:virtualenv:1.11.6

### 开发流程

用于开发的安装
-----------------
1.检测
2按照以下流程安装
(.venv)$pip install -e .


(.venv)virtualenv –clear .venv    
#删除.venv环境内的全部依赖库
(.venv)pip install -e                     
#根据./setup.py安装依赖库

#创建requiments.txt: 
(.venv)$pip freeze >requirements.txt 
#安装了同样版本的程序包:
(.venv)$pip install -r requirements.txt 

Python setup.py bdist_wheel_制作用于wheel发布的程序包


### TODO
1.去厕所拉屎


### test 

用py.test+Hypothesis/tox/mock(web)

