#ifndef CPR_COOKIES_H
#define CPR_COOKIES_H

#include "cpr/curlholder.h"
#include <initializer_list>
#include <map>
#include <sstream>
#include <string>

namespace cpr {

class Cookies {
  public:
    bool encode{true};

    Cookies(bool p_encode = true) : encode(p_encode) {}
    Cookies(const std::initializer_list<std::pair<const std::string, std::string>>& pairs, bool p_encode = true) : encode(p_encode), map_{pairs} {}
    Cookies(const std::map<std::string, std::string>& map, bool p_encode = true) : encode(p_encode), map_{map} {}

    std::string& operator[](const std::string& key);
    std::string GetEncoded(const CurlHolder& holder) const;

    using iterator = std::map<std::string, std::string>::iterator;
    using const_iterator = std::map<std::string, std::string>::const_iterator;

    iterator begin();
    iterator end();
    const_iterator begin() const;
    const_iterator end() const;
    const_iterator cbegin() const;
    const_iterator cend() const;

  private:
    std::map<std::string, std::string> map_;
};

} // namespace cpr

#endif
