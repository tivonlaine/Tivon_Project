#include "LL.h"
#include "LL.cpp"
#include <string>
#include <iostream>
using namespace std;

int main()
{
	LL<string> list;
	LL<string>::iterator nil;

	list.tailInsert("Hey");
	list.tailInsert("Oh");
	list.tailInsert("Where");
	list.tailInsert("Did");
	list.tailInsert("All");
	list.tailInsert("The");
	list.tailInsert("Good");
	list.tailInsert("Go?");

	cout << "list (Forward): ";
	for (auto it = list.begin(); it != nil; it++)
		cout << *it << " ";
	cout << endl;


	cout << "list (Backward): ";
	for (auto it = list.end(); it != nil; it--)
		cout << *it << " ";
	cout << endl;
	
	return 0;
}