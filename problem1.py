'''
**Challenge**

Mike wants to go fishing this weekend to nearby lake. His neighbour Alice (is the one Mike was hoping to ask out since long time) is also planing to go to the same spot for fishing this weekend. The probability that it will rain this weekend is p1. There are two possible ways to reach the fishing spot (bus or train). The probability that Mike will take the bus is p^mb and that Alice will take the bus is p^ab. Travel plans of both are independent of each other and rain.
What is the probability P^rs that Mike and Alice meet each other only (should not meet in bus or train) in a romantic setup (on a lake in rain)?

Input constraints:
0 < p1 < 1
0 < P^ab < 1
0 < P^mb < 1


**Solution**


Mike and Alice are going for fishing.

Probility of the rain of this weekend is ------> P1


Mike -----probability to take bus------------> P^mb
Alice ----probability to take bus------------> P^ab


Probability P^rs  -----------------> Lake (Rain spot)

Probability of Alice and Mike that they will meet in lake spot in raining day.


||============================================================||
|| probability = p1 * (p^ab * (1 - p^mb) + p^mb * (1 - p^ab)) ||
||============================================================||

Let's understand with example:
Probability of Mike will take bus: 0.2
Probability of Alice will take bus: 0.2
Probabilty of Raining this weekend: 0.5

So, input will be in the format as:

0.5 * ( ( 0.2 * 0.8 ) + (0.2 * 0.8) )
           ^     ^        ^     ^
           |     |        |     |
          P^ab  P^mt     P^mb  P^at

Where P^mt will be the probability of mike will take train.
and P^at will be the probability of Alice will take train.


First line: P^mb
Second line: P^ab
Third line: P1

Output format: P^rs rounded up to six decimal digits.

'''

def problem():
    Pmb = input()
    Pab = input()
    p1 = input()

    Prs = (p1 * ( Pab * (1 - Pmb) + Pmb * (1 - Pab)))
    print "%.6f" % Prs
    
if __name__ == "__main__":
    problem()    











