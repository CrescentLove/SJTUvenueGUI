







### 核心库

#### datetime

datetime包含date/time/datetime三个核心类，分别用于日期，时间，日期&时间。

**基础的日期、时间及延迟计算**

```python
import datetime
datetime.date.today()
# print会显示诸如2022-02-02
datetime.timedelta(days=7)
# print会显示7days,0:00:00
datetime.date.today()+datetime.timedelta(days=7)
# print会显示2022-02-09
```

基础的格式化方法

```python
datetime.datetime.now().strftime("%Y-%m-%d")
# print会显示
datetime.datetime.now().strftime("%H:%M:%S")
```

