import threading
import time
cf=input("请输入只含有C,H且构成甲烷的化学式：")
C_num=cf.count("C")
H_num=cf.count("H")
total_num=len(cf)
if total_num==H_num+C_num:
    if H_num==C_num*4:
        barrier = threading.Barrier(5) 
        def release_hydrogen(i):
            print("正在组装H原子\n")
            time.sleep(1)
            barrier.wait()
            time.sleep(1)
            print("氢原子组建完成\n")
            time.sleep(2)
        def release_carbon(i):
            print("正在组装C原子\n")
            time.sleep(0.1)
            barrier.wait()
            time.sleep(0.1)
            print("C原子组装完成\n")
            time.sleep(1)
        threads = []
        a=[]
        i=0
        while i < C_num:
            i=i+1
            t = threading.Thread(target=release_carbon, args=(1,))
            threads.append(t)
            a.append("C")
            t.start()
            for i in range(4):
                t = threading.Thread(target=release_hydrogen, args=(i+1,))
                threads.append(t)
                a.append("H")
                t.start()
            for t in threads:
                t.join()
        A = "".join(a)
        print("甲烷组建成功,结果为："+A*C_num)
    else:
        print("输入中C,H个数不匹配，不能形成甲烷，请重试")
else:
    print("输入不只有C,H或C,H未大写，请重新运行并输入只含有C,H的化学式")
