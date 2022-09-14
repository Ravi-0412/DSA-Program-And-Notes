/*  Name :Ravi Raushan
    class:CS-B(3rd sem)
    Roll:72
    program:priority queue with priority of each element given
*/
import java.util.Scanner;
import java.io.*;
import java.io.IOException;
class link
{
    int data;
    int priority;
    link next;
    public link(int d,int p)
    {
        data=d;
        priority=p;
        next=null;
    }
}
class PriorityQueue1
{
    link front;
    public PriorityQueue1()
    {
        front=null;
    }
    public boolean isEmpty()
    {
        return(front==null);			
    }
    public void Enqueue(int d,int p)
    {   
        link current=front;
        link newlink=new link(d,p);
        if(isEmpty())
        {
            front=newlink;
        }
        else if(p<front.priority)
        {
            newlink.next=front;
            front=newlink;
        }
         else
         {
            while(current.next!=null && p>current.next.priority)
            {
                current=current.next;
            }
            if(current.next==null)
            {
              current.next=newlink;
            }
            else
            {
                newlink.next=current.next;
                current.next=newlink;
            }
         }
    }
               public void Display()
		      {   
		    	  link current=front;
		    	  if(isEmpty())
		    	 {
		    		System.out.println("empty linklist pls insert the elements");
		    	 }
                  else
                {
                     System.out.println("elements are:");
                   do
                  {
                     System.out.println(current.data);
                     current=current.next;
                  } while(current!=null);
                }
              }
              public void Dequeue()
              {
                link temp=front;
                if(isEmpty())
                {
                    System.out.println("empty queue");
                }               
                else
                {  System.out.println("deleted element is:");
                   if(temp!=null)
                  {
                    System.out.println(temp.data);
                     front=front.next;
                     temp=front;
                  }
                } 
              }
    public static void main(String args[]) throws IOException
    {
        link ob1=new link(50,10);
        PriorityQueue1 ob2=new PriorityQueue1();
        Scanner sc=new Scanner(System.in);
        System.out.println("1.Insert 2.Delete 3.Display the elements 4.exit");
        int opt;
        do
        {
            System.out.println("enter the choice");
            opt=sc.nextInt();
            switch(opt)
            {
                case 1:System.out.println("enter the elements to insert");
                       int k=sc.nextInt();
                       System.out.println("enter the priority of elements");
                       int p=sc.nextInt();
                       ob2.Enqueue(k,p);
                          break;
                case 2:ob2.Dequeue();
                       break;
                case 3:ob2.Display();
                        break;
                default:System.out.println("invalid choice");	
            }
        }while(opt!=4);
    }
}
/* output:
1.Insert 2.Delete 3.Display the elements 4.exit
enter the choice
1
enter the elements to insert
10
enter the priority of elements
10
enter the choice
1
enter the elements to insert
0
enter the priority of elements
0
enter the choice
1
enter the elements to insert
4
enter the priority of elements
4
enter the choice
1
enter the elements to insert
2
enter the priority of elements
2
enter the choice
3
elements are:
0
2
4
10
enter the choice
2
deleted element is:
0
enter the choice
2
deleted element is:
2
enter the choice
2
deleted element is:
4
enter the choice
2
deleted element is:
10
enter the choice
2
empty queue
enter the choice
*/
