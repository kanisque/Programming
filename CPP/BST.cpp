#include<bits/stdc++.h>
#define pb push_back
using namespace std;

struct Node {
int data;
struct Node * next;
};

Node * insertNode(Node * head,int data)
{
    Node * temp = head;
    if(head==NULL)
    {
        head = new Node();
        head->data=data;
        head->next=NULL;
        return head;
    }
    while(head->next)
        head=head->next;
    Node * n = new Node();
    n->data=data;
    n->next=NULL;
    head->next=n;
    return temp;
}

Node * reverseList(Node * head)
{
    Node * temp=NULL, * nextNode = NULL;
    while(head)
    {
        nextNode=head->next;
        head->next=temp;
        temp=head;
        head=nextNode;
    }
    return temp;
}

void printList(Node * head)
{
    while(head)
    {
        cout<<head->data<<" ";
        head=head->next;
    }
    cout<<endl;
}

int main(){

    Node * head=NULL;
    head=insertNode(head,10);
    head=insertNode(head,100);
    head=insertNode(head,1000);
    head=insertNode(head,20);
    head=insertNode(head,200);
    head=insertNode(head,2000);
    head=insertNode(head,30);
    head=insertNode(head,300);
    //head=insertNode(head,3000);
    printList(head);

    head=reverseList(head);
    printList(head);

    return 0;
}
