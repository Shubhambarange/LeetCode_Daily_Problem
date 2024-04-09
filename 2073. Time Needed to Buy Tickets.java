2073. Time Needed to Buy Tickets

Example 1:

Input: tickets = [2,3,2], k = 2
Output: 6
Explanation: 
- In the first pass, everyone in the line buys a ticket and the line becomes [1, 2, 1].
- In the second pass, everyone in the line buys a ticket and the line becomes [0, 1, 0].
The person at position 2 has successfully bought 2 tickets and it took 3 + 3 = 6 seconds.

# Code
```
class Solution {
    public int timeRequiredToBuy(int[] tickets, int k) {
        int time = 0;
        for(int i = 0; i < tickets.length; i++){
            if(tickets[i] < tickets[k]){
                time += tickets[i];
            }
            else{
                time += tickets[k];
            }
            if(i>k && tickets[i] >= tickets[k]){
                time--;
            }

        }return time;
    }
}
```
