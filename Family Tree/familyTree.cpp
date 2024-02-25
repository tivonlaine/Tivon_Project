/*
Name: Tivon Laine, 2002167255, 1004 & 1006, Assignment 3
Description: Traversing binary trees to do arithmetics
Input: Text file
Output: Updated Tree
*/ 
#include "familyTree.h"
#include <vector>
#include <cstdlib>
#include <iostream>
using namespace std;

familyTree::familyTree(const std::vector<int>& familyMembers)
{
root=buildTree(familyMembers, 0);    //creating the root and making it the start of a tree
}

familyTree::binTreeNode* familyTree::buildTree(const vector<int>& familyMembers, 
size_t index)
{

if(familyMembers.size()<=index){    //if index is out of bounds
    return nullptr;
}

if (familyMembers[index]==-1){      //if there is no node
    return nullptr;
}
binTreeNode* node= new binTreeNode(familyMembers[index]);       //creating a root node
node->left=buildTree(familyMembers, index*2+1);         //going to the left
node->right=buildTree(familyMembers,(index+1)*2);       //going to the right
return node;

}

familyTree::~familyTree()
{
deallocateTree(root);
}

void familyTree::deallocateTree(binTreeNode * r)
{
if(r==nullptr){     //if there is no node
    return;
}
deallocateTree(r->left);
deallocateTree(r->right);
delete(r);                  //deletes node
}

void familyTree::updateInheritance()
{
updateInheritance(root);
;
}

void familyTree::updateInheritance(binTreeNode * grandParent)
{
if (grandParent==nullptr){  //if no root
    return;
}

updateInheritance(grandParent->left);       //postorder
updateInheritance(grandParent->right);

int left=0;
int right=0;

if(grandParent->right==nullptr||grandParent->left==nullptr){        //if any children is null
    return;
}

if(grandParent->left->left!=nullptr){       //checking left left child
    if(grandParent->left->right!=nullptr){      //checking left right child
        left+=grandParent->left->right->wealth;
        left+=grandParent->left->left->wealth;
    }
    else{
        left+=grandParent->left->left->wealth;
    }
}else if(grandParent->left->right!=nullptr){    //checking left right child if no left left child
    left+=grandParent->left->right->wealth;
}

if(grandParent->right->left!=nullptr){
    if(grandParent->right->right!=nullptr){
        right+=grandParent->right->left->wealth;
        right+=grandParent->right->right->wealth;
    }else{
        right+=grandParent->right->left->wealth;
    }
}else if(grandParent->right->right!=nullptr){
    right+=grandParent->right->right->wealth;
}

if((grandParent->left->left!=nullptr||grandParent->left->right!=nullptr)&&(grandParent->right->left!=nullptr
||grandParent->right->right!=nullptr)){//checking if at least one grandchild on left and right side

if(grandParent->left->left!=nullptr){
    grandParent->left->left->wealth=right;                      
}
if(grandParent->left->right!=nullptr){
    grandParent->left->right->wealth=right;
}                                                                   //assigning corresponding values
if(grandParent->right->right!=nullptr){
    grandParent->right->right->wealth=left;
}
if(grandParent->right->left!=nullptr){
    grandParent->right->left->wealth=left;
}
}
}

void familyTree::outputTree()
{
outputTree(root);
}

void familyTree::outputTree(binTreeNode * r)
{
    if(r==nullptr){
        return;
    }
    cout<<r->wealth<<endl;          //preorder
    outputTree(r->left);
    outputTree(r->right);

}
