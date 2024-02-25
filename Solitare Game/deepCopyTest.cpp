#include "LL.h"
#include "LL.cpp"
#include <iostream>
#include <string>
using namespace std;

int main()
{
	LL<string> list1;

	LL<string>::iterator nil;

	list1.tailInsert("Sponge");
	list1.tailInsert("Bob");
	list1.tailInsert("Square");
	list1.tailInsert("Pants");

	LL<string> list2(list1);

	list2.tailInsert("Mermaid_Man");
	list2.tailInsert("Barnacle_Boy");

	cout << "------------------------------------------" << endl;
	cout << "Initial list1 and list2" << endl << endl;

	cout << "list1 (Forward): ";
	for (auto it = list1.begin(); it != nil; it++)
		cout << *it << " ";
	cout << endl;

	cout << "list1 (Backwards): ";
	for (auto it = list1.end(); it != nil; it--)
		cout << *it << " ";
	cout << endl;

	cout << "list2 (Forward): ";
	for (auto it = list2.begin(); it != nil; it++)
		cout << *it << " ";
	cout << endl;

	cout << "list2 (Backwards): ";
	for (auto it = list2.end(); it != nil; it--)
		cout << *it << " ";
	cout << endl;

	cout << "------------------------------------------" << endl;
	cout << "Assignment operator into an empty list" << endl << endl;

	LL<string> list3;

	list3 = list2;

	list3.tailInsert("Butters");

	cout << "list2 (Forward): ";
	for (auto it = list2.begin(); it != nil; it++)
		cout << *it << " ";
	cout << endl;

	cout << "list2 (Backwards): ";
	for (auto it = list2.end(); it != nil; it--)
		cout << *it << " ";
	cout << endl;

	cout << "list3 (Forward): ";
	for (auto it = list3.begin(); it != nil; it++)
		cout << *it << " ";
	cout << endl;

	cout << "list3 (Backwards): ";
	for (auto it = list3.end(); it != nil; it--)
		cout << *it << " ";
	cout << endl;


	cout << "------------------------------------------" << endl;
	cout << "Assignment operator into an existing list" << endl << endl;

	list1 = list3;

	list1.tailInsert("That\'s_me");

	cout << "list1 (Forward): ";
	for (auto it = list1.begin(); it != nil; it++)
		cout << *it << " ";
	cout << endl;

	cout << "list1 (Backwards): ";
	for (auto it = list1.end(); it != nil; it--)
		cout << *it << " ";
	cout << endl;

	cout << "list3 (Forward): ";
	for (auto it = list3.begin(); it != nil; it++)
		cout << *it << " ";
	cout << endl;

	cout << "list3 (Backwards): ";
	for (auto it = list3.end(); it != nil; it--)
		cout << *it << " ";
	cout << endl;

	return 0;
}