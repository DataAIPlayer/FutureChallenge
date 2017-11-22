# FutureChallenge

----
**未来已来——气象数据领航无人飞行器线路优化大赛**

- simpleSub.py 是一个未添加天气预测模型的简单路线规划代码，运行其submit_phase函数可得到提交的DataFrame类型数据，CSV文件需自行转换。
例程：
```
submit = simpleSub.submit_phase()
submit.to_csv('submit.csv',header=False,index=False)
```

- 天气预测模型（待续）
