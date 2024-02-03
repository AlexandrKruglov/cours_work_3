import func


data = func.sorted_list()
data_executed = func.choos_executed_operation(data)
data_last_operation = func.slice_last_operation(data_executed)
print(func.output_operation(data_last_operation))
