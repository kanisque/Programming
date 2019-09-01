#include<iostream>
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

Node * deleteNode(Node * head, int num)
{
    Node * backup=head;
    Node * temp;
    if(head->data==num)
    {
        temp=head->next;
        free(head);
        return(temp);
    }
    while(!(head->next->data==num))
        head=head->next;
    temp=head->next->next;
    free(head->next);
    head->next=temp;
    return backup;
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
    head=insertNode(head,1);
    head=insertNode(head,2);
    head=insertNode(head,3);
    head=insertNode(head,4);
    head=insertNode(head,5);
    head=insertNode(head,6);
    head=insertNode(head,7);
    head=insertNode(head,8);
    head=insertNode(head,9);

    printList(head);

    head=deleteNode(head,3);
    printList(head);

    head=deleteNode(head,1);
    printList(head);

    head=reverseList(head);
    printList(head);

    return 0;
}
