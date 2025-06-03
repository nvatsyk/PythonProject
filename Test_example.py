
arr = [4, 4, 8, 3, 3, 3, 2, 4, 4]


print("Each element:")
for el in arr:
    print(el)


print("\nFirst 3 :")
print(arr[:3])


total_sum = sum(arr)
print(f"\nSumm of all: {total_sum}")


filtered_sum = sum(el for el in arr if el != 4)
print(f"Summ without 4: {filtered_sum}")

