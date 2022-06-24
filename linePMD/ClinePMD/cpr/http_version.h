#ifndef CPR_HTTP_VERSION_H
#define CPR_HTTP_VERSION_H

#include <curl/curlver.h>

namespace cpr {
enum class HttpVersionCode {
    VERSION_NONE,
    /**
     * Enforce HTTP 1.0 requests ~
     **/
    VERSION_1_0,
    /**
     * Enforce HTTP 1.1 requests ~
     **/
    VERSION_1_1,
#if LIBCURL_VERSION_NUM >= 0x072100
    VERSION_2_0,
#endif
#if LIBCURL_VERSION_NUM >= 0x072F00
    VERSION_2_0_TLS,
#endif
#if LIBCURL_VERSION_NUM >= 0x073100
    VERSION_2_0_PRIOR_KNOWLEDGE,
#endif
#if LIBCURL_VERSION_NUM >= 0x074200
    VERSION_3_0
#endif
};

class HttpVersion {
  public:
    HttpVersionCode code = HttpVersionCode::VERSION_NONE;

    HttpVersion() = default;
    explicit HttpVersion(HttpVersionCode _code) : code(_code) {}
};

} // namespace cpr

#endif
