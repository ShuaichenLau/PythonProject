# -*- coding: utf-8 -*-
"""
Python 3.7 标准库 time 模块 使用示例
"""

import datetime
import time

# ============================================================
# 1. time.time() —— 获取当前时间戳（自1970-01-01 00:00:00 UTC 起的秒数）
# ============================================================
timestamp = time.time()
print("当前时间戳:", timestamp)   # 例如: 1690000000.123456
# 注意：返回的是 float，包含微秒级精度（依赖平台）


# ============================================================
# 2. time.sleep(seconds) —— 让程序暂停执行指定的秒数
# ============================================================
print("开始休眠...")
time.sleep(1.5)   # 暂停 1.5 秒，可以传小数
print("休眠结束")


date= datetime.date.today()
# weekday() → 从 0 开始，周一 = 0（程序员风格）
print(date.weekday())
# isoweekday() → 从 1 开始，周一 = 1（ISO 8601 国际标准，更符合人类习惯）
print(date.isoweekday())



# ============================================================
# 3. time.localtime([secs]) —— 把时间戳转换为本地时间的 struct_time
# ============================================================
local_time = time.localtime(timestamp)
print("本地时间 struct_time:", local_time)
# struct_time 是一个类似 namedtuple 的对象，包含以下字段：
print("年:", local_time.tm_year)
print("月:", local_time.tm_mon)
print("日:", local_time.tm_mday)
print("时:", local_time.tm_hour)
print("分:", local_time.tm_min)
print("秒:", local_time.tm_sec)
print("星期几(0=周一):", local_time.tm_wday)
print("一年中的第几天:", local_time.tm_yday)
print("是否夏令时:", local_time.tm_isdst)  # 0/1/-1


# ============================================================
# 4. time.gmtime([secs]) —— 把时间戳转换为 UTC 时间的 struct_time
# ============================================================
utc_time = time.gmtime(timestamp)
print("UTC 时间 struct_time:", utc_time)


# ============================================================
# 5. time.mktime(struct_time) —— 把本地时间 struct_time 转换回时间戳
#    是 localtime() 的逆操作
# ============================================================
ts_back = time.mktime(local_time)
print("转换回的时间戳:", ts_back)


# ============================================================
# 6. time.strftime(format, [t]) —— 把 struct_time 格式化为字符串
# ============================================================
formatted = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("格式化后的时间字符串:", formatted)

# 常用格式化占位符：
# %Y 四位年份   %m 月份(01-12)   %d 日(01-31)
# %H 24小时制小时  %I 12小时制小时  %M 分钟  %S 秒
# %A 星期全称   %a 星期简称   %B 月份全称   %b 月份简称
# %p AM/PM     %j 一年中的第几天  %% 百分号本身
print(time.strftime("%A, %B %d, %Y", local_time))  # 例如: Sunday, July 21, 2023


# ============================================================
# 7. time.strptime(string, format) —— 把字符串解析为 struct_time
#    是 strftime() 的逆操作
# ============================================================
time_str = "2023-07-21 10:30:00"
parsed = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
print("解析后的 struct_time:", parsed)


# ============================================================
# 8. time.asctime([t]) —— 把 struct_time 转成固定格式的字符串
#    格式类似: 'Sun Jul 21 10:30:00 2023'
# ============================================================
print("asctime 格式:", time.asctime(local_time))
print("不带参数默认使用当前时间:", time.asctime())


# ============================================================
# 9. time.ctime([secs]) —— 把时间戳转成固定格式字符串
#    等价于 time.asctime(time.localtime(secs))
# ============================================================
print("ctime 格式:", time.ctime(timestamp))
print("不带参数默认当前时间:", time.ctime())


# ============================================================
# 10. time.perf_counter() —— 高精度性能计数器（用于计算代码耗时）
#     不受系统时间修改影响，只保证相对值有意义
# ============================================================
start = time.perf_counter()
sum_ = 0
for i in range(1000000):
    sum_ += i
end = time.perf_counter()
print("perf_counter 耗时(秒):", end - start)


# ============================================================
# 11. time.process_time() —— 当前进程的CPU时间（不包括sleep等待时间）
#     常用于统计代码占用CPU的时间，而非墙钟时间
# ============================================================
start_cpu = time.process_time()
sum_ = 0
for i in range(1000000):
    sum_ += i
time.sleep(1)  # 这段睡眠不会计入 process_time
end_cpu = time.process_time()
print("process_time 耗时(秒, 不含sleep):", end_cpu - start_cpu)


# ============================================================
# 12. time.monotonic() —— 单调时钟，保证时间只会增加，不会因系统时间调整而倒退
#     适合用来测量时间间隔（比 time.time() 更安全）
# ============================================================
m_start = time.monotonic()
time.sleep(0.5)
m_end = time.monotonic()
print("monotonic 耗时(秒):", m_end - m_start)


# ============================================================
# 13. time.time_ns() / perf_counter_ns() / monotonic_ns() (Python 3.7新增!)
#     返回整数纳秒级精度，避免浮点数精度损失
# ============================================================
print("纳秒级时间戳:", time.time_ns())
print("纳秒级性能计数器:", time.perf_counter_ns())
print("纳秒级单调时钟:", time.monotonic_ns())


# ============================================================
# 14. time.timezone / time.altzone / time.daylight / time.tzname
#     获取时区相关信息
# ============================================================
print("UTC与本地标准时间差(秒), 西为正:", time.timezone)
print("UTC与本地夏令时时间差(秒):", time.altzone)
print("当地是否使用夏令时(1是0否):", time.daylight)
print("时区名称(标准时,夏令时):", time.tzname)


# ============================================================
# 15. time.clock() 在 Python 3.7 已被弃用（3.8中移除），
#     不推荐使用，应改用 perf_counter() 或 process_time()
# ============================================================
# time.clock()  # DeprecationWarning，不建议再用


# ============================================================
# 综合示例：计算某段代码运行耗时，并打印开始/结束的可读时间
# ============================================================
def demo_task():
    """模拟一个耗时任务"""
    total = 0
    for i in range(5000000):
        total += i
    return total


start_readable = time.strftime("%Y-%m-%d %H:%M:%S")
start_perf = time.perf_counter()

result = demo_task()

end_perf = time.perf_counter()
end_readable = time.strftime("%Y-%m-%d %H:%M:%S")

print(f"\n任务开始时间: {start_readable}")
print(f"任务结束时间: {end_readable}")
print(f"任务耗时: {end_perf - start_perf:.6f} 秒")
print(f"计算结果: {result}")
