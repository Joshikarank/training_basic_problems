
from memory_profiler import profile

@profile
def my_function():
    for i in range(100000):
        yield i
    

if __name__ == '__main__':
    # Use the memory_profiler to check memory usage before and after the function
    from memory_profiler import memory_usage
    
    # Before function call
    memory_before = memory_usage()[0]
    print(f"Memory before function call: {memory_before} MB")

    # Call the function
    my_function()

    # After function call
    memory_after = memory_usage()[0]
    print(f"Memory after function call: {memory_after} MB")

    # Calculate memory usage during the function call
    memory_used = memory_after - memory_before
    print(f"Memory used during function call: {memory_used} MB")
