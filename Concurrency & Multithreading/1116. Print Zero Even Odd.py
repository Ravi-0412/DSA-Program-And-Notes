# Logic: 
"""
Goal: Print 0 1 0 2 0 3 ... using 3 threads (zero, even, odd).

Semaphores control thread execution order.

🔹 How It Works
sem_zero starts at 1 → lets zero() run first.

zero() prints 0, then:

If odd → releases sem_odd

If even → releases sem_even

odd() / even() print the number, then release sem_zero to allow the next 0.
"""

# 🔹 Python Semaphore
"""
acquire() → waits if count is 0
release() → adds permit, unblocks waiting threads
"""


from threading import Semaphore, Thread

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.sem_zero = Semaphore(1)
        self.sem_even = Semaphore(0)
        self.sem_odd = Semaphore(0)

    def zero(self, printNumber):
        for i in range(1, self.n + 1):
            self.sem_zero.acquire()
            printNumber(0)
            if i % 2 == 0:
                self.sem_even.release()
            else:
                self.sem_odd.release()

    def even(self, printNumber):
        for i in range(2, self.n + 1, 2):
            self.sem_even.acquire()
            printNumber(i)
            self.sem_zero.release()

    def odd(self, printNumber):
        for i in range(1, self.n + 1, 2):
            self.sem_odd.acquire()
            printNumber(i)
            self.sem_zero.release()


# java

# About 'semaphore' class in java
"""
What is a Semaphore?

A semaphore is a synchronization primitive that can be used to control access to a common resource in concurrent programming. 
It maintains a set of permits, which threads can acquire and release.

    Permits: The number of permits indicates the number of threads that can access the resource simultaneously.
    Acquire: Decreases the number of available permits. If no permits are available, the thread is blocked until a permit is released.
    Release: Increases the number of available permits, potentially unblocking a waiting thread.

Java Semaphore Class

In Java, semaphores are provided by the java.util.concurrent.Semaphore class.
Constructor

    Semaphore(int permits): Creates a semaphore with the given number of permits and non-fair access policy.
    Semaphore(int permits, boolean fair): Creates a semaphore with the given number of permits and the specified fairness policy. 
    Fairness means granting permits in the order in which they were requested.

Key Methods

    acquire(): Acquires a permit if one is available, blocking the thread until a permit is available.
    release(): Releases a permit, returning it to the semaphore.
    tryAcquire(): Acquires a permit if one is available and returns true, otherwise returns false.
"""


"""
import java.util.concurrent.Semaphore;
import java.util.function.IntConsumer;

class ZeroEvenOdd {
    private int n;
    private Semaphore zero, even, odd;

    public ZeroEvenOdd(int n) {
        this.n = n;
        // Initialize semaphores
        this.zero = new Semaphore(1); // Start with 1 to allow zero to be printed first, passing > 0 to allow zero thread to run first
        this.even = new Semaphore(0); // Start with 0 to block even printing initially
        this.odd = new Semaphore(0);  // Start with 0 to block odd printing initially
    }

    // This method will be called by the thread responsible for printing zero
    public void zero(IntConsumer printNumber) throws InterruptedException {
        for (int i = 1; i <= n; i++) {
            zero.acquire(); // Wait until it's this thread's turn to print
            printNumber.accept(0); // Print zero
            if (i % 2 == 0) {
                even.release(); // If the number is even, signal the even thread
            } else {
                odd.release(); // If the number is odd, signal the odd thread
            }
        }
    }

    // This method will be called by the thread responsible for printing even numbers
    public void even(IntConsumer printNumber) throws InterruptedException {
        for (int i = 2; i <= n; i += 2) {
            even.acquire(); // Wait until it's this thread's turn to print
            printNumber.accept(i); // Print the even number
            zero.release(); // Signal the zero thread to continue
        }
    }

    // This method will be called by the thread responsible for printing odd numbers
    public void odd(IntConsumer printNumber) throws InterruptedException {
        for (int i = 1; i <= n; i += 2) {
            odd.acquire(); // Wait until it's this thread's turn to print
            printNumber.accept(i); // Print the odd number
            zero.release(); // Signal the zero thread to continue
        }
    }
}

"""




#C++ Code
# About 'semaphore' class in C++
"""
What is a Semaphore?

A semaphore is a synchronization primitive that can be used to control access to a common resource in concurrent programming. 
It maintains a set of permits (represented by a counter), which threads can acquire and release.

    Permits: The counter value indicates the number of threads that can access the resource simultaneously.
    Acquire: Decreases the counter (wait operation). If the counter is zero, the thread is blocked until another thread releases.
    Release: Increases the counter (signal operation), potentially unblocking a waiting thread.

C++ Semaphore Support

In C++, semaphores are available through the POSIX semaphore API (on POSIX-compliant systems) using the <semaphore.h> header.

Initialization

    sem_t sem;
    sem_init(&sem, 0, permits); 
    // Initializes a semaphore with a given number of permits. 
    // The second parameter is 0 for thread-shared (within process).

Key Functions

    sem_wait(&sem): Acquires a permit if one is available, blocking the thread until a permit becomes available.
    sem_post(&sem): Releases a permit, incrementing the counter and potentially unblocking a waiting thread.
    sem_trywait(&sem): Attempts to acquire a permit without blocking. Returns 0 on success, or -1 if no permits are available.

Destruction

    sem_destroy(&sem): Destroys the semaphore and releases associated resources.
"""


"""
#include <iostream>
#include <functional>
#include <mutex>
#include <condition_variable>
#include <thread>

class ZeroEvenOdd {
private:
    int n;
    int zeroCount = 1;  // acts like Semaphore(1)
    int evenCount = 0;  // acts like Semaphore(0)
    int oddCount = 0;   // acts like Semaphore(0)

    std::mutex mtx;
    std::condition_variable cv;

public:
    ZeroEvenOdd(int n) {
        this->n = n;
    }

    void zero(std::function<void(int)> printNumber) {
        for (int i = 1; i <= n; ++i) {
            std::unique_lock<std::mutex> lock(mtx);
            cv.wait(lock, [&]() { return zeroCount > 0; });
            zeroCount--;  // simulate acquire
            printNumber(0);
            if (i % 2 == 0) {
                evenCount++;  // simulate release
            } else {
                oddCount++;
            }
            cv.notify_all();
        }
    }

    void even(std::function<void(int)> printNumber) {
        for (int i = 2; i <= n; i += 2) {
            std::unique_lock<std::mutex> lock(mtx);
            cv.wait(lock, [&]() { return evenCount > 0; });
            evenCount--;
            printNumber(i);
            zeroCount++;
            cv.notify_all();
        }
    }

    void odd(std::function<void(int)> printNumber) {
        for (int i = 1; i <= n; i += 2) {
            std::unique_lock<std::mutex> lock(mtx);
            cv.wait(lock, [&]() { return oddCount > 0; });
            oddCount--;
            printNumber(i);
            zeroCount++;
            cv.notify_all();
        }
    }
};

"""
