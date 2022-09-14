//Ascending priority Queue i.e lowest element will be of highest priority(inserted first)
import java.util.Scanner;
import java.io.*;
import java.io.IOException;
class PriorityQueue1
{
    int max,a[];
    int front,rear;
    public PriorityQueue1(int s)
    {
       max=s;
       a=new int[max];
       front=rear=-1;
    }
    public void Enqueue()
    {
        Scanner sc=new Scanner(System.in);
        if(rear==max-1)
        {
            System.out.println("queue is already full");
        }
        else if(front==-1)
        {
           rear=front=0;
           System.out.println("enter the element to insert");
           int data=sc.nextInt();
           a[rear]=data;
        }
        else
        {   
            System.out.println("enter the element to insert");
            int data=sc.nextInt();
            int i;
            for(i=rear;i>=front && a[i]>data;i--)
            {
                a[i+1]=a[i];
            }
            a[i+1]=data;
            rear++;
        }
    }
    public void Dequeue()
    {   
        if(front==-1)
        {
            System.out.println("queue empty");
        }
        int x=a[front];
        if(front==rear)//contains only one element
        {
            System.out.println("deleted element is:" +x);
            front=-1;
            rear=-1;
        }
        else
           {
             System.out.println("deleted element is:" +x);
             front=(front+1)%max;//increase the front by one      
           }
    }
    public void Display()
    {
        if(front==-1)
        {
            System.out.println("Queue is Empty");
        }
        else
        {   
            System.out.println("Elements present in the queue is:");
            for(int i=front;i<=rear;i++)
            {
                System.out.println(a[i]);
            }
        }
    }
    public static void main(String args[]) throws IOException
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the no of elements to enter");
        int s=sc.nextInt();
        PriorityQueue1 ob=new PriorityQueue1(s);
        System.out.println("1.Insert 2.Delete 3.Display 4.exit");
		int opt;
        do
        {
            System.out.println("enter the choice");
            opt=sc.nextInt();
            switch(opt)
            {
                case 1:ob.Enqueue();
                       break;          
                case 2:ob.Dequeue();
                       break;
                case 3:ob.Display();
                     break;
            }
        }while(opt!=4);
    }
}
