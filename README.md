## 使用python 运行代码 ##
1. C, Java, python
- use subprocess.Popen

2. 监控 time 和 memory, debug info

-  time: 
    - shell "time" return total run time
    - if dead loop, python get inner time to judge

-  memory: 
    - ulimit -v size :设置虚拟内存的最大值.单位:kb
    - if time is over, terminal the process
    
