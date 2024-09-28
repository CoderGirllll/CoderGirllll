#include <stdio.h>
#include <stdlib.h>
typedef struct node {
    int val;
    struct node *next;
}node;
int main(void){
    struct node *head = malloc(sizeof(node));
    struct node *node = head;
    int data;
    for (int i = 0; i < 5; i++){
        printf("Enter roll no. of student: ");
        scanf("%i", &data);
        node->val = data;
        if (i == 4){
            node->next = NULL;
        }
        else{
            node->next = malloc(sizeof(node));
            node = node->next;
        }
    }

    int roll;
    printf("Enter roll no after which to add: ");
    scanf("%d", &roll);
    
    node = head;

    for(int i=0; i < 5; i++) {
        if(node->val == roll) {
            struct node* new = malloc(sizeof(node));
            printf ("Enter roll no. of student: ");
            scanf ("%d",&data);
            new->next=node->next;
            node->next=new;
            new->val=data;
            break;
        }
        node = node->next;
    }

    node = head;
    while(node != NULL){
        printf("Roll no. of student is: %i\n", node->val);
        node = node->next;
    }
    return 0;
}
