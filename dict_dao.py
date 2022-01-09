import os
name=input("请输入字典的路径，同目录直接输入文件名即可\n")
if os.path.exists(name):
    print("导入字典成功\n")
    num=input("请输入个数,eg: 20-500 or 5000\n")
    start_num = 0
    dc_list=[]
    new_dc_list=[]
    if "-" in num:
        num=num.split("-")
        start_num=num[0]
        stop_num=num[1]
    else:
        stop_num=num
        
    if str(start_num).isdigit() and str(stop_num).isdigit():
        with open(name) as f:
            dc_list=f.readlines()
            leng=len(dc_list)
            if int(start_num) < int(leng) and int(stop_num) < int(leng) and int(start_num) < int(stop_num):
                if int(start_num) == 0:
                    start_num = 1
                new_dc_list=dc_list[int(start_num)-1:int(stop_num)]
                with open("new_dict.txt","w+") as d:
                    for j in new_dc_list:
                        d.write(j)
            else:
                print("输入不合法")
    else:
        print("输入不合法")
else:
    print("文件未找到\n")
    
