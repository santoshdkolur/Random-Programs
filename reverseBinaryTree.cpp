#include<iostream>
using namespace std;
struct Node{
	int data;
	struct Node *left;
	struct Node *right;
	struct Node *prev;
};
int a[100],count=0;
struct Node *root=NULL;
void insert(int data)
{
	struct Node *temp=(struct Node *)malloc(sizeof(struct Node));
	temp->data=data;
	temp->left=NULL;
	temp->right=NULL;
	if(root==NULL)
		root=temp;
	else
	{
		struct Node *p,*q;
		p=root;
		while(p!=NULL)
		{
			q=p;
			if(data<p->data)
				p=p->left;
			else if(data>p->data)
				p=p->right;
		}
		if(data<q->data)
			q->left=temp;
		else
			q->right=temp;
	}
}
void inorder(struct Node *p)
{
	if(p==NULL)
		return;
	else
	{
		inorder(p->left);
		cout<<p->data<<" ";
		a[count]=p->data;                            // The inorder values are stored in the array
		count++;
		inorder(p->right);
	}
}
void reverse(struct Node *p)
{
	if(p==NULL)
		return;
	else
	{
		
		struct Node *z=p->left;
		p->left=p->right;
		p->right=z;
		reverse(p->right);
		reverse(p->left);
	}
}
void display(struct Node *r, int l)    //The binary tree is displayed horizontally
{
	int i;
	if(r==NULL)
		return ;

	display(r->right,l+1);             //l is used to keep count of the spaces
	for(i=0;i<l;++i)
		printf("   ");
	printf("%d \n\n",r->data);
	display(r->left,l+1);

}
int main()
{
	int n=0;
	cout<<"Enter the data to be stored in the tree, enter -1 to stop."<<endl;
	while(n!=-1)
	{
		cin>>n;
		if(n>=0)
			insert(n);

	}
	cout<<"The values in the tree are: ";
	inorder(root); 
	cout<<endl;
	display(root,0);                           
	reverse(root);
	cout<<endl<<"The reversed values are: ";
	inorder(root);
	cout<<endl;
	display(root,0);
	cout<<endl;

}
