import os
import re


def read_file(filename , remove):
    dir = os.path.dirname(__file__)+"/"+filename
    with open(dir, 'r') as file:
        data = file.read().replace(remove,'')
    data = data.split()
    return data


int_mem = read_file("intmemload.mem" ,'\t')
ext_mem = read_file("ext2memload.mem" ,'')

count = int(input("Enter count :"),16)
int_index = int(input("Enter Internal-Memory index :"),16)
int_modifier = int(input("Enter Internal-Memory modifier :"),16)
ext_index = int(input("Enter External-Memory index :"), 16)
ext_modifier = int(input("Enter External-Memory modifier :") , 16)


int_dict = dict() 
ext_dict = dict() 

for x in range(0, len(int_mem)-1 , 2):
    int_dict[int_mem[x]] = int_mem[x+1]
for x in range(0, len(ext_mem)-1 , 2):
    ext_dict[ext_mem[x]] = ext_mem[x+1]


j = ext_index

for i in range( int_index , int_index + count*int_modifier , int_modifier ):
    # print(int_dict[format(i, '04x')])
    # print(ext_dict[format(j, '04x')])

    if int_dict[format(i, '04x')] != ext_dict[format(j, '04x')]:
        print("Mismatch at ext_mem address " + format(j, '04x') )
    j = j+ext_modifier

   

