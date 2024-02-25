#include "LL.h"
#include "LL.cpp"
#include <iostream>
#include <fstream>
using namespace std;

int main( int args, char * argv[])
{
  struct cardType{
    int face;
    char suit;
  };
  const int PILES=5;
  LL<cardType> piles[PILES];  //creating the pile of cards
  LL<cardType>::iterator topOfPile[PILES];  //creating iterator called topOfPile
  ifstream input;
  input.open(argv[1]);
  cardType card;    //creating a card
  for(int i=0;i<PILES;i++){ //iterating through array
    for(int j=0;j<=i;j++){   //iterating through nodes
      //cardType card;    //creating a card
      input>>card.face>>card.suit;  //getting face and suit of card
      piles[i].tailInsert(card);  //adding cards to end of pile // inserting tail node to end of linked list
    }
    topOfPile[i]=piles[i].end();    //keeping track of last card
  }

 
 LL<cardType>::iterator nul;
  for(int i=0;i<PILES;i++){      //iterating through array
  cout<<i+1<<". ";
    for(auto it = piles[i].begin();it!=nul;it++){ //iterating through nodes in linked lists
    if( it!=piles[i].end()){
        cout<<" __ ";

    }else{
        cout<<(*it).face<<(*it).suit<<" "<<endl;

    }


    }
  }
  
bool check=true;
int i;
int j;
while(cin>>i>>j){


cout<<"Make your move: ";
cout<<i<<" "<<j<<endl;
  i--;
  j--;
  
  if( i<0 || j<0 || i>=PILES || j>=PILES){  //bounds checking
    cout<<"Out of bounds"<<endl;
   for(int first=0;first<PILES;first++){      //iterating through array
     cout<<first+1<<". ";
    for(auto it = piles[first].begin();it!=piles[first].end();it++){ //iterating through nodes in linked lists
        cout<<" __ ";

    }
       for (auto it=topOfPile[first];it!=nullptr;it++){
        cout<<(*it).face<<(*it).suit<<" ";

       }cout<<endl;
    
   
  }     
    continue;
  }

  if (piles[i].isEmpty()){
    cout<<"Cannot move card from empty stack"<<endl;

  for(int first=0;first<PILES;first++){      //iterating through array
  cout<<first<<". ";
    for(auto it = piles[first].begin();it!=piles[first].end();it++){ //iterating through nodes in linked lists
        cout<<" __ ";

    }
       for (auto it=topOfPile[first];it!=nullptr;it++){
        cout<<(*it).face<<(*it).suit<<" ";

       }cout<<endl;
    
   
  }     
    continue;
  }
  if (piles[j].isEmpty()){
      cout<<"Cannot move card to an empty stack"<<endl;

   for(int first=0;first<PILES;first++){      //iterating through array
     cout<<first+1<<". ";
    for(auto it = piles[first].begin();it!=piles[first].end();it++){ //iterating through nodes in linked lists
        cout<<" __ ";

    }
       for (auto it=topOfPile[first];it!=nullptr;it++){
        cout<<(*it).face<<(*it).suit<<" ";

       }cout<<endl;
    
   
  }    
      continue;
  }
bool jj=true;  //checking to
  if((*piles[j].end()).suit=='S'||(*piles[j].end()).suit=='C'){
    jj=true;
  }
  else{
    if((*piles[j].end()).suit=='H'||(*piles[j].end()).suit=='D'){
    jj=false;
  }
  }

  bool ii=true;   //checking from
  if((*piles[i].end()).suit=='S'||(*piles[i].end()).suit=='C'){
    ii=false;
  }
  else{
    if((*piles[i].end()).suit=='H'||(*piles[i].end()).suit=='D'){
    ii=true;
  }
  }

  if((((*topOfPile[i]).face)==(*piles[j].end()).face-1) &&(jj==ii)){
    LL<cardType>::iterator last = piles[i].end();
    piles[i].remove(topOfPile[i]);
    piles[j].tailInsert(topOfPile[i], last);
    topOfPile[i]=piles[i].end();
  
     
  for(int first=0;first<PILES;first++){      //iterating through array
    cout<<first+1<<": ";
    for(auto it = piles[first].begin();it!=topOfPile[first];it++){ //iterating through nodes in linked lists
        cout<<"__"<<" ";

    }
       for (auto it=topOfPile[first];it!=nullptr;it++){
        // if(it==topOfPile[i])
        cout<<(*it).face<<(*it).suit<<" ";

       }cout<<endl;
    
   
  }                                    

  }
 else
 {   cout<<"Invalid move"<<endl;
 for(int first=0;first<PILES;first++){      //iterating through array
   cout<<first+1<<". ";
    for(auto it = piles[first].begin();it!=piles[first].end();it++){ //iterating through nodes in linked lists
        cout<<" __ ";

    }
       for (auto it=topOfPile[first];it!=nullptr;it++){
        cout<<(*it).face<<(*it).suit<<" ";

       }cout<<endl;
    
   
  }   

 }

}
 
  return 0;
}