#include <stdio.h>
#include <stdlib.h>

struct node{
	struct node* next;
	struct node* arbit;
	int val;
};

typedef struct node node;

void buildLL(int *vals,int *avals,node **list,size_t size){
	int i;
	node *cur,*head;
	head = NULL;
	for(i=size-1; i >= 0; i--){
		cur = (node*)malloc(sizeof(node));
		cur->val = vals[i];	
		cur->next = head;
		head = cur;
	}
	cur = head;
	//set arbits
	for(i=0;i<size;i++){
		//get "from" node
		node *from=head,*to=head;
		int z=0,v=avals[i];
		while(z!=i){
			from = from->next;
			z++;
		}
		//get "to" node
		z = 0;
		while(z!=v){
			to = to->next;
			z++;
		}
		//set arbit
		from->arbit = to;
	}
	*list = head;
}

void reverse(node **list){
	node *cur = *list,*prev = NULL,*head = NULL;
	while(cur){
		node *tmp = cur->next;
		cur->next = prev;
		prev = cur;
		cur = tmp;
	}
	head = prev;
	*list = head;
}

void printLL(node *list){
	node *cur = list;
	while(cur){
		printf("%d : %d\n",cur->val,cur->arbit->val);
		cur = cur->next;
	}
	printf("\n");
}

int main(){
	node *head;
	int vals[5]={1,2,3,4,5};
	int arbits[5]={2,0,4,2,1};
	buildLL(vals,arbits,&head,sizeof(vals)/sizeof(vals[0]));
	printLL(head);
	reverse(&head);
	printLL(head);
}
