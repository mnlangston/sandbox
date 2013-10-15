#include <stack>
#include <stdio.h>
#include "tree.h"

bool compactTree::findSum(int s){
    std::stack<int> stk;
    if(tree[0] == s) return true;
    stk.push(0);
    while(!stk.empty()){
        int curIndex = stk.top(); stk.pop();
        tree[getLeftOf(curIndex)] += tree[curIndex];
        //is left a leaf node?
        bool isLeftLeaf = (getLeftOf(getLeftOf(curIndex)) == -1) && (getRightOf(getLeftOf(curIndex)) == -1);
        if((tree[getLeftOf(curIndex)] == s) && isLeftLeaf)
            return true;
        tree[getRightOf(curIndex)] += tree[curIndex];
        //is right a leaf node?
        bool isRightLeaf = (getLeftOf(getRightOf(curIndex)) == -1) && (getRightOf(getRightOf(curIndex)) == -1);
        if((tree[getRightOf(curIndex)] == s) && isRightLeaf)
            return true;
        
        if((tree[getLeftOf(curIndex)] != -1) && tree[getLeftOf(curIndex)] < s){
            stk.push(getLeftOf(curIndex));
        }
        if((tree[getRightOf(curIndex)] != -1) && tree[getRightOf(curIndex)] < s){
            stk.push(getRightOf(curIndex));
        }
    }
    return false;
}

int main(){
    compactTree t(15);
    printf("Find what sum: ");
    int s;
    scanf("%d",&s);
    if(t.findSum(s)){
        printf("Found sum=%d!\n",s);
    }
    else
        printf("Could not find sum=%d\n",s);
}
