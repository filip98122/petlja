n = int(input())
list_of_list_of_numbers_in_box = []
list_of_x_pos_and_sum_of_diagnole = []
for index2 in range(n):
    a = list(map(int, input().split()))
    list_of_list_of_numbers_in_box.append(a)
    list_of_x_pos_and_sum_of_diagnole.append([index2,0])
for index1 in range(n):
    for index2 in range(n):
        list_of_x_pos_and_sum_of_diagnole[index2][1]+=list_of_list_of_numbers_in_box[index1][list_of_x_pos_and_sum_of_diagnole[index2][0]]
        list_of_x_pos_and_sum_of_diagnole[index2][0]+=1
        if list_of_x_pos_and_sum_of_diagnole[index2][0]==n:
            list_of_x_pos_and_sum_of_diagnole[index2][0]-=n
sve = list_of_x_pos_and_sum_of_diagnole[0][1]
for index2 in range(n):
    print(list_of_x_pos_and_sum_of_diagnole[index2][1])
    if list_of_x_pos_and_sum_of_diagnole[index2][1]==sve:
        pass
    else:
        sve = -1
if sve==-1:
    print("ne")
else:
    print("da")