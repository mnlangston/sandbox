#include <stdlib.h>
#include <stdio.h>

class compactTree{
private:
    int *tree;
    size_t sz;
    void buildTree(){
        tree = new int[sz];
        for(int i = 0; i < sz; i++){
            tree[i] = i;
        }
    }
public:
    compactTree(size_t size){
        sz = size;
        buildTree();
    }
    inline void reset(){
        buildTree();
    }
    inline int getLeftOf(int i){
        int ni = (2*i)+1;
        if(ni >= sz) return -1;
        return ni;
    }
    inline int getRightOf(int i){
        int ni = (2*i)+2;
        if(ni >= sz) return -1;
        return ni;
    }
    inline void printTree(){
        for(int i = 0; i < sz; i++){
            printf("%d\n",tree[i]);
        }
    }

    bool findSum(int s);

};
