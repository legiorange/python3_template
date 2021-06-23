applicatio-name
---
### target 
for test  and some icon

### 0x00 install && start
```
    virtualenv .venv
    #linux
    source .venv/bin/activate
    #Windows(cmd)
    .venv\Scripts\activate.bat
    (.venv)$pip install .

```

### 0x01 Tools Version()
|  Tools_Name   | Tools_version  |
|  ----  | ----  |
| python  | 3.x |
| pip  | 1.5.6 |
| virtualenv  | 1.11.6 |
|    |  


### 0x02 开发流程

用于开发的安装
-----------------
1.检测
2按照以下流程安装
```
(.venv)$pip install -e .


#删除.venv环境内的全部依赖库
(.venv)virtualenv –clear .venv    
#根据./setup.py安装依赖库
(.venv)pip install -e                     
```

Create requiments.txt: 
```
(.venv)$pip freeze >requirements.txt 
#安装了同样版本的程序包:
(.venv)$pip install -r requirements.txt 

Python setup.py bdist_wheel_制作用于wheel发布的程序包



```




### 0x03 Model List()
|  Mod_Name   | Remark |
|  ----  | ----  |
| compress  | 3.x |
| sound  | 1.5.6 |
| task  | 1.11.6 |
 

### TODO
-  compress - tar 
-  compress - zip
-  compress - 7z


### test 

用py.test+Hypothesis/tox/mock(web)

