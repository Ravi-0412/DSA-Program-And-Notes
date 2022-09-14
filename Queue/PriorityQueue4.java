//Ascending priority queue(By inserting the elements as usual and while deleting delete the smallest one)
import java.util.Scanner;
import java.io.*;
import java.io.IOException;
class PriorityQueue4
{
    int max,a[];
    int front,rear;
    public PriorityQueue4(int s)
    {
       max=s;
       a=new int[max];
       front=rear=-1;
    }
    