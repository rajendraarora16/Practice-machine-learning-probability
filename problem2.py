'''

Bayes' rules, Coditional probabilit, Chain rule
-----------------------------------------------

Conditional probability
=======================


If X and Y are two events then the conditional probability of X wiith respect to Y is denoted by P(X|Y).

The conditional probability in terms of statements will be treated as:
"The probability of event X given that Y has already occurred.


What if X and Y are independent events?
The occurence of event X is not dependent on event Y, i.e
Therefore, P(X|Y) = P(X)

What if X and Y are mutually exclusive?
As X and Y are disjoint events. The probability that X will occur when Y has already occured is 0.
Therefore, P(X|Y) = 0


Product rule:
it states that:
        #P(X intersection Y) = P (X | Y) * P(Y)
        #P(Y intersection X) = P (Y | X) * P(X)

_________________________________________________________________________________________________________________________


**Challenge**


Bob has an important meeting tomorrow and he has to reach office on time in morning. His general mode of transport is by car
and on a regular day (No car trouble) the probability that he will reach on time is P^ot. The prbability that he might have car trobule is P^ct. 
If the car runs into trouble he will have to take a train and only 2 trains are available out of N trains to get office on time.

What are the chances that he will reach office on time tomorrow?


If no car trouble: (1 - P^ct) * P^ot
If car trouble: P^ot * (2/N)


**Solution**

Let X: He reaches on time
Let Y: Car works

P(X|Y) = P^ot
P(Y) = P^ct

P(X) =  P(X intersection Y) +  P(X intersection Y') 

Where Y' is transport of train

P(X) = P(X|Y) * P(Y) + P(X|Y) * P(Y')
     = P^ot * (1-P^ct) + P^ct * 2/N

'''

def problem():
    Pct = input()
    Pot = input()
    N = input()

    P = (Pot*(1 - Pct)) + (Pct * 2/N)
    
    print("%.6f" % P)

if __name__ == "__main__":
    problem()    


