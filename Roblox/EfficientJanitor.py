    # def numRescueBoats(self, people: List[int], limit: int) -> int:
    #     people.sort()
    #     beg, end, ans = 0, len(people) - 1, 0
    #     while beg <= end:
    #         if people[beg] + people[end] <= limit:
    #             beg += 1
    #         ans += 1
    #         end -= 1
                
    #     return ans




public static int findPossibleFreeSizesCount(int s0, int n, int k, int b, int m, int a) {
	// Step 1. Create list of wall length
	List<Integer> walllengthlist = new ArrayList<>();
	walllengthlist.add(s0);

	for (int i = 1; i < n; i++) {
		int next = (k * walllengthlist.get(i - 1) + b) % m + 1 + walllengthlist.get(i - 1);
		walllengthlist.add(next);
	}
	Collections.sort(walllengthlist);

	// Step 2. find out all possible free
	int result = 0;
	int left = 0, right = walllengthlist.size() - 1;

	while (left < right && right < walllengthlist.size()) {
		if (walllengthlist.get(left) * walllengthlist.get(right) > a) {
			right--;
		} else { // less or equal to a
					// (i, i), (i, j), (j, i), (i, j-1), (j-1, i) are all OK
			result += 1 + (right - left) * 2;
			left++;
		}
	}

	return result;
} 


public static int findPossibleFreeSizesCount(int s0, int n, int b, int k, int m, int a) {
	
	List<Integer> walls = new ArrayList<>();
	walls.add(s0);
    int pointer = 0, result = 0;
	for (int i = 1; i < n; i++) {
        // All new walls created will be longer than previous wall.
		int next = (b * walls.get(i - 1) + k) % m + 1 + walls.get(i - 1);
		walls.add(next);
        
        if (pointer == i - 2) pointer = i - 1;
        // If you can make an area with current wall and the wall at pointer,
        // You can make an area with all walls before the pointer.
        
        while (pointer >= 0 && walls.get(pointer) * next > a) pointer--;
        if (pointer < 0) return result;
        result += (pointer + 1) * 2;
	}
    return result;
}