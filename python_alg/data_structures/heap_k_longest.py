'''
Suppose you were asked to write a program which takes a sequence of strings presented in “streaming” fashion: 
you cannot back up to read an earlier value. Your program must compute the k longest
strings in the sequence. All that is required is the k longest strings—it is not required to order these
strings.
- Min-heap
'''
import heapq
def top_k(k, stream):
    # compare entries by length
    min_heap = [(len(s), s) for s in itertools.islice(stream, k)]
    heapq.heapify(min_heap)

    for next_string in stream:
        # push next_string and pop the shortest 
        # to avoid arbitrary look up and deletes )(Nlogk), which check if its even worth adding the string to the q
        if len(next_string) > heapq[0][0]:
            heapq.heappushpop(min_heap, (len(next_string), next_string))
    return [p[i] for p in heapq.nsmallest(k, min_heap)]