# Two sum problem & Median Maintenance


from time import time
import sys, threading, bisect, heapq


class part_a():

    @classmethod
    def count_t(cls, data):
        interval = 10000
        count = set()

        for i in data:
            bound_1 = (i - interval) * -1
            bound_2 = (i + interval) * -1
            if bound_1 < bound_2:
                left = bisect.bisect_left(data, bound_1)
                right = bisect.bisect_right(data, bound_2)
            else:
                left = bisect.bisect_left(data, bound_2)
                right = bisect.bisect_right(data, bound_1)
            count |= set([i + j for j in data[left:right]])
        return len(count)

    @classmethod
    def read_data(cls):
        data = []

        with open('TwoSum.txt') as f:
            for line in f:
                data.append(int(line))
        data.sort()
        return data

    @classmethod
    def start(cls):
        start = time()
        print 'Start A'
        data = cls.read_data()
        print cls.count_t(data)
        print 'End A: ', time() - start


class part_b():

    @classmethod
    def compute(cls):
        heap_high = []
        heap_low = []
        sum = 0

        with open('Median.txt') as f:
            first_line = f.readline()
            heapq.heappush(heap_low, int(first_line) * -1)
            sum += int(first_line)

            second_line = f.readline()
            if heap_low[0] * -1 > int(second_line):
                heapq.heappush(heap_low, int(second_line) * -1)
                temp = heapq.heappop(heap_low)
                heapq.heappush(heap_high, temp * -1)
            else:
                heapq.heappush(heap_high, int(second_line))
            sum += heap_low[0] * -1

            for line in f:
                new_num = int(line)
                if new_num < (heap_low[0] * -1):
                    heapq.heappush(heap_low, new_num * -1)
                else:
                    heapq.heappush(heap_high, new_num)

                if len(heap_low) - len(heap_high) > 1:
                    num = heapq.heappop(heap_low) * -1
                    heapq.heappush(heap_high, num)
                elif len(heap_high) - len(heap_low) > 1:
                    num = heapq.heappop(heap_high)
                    heapq.heappush(heap_low, num * -1)
                if len(heap_low) >= len(heap_high):
                    sum += (heap_low[0] * -1)
                else:
                    sum += heap_high[0]
        return sum

    @classmethod
    def start(cls):
        start = time()
        print 'Start B'
        summed = cls.compute()
        print summed
        print 'End B: ', time() - start


def main():
    part_a.start()
    part_b.start()
    return


if __name__=="__main__":
    threading.stack_size(67108864)
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target = main)
    thread.start()

