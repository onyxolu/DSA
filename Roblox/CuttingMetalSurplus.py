# def max_profit(cutting_cost,sale_price,rods,cutting_size):
#     profit = 0
#     total_rods = len(rods)
#     for i in range(total_rods):
#         if rods[i]%cutting_size == 0:
#             profit+=(sale_price * rods[i]-(rods[i] // cutting_size-1) * cutting_cost)

#         else:
#             profit+=(sale_price * (rods[i] - rods[i] % cutting_size) - (rods[i] // cutting_size)* cutting_cost)


#     return profit


# cutting_cost = int(input("Cutting Cost: "))
# sale_price = int(input("Sale Price : "))
# road_number = int(input("Number of Rods : "))
# rods=[]
# for i in range(road_number):
#     rod = int(input())
#     rods.insert(i,rod)

# max_size_road = max(rods)
# maximum_profit=0
# for cutting_size in range(1,max_size_road):
#     profit = max_profit(cutting_cost,sale_price,rods,cutting_size)
    
#     if profit > maximum_profit:
#         maximum_profit=profit

# print(maximum_profit)



# public int commonPrefix(String input) {
# 	int n = input.length();
# 	if(n == 0) return 0;

# 	int res = n;
# 	char[] arr = input.toCharArray();
# 	for(int i = 1; i < n; i++) {
# 		if(arr[i] == arr[0])
# 			res += getPrefixLength(arr, i);
# 	}

# 	return res;
# }

# public int getPrefixLength(char[] arr, int start) {
# 	int res = 0, i = 0, j = start;

# 	while(j < arr.length) {
# 		if(arr[i++] == arr[j++])
# 			res++;
# 		else
# 			break;
# 	}
# 	return res;
# }
    


   public static int maxProfit(int costPerCut, int salePrice, List<Integer> lengths) {        
            int total = 0;
            int max = lengths.get(0); 
            int maxProfit = 0; 
       //get max Length
            for(int i = 0; i < lengths.size(); i++) {
               if(max < lengths.get(i)) max = lengths.get(i);  
            }
       //Time Complexity o(N*N) 
            for(int size = 1;  size <= max; size ++ ) {
               int profits = 0; 
               for(int i = 0; i < lengths.size(); i++) {
                   int length = lengths.get(i); 
                   if(size > length) continue; 
                   int currentPrice = (length/size) * salePrice * size; // current Rode price after currint it
                   int cuts = length % size == 0 ? (length/size) -1 : (length/size); // number of cuts during process; 
                   int currentProfits = currentPrice - costPerCut * cuts; 
                   if(currentProfits > 0) {
                       profits += currentProfits; 
                   }
               }
                if(profits > maxProfit) {
                    maxProfit = profits; 
                }
           }
       return maxProfit; 
   }


# public static long calculateMaximumProfit(int cost_per_cut, int metal_price, int[] lengths) {

#     long maxProfit = 0;
#     long curProfit = 0;
#     int maxLength = 0;
#     int totalRods = 0;
#     int totalCuts = 0;
#     Arrays.sort(lengths);
#     // Find out maximum length
#     for (int curLength : lengths) {
#         maxLength = Math.max(maxLength, curLength);
#     }

#     // For each of the possible rod lengths, calculate possible profit
#     for (int curLength = 1; curLength <=maxLength; curLength++) {        
#         int prevSum=0;
#         // Cut each of the rods into smaller rods of size curLength
#         // Count total rods and total cuts
#         for (int length : lengths) {
#             int cut = 0;
#             int waste = 0;
#             if(length%curLength==0){
#                 cut=(length/curLength)-1;
#             }else{
#                 cut=length/curLength;
#             }
#             waste=length%curLength;
#             int profit=Math.max(prevSum,prevSum+(length*metal_price-cut*cost_per_cut-waste*metal_price));
#             prevSum=profit;
#         }

#         curProfit=prevSum;
#         // Calculate maximum profit
#         maxProfit = Math.max(maxProfit, curProfit);
#     }

#     return maxProfit;
# }


# public static void main(String[] args) {
# 	int cutCost1 = 1, price1 = 10;
# 	int[] nums1 = {26, 59, 103};
# 	int cutCost2 = 100, price2 = 10;
# 	int[] nums2 = {26, 59, 103};
# 	int cutCost3 = 1, price3 = 10;
# 	int[] nums3 = {30, 59, 110};
# 	System.out.println(maxProfit(nums1, cutCost1, price1));
# 	System.out.println(maxProfit(nums2, cutCost2, price2));
# 	System.out.println(maxProfit(nums3, cutCost3, price3));
# }

# private static int maxProfit(int[] nums, int cutCost, int price) {
# 	int maxLength = 0;
# 	for(int n : nums)
# 		maxLength = Math.max(n, maxLength);
# 	return helper(nums, cutCost, price, 0, maxLength, new HashMap<>());
# }


# private static int helper(int[] nums, int cutCost, int price, int l, int r, Map<String, Integer> memo) {
# 	int res = 0;
# 	if(l >= r)
# 		return res;
# 	if(memo.containsKey(l + "_" + r))
# 		return memo.get(l + "_" + r);
# 	int rangeL = l, rangeR = r;
# 	while(l < r) {
# 		int m1 = l + (r - l)/2;
# 		int m2 = m1 + 1;
# 		if(getCost(nums, cutCost, price, m1) > getCost(nums, cutCost, price, m2))
# 			r = m1;
# 		else
# 			l = m2;
# 	}
# 	int resR = helper(nums, cutCost, price, l+1, rangeR, memo);
# 	int resL = helper(nums, cutCost, price, rangeL, l-1, memo);
# 	res = Math.max(getCost(nums, cutCost, price, l), Math.max(res, Math.max(resL, resR)));
# 	memo.put(rangeL+"_"+rangeR, res);
# 	return res;
# }

# static int getCost(int[] nums, int cutCost, int price, int length) {
# 	int res = 0;
# 	int cost = 0;
# 	if(length == 0) {
# 		return Integer.MIN_VALUE;
# 	}
# 	for(int i=0;i<nums.length;i++) {
# 		int numOfCuts = nums[i]/length;
# 		res += numOfCuts*length*price;
# 		cost += (numOfCuts-1) * cutCost + (nums[i]%length != 0 ? 1 : 0) * cutCost;
# 	}
# 	res -= cost;
# 	return res;
# }