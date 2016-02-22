#include <stdio.h>
#define MAX_SIZE 15

struct TreeNode
{
	int data;
};

struct Tree
{
	int cur = 1;
	TreeNode Array[MAX_SIZE];
};

int compare_add(Tree *target_tree, int position)
{
	int temp;
	if(target_tree->Array[position].data < target_tree->Array[position/2].data || position ==1)
		return 0;
	if(target_tree->Array[position].data > target_tree->Array[position/2].data){
		temp = target_tree->Array[position].data;
		target_tree->Array[position].data = target_tree->Array[position/2].data;
		target_tree->Array[position/2].data = temp;
		return compare_add(target_tree, position/2);
	}
	return 0;
}

void add_tree(Tree *target_tree, int item)
{
	if(target_tree-> cur ==1){
		target_tree->Array[target_tree->cur].data = item;
		target_tree->cur +=1;
		return;
	}
	target_tree->Array[target_tree->cur].data = item;
	compare_add(target_tree, target_tree->cur);
	target_tree->cur +=1;
}

int compare_delete(Tree *target_tree, int position)
{
	if (position > target_tree->cur)
		return 0;
	int temp,next;
	if (target_tree->Array[position*2].data > target_tree->Array[position*2+1].data){
		next = 0;
	} else
		next = 1;
	temp = target_tree->Array[position*2 + next].data;
	target_tree->Array[position*2 + next].data = target_tree->Array[position].data;
	target_tree->Array[position].data = temp;
	return compare_delete(target_tree, position*2 + next);
}

int delete_tree(Tree *target_tree)
{
	if (target_tree->cur == 0)
		return -1;
	int temp;
	if (target_tree->cur != 1){
		temp =  target_tree->Array[1].data;
		target_tree->Array[1].data = target_tree->Array[target_tree->cur].data;
		target_tree->cur -= 1;
		compare_delete(target_tree, 1);
	}
	else{
		temp = target_tree->Array[1].data;
		target_tree->cur -= 1;
	}
	return temp;
}

int main(){
	Tree heap;
	add_tree(&heap, 10);
	add_tree(&heap, 20);
	add_tree(&heap, 30);
	add_tree(&heap, 60);
	add_tree(&heap, 40);
	delete_tree(&heap);
	for (int i=1; i < heap.cur ; i++)
		printf("heap= %d\n", heap.Array[i].data);
	return 0;
}
