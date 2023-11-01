class Solution{
    public int maxProfit(int[] prices){
        int res = 0;
        int minPrice = prices[0];
        for (int price:prices){
            // curr - min
            res = Math.max(price - minPrice,res);
            // update minPrice
            minPrice = Math.min(minPrice,price);
        }
        return res;
    }
}