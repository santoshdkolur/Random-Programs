/*
Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit. 
The digits are stored in reverse order, such that the least significant digit is at the head of the list. 
Write a function that adds the two numbers and returns the sum as a linked list. 
Example
Input: (7-> 1-> 6) + (5-> 9-> 2).That is, 617 + 295. 
Output: 2 1 9. That is, 912. 



Answer:
The output here is formatted to display 912 using recursive function. 
If the actual sum is required, you can just print the list linked to ptr normally without using the recursive 
function at the end of the program.

The below program is also modified to take variable lenghts of the numbers. 
For example: First number can have 2 digits
and the second can have 3 digits.



*/
#include<iostream>
using namespace std;
struct Node{
    int data;
    struct Node* next;
};
struct Node *head1=NULL;
struct Node *head2=NULL;
void display(struct Node* ptr)
{
    if(ptr->next!=NULL)
        display(ptr->next);
    cout<<ptr->data<<" ";
}
int main()
{
    int n1,n2,n,n_1,n_2;
    cout<<"Enter the degrees of the numbers"<<endl;
    cin>>n1>>n2;
    n_1=n1;
    n_2=n2;
    cout<<"Enter the digits of the first number"<<endl;
    while(n1--!=0)
    {
        struct Node *temp=(struct Node *)malloc(sizeof(struct Node));
        cin>>n;
        temp->data=n;
        temp->next=NULL;
        if(head1==NULL)
            head1=temp;
        else{
            struct Node *ptr;
            ptr=head1;
            while(ptr->next!=NULL)
            {
                ptr=ptr->next;
            }
            ptr->next=temp;
        }
    }
    cout<<"Enter the digits of the secind number"<<endl;
    while(n2--!=0)
    {
        struct Node *temp=(struct Node *)malloc(sizeof(struct Node));
        cin>>n;
        temp->data=n;
        temp->next=NULL;
        if(head2==NULL)
            head2=temp;
        else{
            struct Node *ptr;
            ptr=head2;
            while(ptr->next!=NULL)
            {
                ptr=ptr->next;
            }
            ptr->next=temp;
        }
    }
    cout<<"Input Finished"<<endl;
    int min;
    struct Node *ptr,*ptr2;
    if(n_1<=n_2)
    {
        min=n_1;
        ptr=head2;
        ptr2=head1;
    }
    else
    {
        min=n_2;
        ptr=head1;
        ptr2=head2;
    }
    
    while(min--!=0)
    {
        int s=ptr->data+ptr2->data;
        cout<<"S="<<s<<endl;
        if(s>=10){
            if(ptr->next==NULL)
            {
                struct Node *temp=(struct Node*)malloc(sizeof(Node));
                temp->next=NULL;
                temp->data=0;
                ptr->next=temp;
            }
            ptr->next->data=ptr->next->data+1;
            ptr->data=s-10;
        }
        else
        {
            ptr->data=s;
        }
        ptr=ptr->next;
        ptr2=ptr2->next;
    }
    cout<<"Displaying the result:"<<endl;
    if(n_1<=n_2)
    {
        min=n_1;
        ptr=head2;
    }
    else
    {
        min=n_2;
        ptr=head1;
    }
    display(ptr);
}
