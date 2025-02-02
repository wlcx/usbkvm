#pragma once
#include <string>

namespace usbkvm {

class Version {
public:
    static const unsigned int major, minor, micro;
    static std::string get_string();
    static const char *commit;
    static const char *commit_hash;
};

} // namespace usbkvm
