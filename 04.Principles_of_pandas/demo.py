# def generate_pascal_row(n):
#     row = [1]
#     for i in range(1, n + 1):
#         next_element = row[i - 1] * (n - i + 1) // i
#         row.append(next_element)
#
#     return row
#
# n = int(input())
#
#
# pascal_row = generate_pascal_row(n)
#
# print(" ".join(map(str, pascal_row)))



# ____^____
# ___/|\___
# __/|||\__
# _/.|||.\_
# /..|||..\
# _/.|||.\_
# ___|||___
# ___|||___
# ___|||___
# ___|||___
# ___~~~___
# __//!\\__
# _//.!.\\_

n = int(input())
result = ["____^____","___/|\___","__/|||\__","_/.|||.\_","/..|||..\\","_/.|||.\_","___|||___","___|||___","___|||___","___|||___","___~~~___","__//!\\\__","_//.!.\\\_"]
if n > 4:
    for i in range(n-4):
        result.insert(7,"___|||___")
print('\n'.join(result))