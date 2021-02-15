/**
 * time complexity: O(nV)
 * space complexity: O(nV)
 * */

/**
 * n: n件物品
 * i:  第i件物品
 * c: 一件物品的价值
 * */
// 物品数量枚举
for (int i = 1; i <= n; i++)
{
    /**
     * w[i]: 每件物品的重量, 
     * v: 容量为v的背包,
     * V: 背包真实容量
     * */
    // 重量枚举
    for (int v = w[i]; v <= V; v++)
    {
        // 状态转移方程: d[i][v]表示前i件物品恰好装入容量为v的背包中所能获得的最大价值
        dp[i][v] = max(dp[i - 1][v], dp[i - 1][v - w[i]])
    }
}

/**
 * time complexity: O(nV)
 * space complexity: O(V)
 * */
// 空间优化, 滚动数组
for (int i = 1; i <= n; i++)
{
    // 逆序枚举
    for (int v = V; v >= w[i]; v--)
    {
        //
        dp[v] = max(dp[v], dp[v - w[i]] + c[i]);
    }
};