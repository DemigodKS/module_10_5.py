from datetime import datetime
import multiprocessing
import time
from multiprocessing import Pool, cpu_count

def read_info(*name):
    all_data = []
    for file_name in name:
        with open(file_name,'r', encoding='utf-8') as file:
            while True:
            # считываем строку
                line = file.readline()
                if line:
                    all_data.append(line.rstrip())
                else:
                    break
    #print(all_data)


if __name__ == '__main__':
    start_time = datetime.now()
    name = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
    read_info(*name)
    end_time = datetime.now()
    all_time = end_time - start_time
    print(all_time)

if __name__ == '__main__':
    name = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
    with Pool(4) as pool:
        start_time1 = datetime.now()
        pool.map(read_info, [var for var in name])
        end_time1 = datetime.now()
        all_time1 = end_time1 - start_time1
    print(all_time1)





