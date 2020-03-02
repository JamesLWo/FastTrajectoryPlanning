def heappush(heap, item):
    heap.append(item)
    size = len(heap) - 1
    siftdown(heap, 0, size)

def heappop(heap):
    last = heap.pop()
    if heap:
        retval = heap[0]
        heap[0] = last
        siftup(heap, 0)
        return retval
    return last
 
def siftdown(heap, start, index):
    insert = heap[index]
    while index > start:
        parentpos = get_parent(index)
        parent = heap[parentpos]
        if insert < parent:
            heap[index] = parent
            index = parentpos
            continue
        break
    heap[index] = insert

def siftup(heap, index):
    end = len(heap)
    start = index
    insert = heap[index]
    child = get_child(index)
    while child < end:
        right = child + 1
        if right < end and not heap[child] < heap[right]:
            child = right
        heap[index] = heap[child]
        index = child
        child = get_child(index)
    heap[index] = insert
    siftdown(heap, start, index)

def get_child(index):
    return 2*index + 1

def get_parent(index):
    return (index - 1) >> 1

''' 
python heapq library implementation courtesy of cpython library
customized and removed functions for own heap class for purpose of fast trajectory replanning
'''
