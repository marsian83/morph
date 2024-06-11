#include <iostream>
#include <string>
#include <cstring>

extern "C" const char* greet(const char* name) {
    std::string greeting = "Hello, ";
    greeting += name;
    greeting += "! I am not happy to meet you.";
    return strdup(greeting.c_str());
}
