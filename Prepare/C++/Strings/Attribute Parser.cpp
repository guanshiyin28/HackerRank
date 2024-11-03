#include <cmath>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstdio>  // For freopen
#include <map>
using namespace std;


class Node {

    public:
        string data;
        vector<Node*> children;
        void add_child(Node* node);
        bool has_child(const string tag_name);
        Node* get_prev(Node* node);
        Node* get_next(Node* node);
        Node* get_last(Node* node);
        Node* get_node(int index);
        bool remove_node(const string& data);
        
 
        // Constructor
        Node(const std::string& value) : data(value) {}

        // Deep copy constructor
        Node(const Node& other) {
            data = other.data;
            // Recursively copy all children
            for (Node* child : other.children) {
                children.push_back(new Node(*child)); // Deep copy
            }
        }

};

bool Node::has_child(const string tag_name) {
    for (Node* child : children) {
        if (child->data == tag_name) {
            return true;  // Child with the specified data found
        }
    }
    return false;  // No child with the specified data found
}

void Node::add_child(Node* node) {
    children.push_back(node);
}


Node* Node::get_last(Node* node) {
    return children[children.size() -1];
}

Node* Node::get_node(int index) {
   if (index >= 0 && static_cast<size_t>(index) < children.size()) {
        return children[index];
    }
    return nullptr;  // Return nullptr if index is out of bounds
}

Node* Node::get_prev(Node* node) {
    Node* prev_child = nullptr;
    Node* current_child = nullptr;
    for (Node* child : children) {
        prev_child = current_child;
        if (node->data == child->data) {
            current_child = node;
        }
    }
    return prev_child;
}

Node* Node::get_next(Node* node) {
    Node* next_child = nullptr;
    Node* current_child = nullptr;
    int i = 0;
    for (Node* child : children) {
        if (node->data == child->data) {
            current_child = node;
            if (children.size() > i) {
                next_child = children[ i + 1];
            }
        }
        i++;
    }
    return next_child;
}

bool Node::remove_node(const string& data) {
    // Iterate through the list of children
    for (auto it = children.begin(); it != children.end(); ++it) {
        if ((*it)->data == data) {
            // Remove the node if data matches
            delete *it; // Free memory
            children.erase(it); // Erase the node from the vector
            return true; // Node removed successfully
        }
    }
    return false; // Node not found
}

class HRML_Parser {

    private:
        vector<Node*> node_tree; // contains all vectors of tags
        map<string, map<string, string> > node_map;
        Node* root_node = nullptr;


    private:
        string get_tag_name(const string& node);
        // map_node_attributes
        size_t create_node_map(string current_tag, string node, size_t starting_pos) ;
        void remove_character(string& string_to_update, const char char_to_remove);
        bool validate_query(const string& query);
        vector<string> split_string(const string& str, char delimiter);

    public:
        void build_node_tree(const string& hrml_node);
        void build_attribute_map(const string& hrml_node);
        void handle_queries(const string& query);
      
};


void HRML_Parser::remove_character(string& string_to_update, const char char_to_remove) {
    string_to_update.erase(remove(string_to_update.begin(), string_to_update.end(), char_to_remove), string_to_update.end());
}


void HRML_Parser::build_node_tree(const string& hrml_node) 
{
    string tag_name = get_tag_name(hrml_node);
    
    Node* current_node = new Node(tag_name);
    // There is not root node 
    if (root_node == nullptr) {
        root_node = current_node;
    } else {
        // if a tag is closed which is not the root tag
        if (hrml_node.substr(0, 2) == "</" && root_node->data == tag_name) {

            if (node_tree.size() == 0) {
                node_tree.push_back(new Node(*root_node));
            }
            root_node = nullptr;
            
            // the root node is closed, so we null it
        } else if (hrml_node.substr(0, 2) == "</" && tag_name == root_node->get_last(current_node)->data) {
            node_tree.push_back(new Node(*root_node));  // contains a, b
            root_node->remove_node(current_node->data);
        }  else {
            root_node->add_child(current_node);
        }
    }
}

void HRML_Parser::build_attribute_map(const string& hrml_node) 
{
    string tag_name = get_tag_name(hrml_node);
    size_t current_end_position = hrml_node.find(" ", 0);

     /**
     * Loops through all attributes in a specific node
     */
    bool node_parsed_done = false;
    int attributes_parsed = 0;
    
    while (node_parsed_done == false) {
        attributes_parsed++;
        current_end_position = create_node_map(tag_name, hrml_node, current_end_position + 1);
        if (current_end_position == string::npos) {
            node_parsed_done = true;
            return;
        } else if (current_end_position + attributes_parsed  >= hrml_node.length()) {
            node_parsed_done = true;
        }
    }
}

void HRML_Parser::handle_queries(const string& query) {
    if (query.find('~') == string::npos) {
        cout << "Invalid query!!" << endl;
        return;
    }

    if (!validate_query(query)) {
        cout << "Not Found!" << endl;
        return;
    }

    size_t tag_start = query.find_last_of('.');
    size_t tag_end = query.find_first_of("~");
    if (tag_start == string::npos) {
        // e.g tag1~name
        tag_start = 0;
    }  else {
        tag_start = tag_start +1;
    }
    
    tag_end = tag_end +1;
    string tag = query.substr(tag_start, tag_end - 1 - tag_start);
    string attribute = query.substr(tag_end, query.length());
    map<string, string> node_map_tag = node_map[tag];
    auto iter = node_map_tag.find(attribute);
    if (iter != node_map_tag.end()) {
        // Key exists, access the value
        cout << iter->second << endl;
    } else {
        // Key does not exist
        cout << "Not Found!" << endl;
    }
}


string HRML_Parser::get_tag_name(const string& hrml_node) 
{
    string tag_name;
    size_t tag_end = hrml_node.find_first_of(" ", 0);
    if (tag_end == string::npos) {
        tag_end = hrml_node.find(">", 0);
    }
    if (tag_end == string::npos) {
       cerr << "Cannot parse tag" << endl;
       return "";
    }

    tag_end = tag_end - 1;
    tag_name = hrml_node.substr(0, 2) == "</" ? hrml_node.substr(2, tag_end) : hrml_node.substr(1, tag_end);
    remove_character(tag_name, '>');
    remove_character(tag_name, ' ');
    return tag_name;
}

size_t HRML_Parser::create_node_map(string current_tag, string node, size_t starting_pos) {
    size_t equal_sign_pos = node.find("=", starting_pos);
    if (equal_sign_pos == string::npos) {
        return string::npos;
    }
    string attribute_name = node.substr(starting_pos, equal_sign_pos - starting_pos); // another
    size_t quote_start_pos = node.find('"', equal_sign_pos);
    size_t quote_end_pos = node.find('"', quote_start_pos + 1);
     if (quote_start_pos == string::npos || quote_end_pos == string::npos) {
        return string::npos;
    }
    quote_start_pos = quote_start_pos + 1;
    string attribute_value = node.substr(quote_start_pos, quote_end_pos - quote_start_pos); // foo
    remove_character(attribute_name, ' ');
    remove_character(attribute_value, '"');
    node_map[current_tag][attribute_name] = attribute_value;
    return quote_end_pos;
}



bool HRML_Parser::validate_query(const string& query) {
    size_t tag_start = query.find('.');
    size_t tag_end = query.find_first_of("~");
    vector<string> tags;
    string current_tag;

    // this can be put into a method - get tags from query
    if (tag_start == string::npos) {
        // e.g tag1~name
        tag_start = 0;
        current_tag = query.substr(tag_start, tag_end);
        tags.push_back(current_tag);
    }  else {
        // a.c.d.e~strength
        tag_start = 0;
        current_tag = query.substr(tag_start, tag_end);
        tags = split_string(current_tag, '.');
    }
    
    for(Node* node : node_tree) {
        if(node->data == tags[0]) {
            int index = 0;
            for(string tag : tags) {
                // skip first tag 
                if (tag != tags[0]) {
                    if (node->get_node(index -1) == nullptr || node->get_node(index -1)->data != tag) {
                        break;
                    }
                }
                index++;
                // all tags found !
                if (index == tags.size()) {
                    return true; 
                }
            }
        }

        }

    return false;
}

vector<string> HRML_Parser::split_string(const string& str, char delimiter) {
    vector<string> result;
    string temp = "";

    for (char ch : str) {
        if (ch == delimiter) {
            if (!temp.empty()) {
                result.push_back(temp);  // Add substring to the result
                temp = "";  // Reset temp string
            }
        } else {
            temp += ch;  // Build the substring
        }
    }

    // Add the last substring (if any)
    if (!temp.empty()) {
        result.push_back(temp);
    }

    return result;
}



int main() {

    int lines, queries;
    cin >> lines >> queries;
    cin.ignore(); 

    HRML_Parser parser;
    string hrml_node;
    string query_request;

    for (int i = 0; i < lines; ++i) {
        getline(cin, hrml_node);
        parser.build_node_tree(hrml_node);
        parser.build_attribute_map(hrml_node);
    }

     for (int i = 0; i < queries; i++) {
        getline(cin, query_request);
        parser.handle_queries(query_request);
    }


    return 0;
}
