user_data = {"BLZ": {"SN00000001": {"M000001", "M000002"}, "SN00000002": {"M000003", "M000004"},
                     "SN00000003": {"M000005", "M000006"}}}


apparat_list = list(user_data['BLZ'].keys())

print(apparat_list)
print(len(apparat_list))

# manipula_list =

print(list(user_data['BLZ']['SN00000003']))

apparat_full_list = []
manipula_full_list = []
for i in range(50):
    apparat_full_list.append(f"apparat{i}")
    manipula_full_list.append(f"manipula{i}")

user_data = {13456: user_data}

print(user_data)



