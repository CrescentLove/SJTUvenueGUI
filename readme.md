







### 核心库

#### datetime
修改

datetime包含date/time/datetime三个核心类，分别用于日期，时间，日期&时间。

**基础的日期、时间及延迟计算**

```python
import datetime
datetime.date.today()
# print会显示诸如2022-02-02
datetime.timedelta(days=7)
# print会显示7days,0:00:00
datetime.date.today()+datetime.timedelta(days=7)
# print会显示2022-02-09,但是任然是一个date对象，可以通过str(datetime.date.today()+datetime.timedelta(days=7))或(xxx+xxdeltaxxx).strftime()来转字符串
```

基础的格式化方法

```python
datetime.datetime.now().strftime("%Y-%m-%d")
# print会显示xxxx-xx-xx,str类型
datetime.datetime.now().strftime("%H:%M:%S")
```



