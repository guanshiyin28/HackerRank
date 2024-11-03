#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Message {
public: 
    Message() {}
    Message(string text, int id):msg_body(text), msg_id(id) {}
    const string& get_text() {
        return msg_body;
    }
    bool operator<(const Message& other) const {
        return this->msg_id < other.msg_id;
    }
    
private:
    string msg_body;
    int msg_id;
};

class MessageFactory {
public:
    MessageFactory() {}
    Message create_message(const string& text) {
        msg_counter += 1;
        return Message(text, msg_counter);
    }
private:
    int msg_counter = -1;
};

class Recipient {
public:
    Recipient() {}
    void receive(const Message& msg) {
        messages_.push_back(msg);
    }
    void print_messages() {
        fix_order();
        for (auto& msg : messages_) {
            cout << msg.get_text() << endl;
        }
        messages_.clear();
    }
private:
    void fix_order() {
        sort(messages_.begin(), messages_.end());
    }
    vector<Message> messages_;
};

class Network {
public:
    static void send_messages(vector<Message> messages, Recipient& recipient) {
    // simulates the unpredictable network, where sent messages might arrive in unspecified order
        random_shuffle(messages.begin(), messages.end());         
        for (auto msg : messages) {
            recipient.receive(msg);
        }
    }
};



int main() {
    MessageFactory message_factory;
    Recipient recipient;
    vector<Message> messages;
    string text;
    while (getline(cin, text)) {
        messages.push_back(message_factory.create_message(text));
    }
    Network::send_messages(messages, recipient);
    recipient.print_messages();
}
