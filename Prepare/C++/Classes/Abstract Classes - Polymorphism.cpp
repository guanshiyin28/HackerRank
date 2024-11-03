#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <set>
#include <cassert>
using namespace std;

struct Node{
   Node* next;
   Node* prev;
   int value;
   int key;
   Node(Node* p, Node* n, int k, int val):prev(p),next(n),key(k),value(val){};
   Node(int k, int val):prev(NULL),next(NULL),key(k),value(val){};
};

class Cache{
   
   protected: 
   map<int,Node*> mp; //map the key to the node in the linked list
   int cp;  //capacity
   Node* tail; // double linked list tail pointer
   Node* head; // double linked list head pointer
   virtual void set(int, int) = 0; //set function
   virtual int get(int) = 0; //get function

};

class LRUCache : public Cache 
{
    private:
        int capacity;
        void move_node_to_head(Node* node);
        void remove_node_from_tail(Node* node);
    public:
        LRUCache(int capacity);
        int get(int key);
        void set(int key, int value);
};


LRUCache::LRUCache(int capacity)
{
    this->tail = nullptr;
    this->head = nullptr;
    this->capacity = capacity; 
}


int LRUCache::get(int key)
{
    if (mp[key] == nullptr) {
        return -1;
    }
    int cache_entry = mp[key]->value;
    move_node_to_head(mp[key]);
    return cache_entry;
}

void LRUCache::move_node_to_head(Node* new_head_node)
{
    // In case we are getting or setting a value at the head
    if (head == new_head_node) {
        return;
    }

    // IN case its the very first insert, we set head = tail
    if (tail == nullptr) {
        tail = new_head_node;
    }
    if (head == nullptr) {
        head = new_head_node;
        mp[new_head_node->key] = new_head_node;
        return;
    }

    if (tail->prev == nullptr) {
        tail->prev = head;
    }

    /**
     *  N1 -> next | prv <- N2 -> next 
     * We take the currrent head and move it to the next position, so the new head node next, will point to the current head node previous node
     */
    new_head_node->next = head;   
    new_head_node->prev = nullptr; // A head doesn't have any previous node
    head = new_head_node;

  
    mp[new_head_node->key] = new_head_node;
}


/**
 * Need to remove the tail node and shifting the nodes to the right
 */
void LRUCache::remove_node_from_tail(Node* node)
{
    if (tail == nullptr) {
        return;
    }
    Node* old_tail = tail;
    if (tail->prev != nullptr) {
        tail->prev->next = nullptr; // remove the tail also from the node before
    }
   
    mp.erase(tail->key);
    delete old_tail;
}


void LRUCache::set(int key, int value)
{
    Node* new_node = new Node(key, value);

    // first entry in the list

    if (mp[key] != nullptr) {
        // the Node is existing, so we update the value move to the head
        Node* node = mp[key];
        node->value = value;
        move_node_to_head(new_node);
    } else {
         // Cache is full
        if (mp.size() > this->capacity) {
            // remove node from tail
            remove_node_from_tail(new_node);
        }
        move_node_to_head(new_node);
    } 
}


int main() {
   int n, capacity,i;
   cin >> n >> capacity;
   LRUCache l(capacity);
   for(i=0;i<n;i++) {
      string command;
      cin >> command;
      if(command == "get") {
         int key;
         cin >> key;
         cout << l.get(key) << endl;
      } 
      else if(command == "set") {
         int key, value;
         cin >> key >> value;
         l.set(key,value);
      }
   }
   return 0;
}
