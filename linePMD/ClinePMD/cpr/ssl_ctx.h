#ifndef CPR_SSL_CTX_H
#define CPR_SSL_CTX_H

#include "cpr/ssl_options.h"
#include <curl/curl.h>

#if SUPPORT_CURLOPT_SSL_CTX_FUNCTION

namespace cpr {

CURLcode sslctx_function_load_ca_cert_from_buffer(CURL* curl, void* sslctx, void* raw_cert_buf);

} // Namespace cpr

#endif

#endif