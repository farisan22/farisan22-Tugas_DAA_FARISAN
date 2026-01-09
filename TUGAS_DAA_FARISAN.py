def knapsack_01(weights, values, capacity, n):
    # Membuat tabel DP berukuran (n+1) x (capacity+1)
    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    # Membangun tabel dp[][] secara bottom-up
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]],  dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    # Mencari item mana saja yang terpilih
    res = dp[n][capacity]
    total_value = res
    w = capacity
    items_selected = []

    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == dp[i-1][w]:
            continue
        else:
            items_selected.append(i) # Simpan ID item
            res = res - values[i-1]
            w = w - weights[i-1]
            
    return total_value, items_selected, capacity - w

# Data Item (Berat, Nilai)
names = ["Tenda", "Sleeping Bag", "Jaket", "Kompor", "Logistik", "Matras", "Powerbank", "Headlamp", "P3K", "Sepatu"]
weights = [4, 2, 1, 1, 3, 1, 1, 1, 1, 2]
values = [10, 8, 7, 6, 9, 4, 5, 5, 9, 3]
capacity = 10
n = len(values)

max_val, selected_ids, total_weight = knapsack_01(weights, values, capacity, n)

print(f"Nilai Maksimum: {max_val}")
print(f"Daftar item terpilih: {[names[i-1] for i in selected_ids]}")
print(f"Total Berat: {total_weight} kg")