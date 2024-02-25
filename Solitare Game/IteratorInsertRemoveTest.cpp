#include "LL.h"
#include "LL.cpp"
#include <string>
#include <iostream>
using namespace std;

int main()
{
	LL<string> list1;
	LL<string> list2;
	LL<string> list3;

	list1.tailInsert("Bill");
	list1.tailInsert("Ted");
	list1.tailInsert("Tim");
	list1.tailInsert("Eric");
	list1.tailInsert("Pierre");
	list1.tailInsert("Boro");


	list2.tailInsert("Awesome");
	list2.tailInsert("Show");
	list2.tailInsert("Great");
	list2.tailInsert("Job");

	LL<string>::iterator it1, it2, it3, it4;
	LL<string>::iterator nil;


	it1 = list1.begin();
	it1++;
	it1++;
	it2 = list1.end();

	list1.remove(it1);

	list2.tailInsert(it1, it2);
	cout << "-----------------------------------------------------" << endl;
	cout << "Move elements from list1 into list2" << endl << endl;

	cout << "List1 (Forward): ";
	for (auto i = list1.begin(); i != nil; i++)
		cout << *i << " ";
	cout << endl;

	cout << "List1 (Backwards): ";
	for (auto i = list1.end(); i != nil; i--)
		cout << *i << " ";
	cout << endl;


	cout << "List2 (Forward): ";
	for (auto i = list2.begin(); i != nil; i++)
		cout << *i << " ";
	cout << endl;


	cout << "List2 (Backwards): ";
	for (auto i = list2.end(); i != nil; i--)
		cout << *i << " ";
	cout << endl;

	cout << "-----------------------------------------------------" << endl;
	cout << "Remove everything from list2 into list3" << endl << endl;

	it1 = list2.begin();
	it2 = list2.end();

	list2.remove(it1);

	list3.tailInsert(it1, it2);

	cout << "List3 (Forward): ";
	for (auto i = list3.begin(); i != nil; i++)
		cout << *i << " ";
	cout << endl;

	cout << "List3 (Backwards): ";
	for (auto i = list3.end(); i != nil; i--)
		cout << *i << " ";
	cout << endl;

	cout << "List2 (Forward): ";
	for (auto i = list2.begin(); i != nil; i++)
		cout << *i << " ";
	cout << endl;

	cout << "List2 (Backwards): ";
	for (auto i = list2.end(); i != nil; i--)
		cout << *i << " ";
	cout << endl;

	cout << "-----------------------------------------------------" << endl;
	cout << "Move a single item from list3 into (empty) list2" << endl << endl;

	it2 = list3.end();

	list3.remove(it2);

	list2.tailInsert(it2);

	cout << "List3 (Forward): ";
	for (auto i = list3.begin(); i != nil; i++)
		cout << *i << " ";
	cout << endl;

	cout << "List3 (Backwards): ";
	for (auto i = list3.end(); i != nil; i--)
		cout << *i << " ";
	cout << endl;

	cout << "List2 (Forward): ";
	for (auto i = list2.begin(); i != nil; i++)
		cout << *i << " ";
	cout << endl;

	cout << "List2 (Backwards): ";
	for (auto i = list2.end(); i != nil; i--)
		cout << *i << " ";
	cout << endl;


	cout << "-----------------------------------------------------" << endl;
	cout << "Move a single item from list3 into list2 again" << endl << endl;

	it2 = list3.end();
	list3.remove(it2);

	list2.tailInsert(it2);

	cout << "List3 (Forward): ";
	for (auto i = list3.begin(); i != nil; i++)
		cout << *i << " ";
	cout << endl;

	cout << "List3 (Backwards): ";
	for (auto i = list3.end(); i != nil; i--)
		cout << *i << " ";
	cout << endl;

	cout << "List2 (Forward): ";
	for (auto i = list2.begin(); i != nil; i++)
		cout << *i << " ";
	cout << endl;

	cout << "List2 (Backwards): ";
	for (auto i = list2.end(); i != nil; i--)
		cout << *i << " ";
	cout << endl;

	return 0;
}