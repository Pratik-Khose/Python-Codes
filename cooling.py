import multiprocessing
import time

def cpu_stress_test():
    start_time = time.time()
    # Perform a large number of calculations
    for i in range(10**8):
        x = i ** 2
    end_time = time.time()
    print(f"Process finished in {end_time - start_time:.2f} seconds")

def run_stress_test():
    # Get the number of available CPU cores
    num_cores = multiprocessing.cpu_count()

    # Create a process for each core
    processes = []
    for _ in range(num_cores):
        p = multiprocessing.Process(target=cpu_stress_test)
        processes.append(p)
        p.start()

    # Wait for all processes to complete
    for p in processes:
        p.join()

if __name__ == "__main__":
    for _ in range(20):  # Run the stress test 20 times
        print(f"Running stress test iteration {_+1}...")
        run_stress_test()
        print(f"Iteration {_+1} completed.\n")
