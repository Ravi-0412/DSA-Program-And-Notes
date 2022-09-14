//Ascending priority queue with smallest no as the highest priority(By inserting the elements simply and at the time of deletion delete the smallest one)
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
class PriorityQueue3
{
    private link front;
    public PriorityQueue3()
    {
        front=null;
    }
    public boolean isEmpty()
    {
        return(front==null);			
    }
         public void Enqueue(int d)       //InsertAtFirst
		{
			link newlink=new link(d);
			if(isEmpty())
			{
				front=newlink;
			}
			else
			{
			   newlink.next=front;
			   front=newlink;
			}
        }
        public void Dequeue()    //Deleting the smallest element first
        {   
            link smallest=front;
            link temp=front;
            link pre=null;
            if(isEmpty())
           {
              System.out.println("empty queue");
           }
           else
           {
              System.out.println("deleted element is:");
              while(temp!=null)
              {
                  if(temp.next!=null && temp.next.data<smallest.data)
                  {
                      smallest=temp.next;
                      pre=temp;      //pre will point to smaller one
                  }
                  temp=temp.next;
              }
              System.out.println(smallest.data);
              if(smallest!=front)
              {
                  pre.next=smallest.next;
              }
              else
              {
                  front=front.next;
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
     public static void main(String args[]) throws IOException
    {
        link ob1=new link(50);
        PriorityQueue3 ob2=new PriorityQueue3();
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
    