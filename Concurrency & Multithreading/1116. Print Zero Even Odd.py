# java
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