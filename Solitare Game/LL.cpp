#include "LL.h"

template <class type>
LL<type>::LL(const LL<type> &copy)
{

  head = nullptr;
  tail = nullptr;
  const node *iter = copy.head;
  while (iter != nullptr)
  {
    this->tailInsert(iter->data);
    iter = iter->next;
  }
}

template <class type>
const LL<type> &LL<type>::operator=(const LL<type> &rhs)
{
  if (this != &rhs)
  {
    if (!isEmpty())
    {
      while (head != nullptr)
      {
        node *temp = head;
        head = head->next;
        delete temp;
      }
      head=tail=nullptr;
    }
    const node *current = rhs.head;
    while (current != nullptr)
    {
      tailInsert(current->data);
      current = current->next;
    }
  }
  return *this;
}

template <class type>
LL<type>::~LL()
{
  while (head != nullptr)
  {
    node *temp = head;
    head = head->next;
    delete temp;
  }
  head=tail=nullptr;
}
template <class type>
void LL<type>::tailInsert(const type &data)
{
  node *end = new node;
  end->next = nullptr;
  end->data = data;
  if (isEmpty())
  {
    head = tail = end;
    head->prev = nullptr;
  }
  else
  {
    tail->next = end;
    end->prev = tail;
  }
  tail = end;
}

template <class type>
void LL<type>::tailInsert(const iterator &s, const iterator &t)
{
  if (isEmpty())
  {
    head = s.current;
    tail = t.current;
    head->prev=nullptr;
  }
  else
  {
    tail->next = s.current;
    s.current->prev = tail;
    tail = t.current;
  }
}

template <class type>
void LL<type>::tailInsert(const iterator &s)
{
  if (isEmpty())
  {
    head = s.current;
    tail = s.current;
  }
  else
  {
    tail->next = s.current;
    s.current->prev = tail;
    tail = s.current;
  }
}

template <class type>
void LL<type>::remove(iterator &it)
{
  if(isEmpty()){
    return;
  }
  if(head==it.current){
    head=tail=nullptr;
  }else{
  tail = it.current->prev;
  tail->next = nullptr;
  it.current->prev = nullptr;
  }

}

template <class type>
void LL<type>::headRemove()
{
  if(head->next==nullptr){
    delete head;
    head=tail=nullptr;
  }else{
  node *temp = head;
  head = head->next;
  delete temp;
  }

}
