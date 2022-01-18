#import loop3.algo as algo_parallel
import loop3.algo_correct_pipes as algo_parallel
# import loop3.algo_queues as algo_parallel

def algo(i):
    return algo_parallel.main(i)

print(algo(10))
