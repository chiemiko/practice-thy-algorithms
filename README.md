# practice-thy-algorithms
It's been a minute since I've gone over data structures and algorithms, so I'm implementing the ones I find interesting or could use a refresher for here.

I'm starting with Python and will then move to Javascript.


# NOTES
## max heap properties
definition of a priority queue     
        
A binary tree that SATISFIES THE HEAP PROPERTY: 

- parent is larger than the child 

What are they used for? 

- finding the smallest or largest item in a dataset quickly... and that's it...
    - can help with sorting/searching/k largest item

RUNTIMES: 

insert: Olog(N)
pop: Olog(N)
peek: O(1)

BUILDING a heap / heapify: ONlog(N)
