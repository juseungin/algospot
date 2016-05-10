#include <stdio.h>
#include <stdlib.h>

typedef struct node {
  int val;
  struct node * next;
} node_t;

void print_list(node_t * head) {
  node_t * current = head;

  while (current != NULL) {
    printf("%d\n", current->val);
    current = current->next;
  }
}

int pop(node_t ** head) {
  int retval = -1;
  node_t * next_node = NULL;

  if (*head == NULL) {
    return -1;
  }

  next_node = (*head)->next;
  retval = (*head)->val;
  free(*head);
  *head = next_node;

  return retval;
}

void push(node_t * head, int data) {
  node_t* new_node = malloc(sizeof(node_t));
  new_node->val = data;
  new_node->next = NULL;

  if (head == NULL){
    head = new_node;
    return;
  }
  node_t* tail = head;
  while( tail->next != NULL)
    tail = tail->next;
  tail->next = new_node;
}

int remove_by_value(node_t ** head, int val) {
  /* TODO: fill in your code here */
  node_t * current = * head;
  node_t * prev = NULL;

  while( current != NULL){
    if (current->val == val){
      if(prev != NULL){
        prev->next = current->next;
        free(current);
      }else{
        free(*head);
        *head = current->next;
      }
    }
    else
      prev = current;
      current = current->next;
  }
  return 0;
}

int main() {

  node_t * test_list = malloc(sizeof(node_t));
  //test_list->val = 1;
  push(test_list, 1);
  test_list->next = malloc(sizeof(node_t));
  test_list->next->val = 2;
  test_list->next->next = malloc(sizeof(node_t));
  test_list->next->next->val = 3;
  test_list->next->next->next = malloc(sizeof(node_t));
  test_list->next->next->next->val = 4;
  test_list->next->next->next->next = NULL;

  remove_by_value(&test_list, 3);

  print_list(test_list);
}
