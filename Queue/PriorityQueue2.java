//Ascending priority queue with smallest no as the highest priority(By inserting smallest at first position and simply delete from first)
import java.util.Scanner;
import java.io.*;
import java.io.IOException;
class link
{
	public int data;
	public link next;
	public link(int d)
	{
        data=d;
        next=null;
    }
}
class PriorityQueue2
{
    private link front;
    public PriorityQueue2()
    {
        front=null;
    }
    public boolean isEmpty()
    {
        return(front==null);			
    }
    public void Enqueue(int d)
    {
        link current=front;
        link newlink=new link(d);
        if(isEmpty())
        {
            front=newlink;
        }
        else if(d<front.data)
        {
            newlink.next=front;
            front=newlink;
        }
         else
         {
            while(current.next!=null && d>current.next.data)
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
        link ob1=new link(50);
        PriorityQueue2 ob2=new PriorityQueue2();
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
                       ob2.Enqueue(k);
                          break;
                case 2:ob2.Dequeue();
                       break;
                case 3:ob2.Display();
                        break;
            }
        }while(opt!=4);
    }
}