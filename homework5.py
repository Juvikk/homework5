immutable_var = ('бобр',1721,'штандарт',True)

#immutable_var [0]= 'кваказябра'
##значение элементов кортежа нельзя изменить потому что кортеж не поддерживает обращение по элементам ''tuple' object does not support item assignment'

mutable_list = [1234,5678]
print (mutable_list)
mutable_list[1] = 11111
print(mutable_list)
