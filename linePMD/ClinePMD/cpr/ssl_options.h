#ifndef CPR_SSLOPTIONS_H
#define CPR_SSLOPTIONS_H

#include <memory>
#include <string>
#include <vector>

#include <curl/curl.h>

#include <utility>

#define __LIBCURL_VERSION_GTE(major, minor) ((LIBCURL_VERSION_MAJOR > (major)) || ((LIBCURL_VERSION_MAJOR == (major)) && (LIBCURL_VERSION_MINOR >= (minor))))
#define __LIBCURL_VERSION_LT(major, minor) ((LIBCURL_VERSION_MAJOR < (major)) || ((LIBCURL_VERSION_MAJOR == (major)) && (LIBCURL_VERSION_MINOR < (minor))))

#ifndef SUPPORT_ALPN
#define SUPPORT_ALPN __LIBCURL_VERSION_GTE(7, 36)
#endif
#ifndef SUPPORT_NPN
#define SUPPORT_NPN __LIBCURL_VERSION_GTE(7, 36)
#endif

#ifndef SUPPORT_SSLv2
#define SUPPORT_SSLv2 __LIBCURL_VERSION_LT(7, 19)
#endif
#ifndef SUPPORT_SSLv3
#define SUPPORT_SSLv3 __LIBCURL_VERSION_LT(7, 39)
#endif
#ifndef SUPPORT_TLSv1_0
#define SUPPORT_TLSv1_0 __LIBCURL_VERSION_GTE(7, 34)
#endif
#ifndef SUPPORT_TLSv1_1
#define SUPPORT_TLSv1_1 __LIBCURL_VERSION_GTE(7, 34)
#endif
#ifndef SUPPORT_TLSv1_2
#define SUPPORT_TLSv1_2 __LIBCURL_VERSION_GTE(7, 34)
#endif
#ifndef SUPPORT_TLSv1_3
#define SUPPORT_TLSv1_3 __LIBCURL_VERSION_GTE(7, 52)
#endif
#ifndef SUPPORT_MAX_TLS_VERSION
#define SUPPORT_MAX_TLS_VERSION __LIBCURL_VERSION_GTE(7, 54)
#endif
#ifndef SUPPORT_MAX_TLSv1_1
#define SUPPORT_MAX_TLSv1_1 __LIBCURL_VERSION_GTE(7, 54)
#endif
#ifndef SUPPORT_MAX_TLSv1_2
#define SUPPORT_MAX_TLSv1_2 __LIBCURL_VERSION_GTE(7, 54)
#endif
#ifndef SUPPORT_MAX_TLSv1_3
#define SUPPORT_MAX_TLSv1_3 __LIBCURL_VERSION_GTE(7, 54)
#endif
#ifndef SUPPORT_TLSv13_CIPHERS
#define SUPPORT_TLSv13_CIPHERS __LIBCURL_VERSION_GTE(7, 61)
#endif
#ifndef SUPPORT_SESSIONID_CACHE
#define SUPPORT_SESSIONID_CACHE __LIBCURL_VERSION_GTE(7, 16)
#endif
#ifndef SUPPORT_SSL_FALSESTART
#define SUPPORT_SSL_FALSESTART __LIBCURL_VERSION_GTE(7, 42)
#endif
#ifndef SUPPORT_SSL_NO_REVOKE
#define SUPPORT_SSL_NO_REVOKE __LIBCURL_VERSION_GTE(7, 44)
#endif
#ifndef SUPPORT_CURLOPT_SSLKEY_BLOB
#define SUPPORT_CURLOPT_SSLKEY_BLOB __LIBCURL_VERSION_GTE(7, 71)
#endif
#ifndef SUPPORT_CURLOPT_SSL_CTX_FUNCTION
#define SUPPORT_CURLOPT_SSL_CTX_FUNCTION __LIBCURL_VERSION_GTE(7, 11)
#endif

namespace cpr {

class VerifySsl {
  public:
    VerifySsl() = default;
    VerifySsl(bool p_verify) : verify(p_verify) {}

    explicit operator bool() const {
        return verify;
    }

    bool verify = true;
};

namespace ssl {

// set SSL client certificate
class CertFile {
  public:
    CertFile(std::string&& p_filename) : filename(std::move(p_filename)) {}

    virtual ~CertFile() = default;

    const std::string filename;

    virtual const char* GetCertType() const {
        return "PEM";
    }
};

using PemCert = CertFile;

class DerCert : public CertFile {
  public:
    DerCert(std::string&& p_filename) : CertFile(std::move(p_filename)) {}

    virtual ~DerCert() = default;

    const char* GetCertType() const override {
        return "DER";
    }
};

// specify private keyfile for TLS and SSL client cert ~
class KeyFile {
  public:
    KeyFile(std::string&& p_filename) : filename(std::move(p_filename)) {}

    template <typename FileType, typename PassType>
    KeyFile(FileType&& p_filename, PassType p_password) : filename(std::forward<FileType>(p_filename)), password(std::move(p_password)) {}

    virtual ~KeyFile() = default;

    std::string filename;
    std::string password;

    virtual const char* GetKeyType() const {
        return "PEM";
    }
};

#if SUPPORT_CURLOPT_SSLKEY_BLOB
class KeyBlob {
  public:
    KeyBlob(std::string&& p_blob) : blob(std::move(p_blob)) {}

    template <typename BlobType, typename PassType>
    KeyBlob(BlobType&& p_blob, PassType p_password) : blob(std::forward<BlobType>(p_blob)), password(std::move(p_password)) {}

    virtual ~KeyBlob() = default;

    std::string blob;
    std::string password;

    virtual const char* GetKeyType() const {
        return "PEM";
    }
};
#endif

using PemKey = KeyFile;

class DerKey : public KeyFile {
  public:
    DerKey(std::string&& p_filename) : KeyFile(std::move(p_filename)) {}

    template <typename FileType, typename PassType>
    DerKey(FileType&& p_filename, PassType p_password) : KeyFile(std::forward<FileType>(p_filename), std::move(p_password)) {}

    virtual ~DerKey() = default;

    const char* GetKeyType() const override {
        return "DER";
    }
};

class PinnedPublicKey {
  public:
    PinnedPublicKey(std::string&& p_pinned_public_key) : pinned_public_key(std::move(p_pinned_public_key)) {}

    const std::string pinned_public_key;
};

#if SUPPORT_ALPN
class ALPN {
  public:
    ALPN() = default;
    ALPN(bool p_enabled) : enabled(p_enabled) {}

    explicit operator bool() const {
        return enabled;
    }

    bool enabled = true;
};
#endif

#if SUPPORT_NPN
class NPN {
  public:
    NPN() = default;
    NPN(bool p_enabled) : enabled(p_enabled) {}

    explicit operator bool() const {
        return enabled;
    }

    bool enabled = true;
};
#endif

class VerifyHost {
  public:
    VerifyHost() = default;
    VerifyHost(bool p_enabled) : enabled(p_enabled) {}

    explicit operator bool() const {
        return enabled;
    }

    bool enabled = true;
};

class VerifyPeer {
  public:
    VerifyPeer() = default;
    VerifyPeer(bool p_enabled) : enabled(p_enabled) {}

    explicit operator bool() const {
        return enabled;
    }

    bool enabled = true;
};

class VerifyStatus {
  public:
    VerifyStatus(bool p_enabled) : enabled(p_enabled) {}

    explicit operator bool() const {
        return enabled;
    }

    bool enabled = false;
};

// TLS v1.0 or later
struct TLSv1 {};
#if SUPPORT_SSLv2
// SSL v2
struct SSLv2 {};
#endif
#if SUPPORT_SSLv3
// SSL v3
struct SSLv3 {};
#endif
#if SUPPORT_TLSv1_0
// TLS v1.0 or later
struct TLSv1_0 {};
#endif
#if SUPPORT_TLSv1_1
// TLS v1.1 or later
struct TLSv1_1 {};
#endif
#if SUPPORT_TLSv1_2
// TLS v1.2 or later
struct TLSv1_2 {};
#endif
#if SUPPORT_TLSv1_3
// TLS v1.3 or later
struct TLSv1_3 {};
#endif
#if SUPPORT_MAX_TLS_VERSION
struct MaxTLSVersion {};
#endif
#if SUPPORT_MAX_TLSv1_0
struct MaxTLSv1_0 {};
#endif
#if SUPPORT_MAX_TLSv1_1
struct MaxTLSv1_1 {};
#endif
#if SUPPORT_MAX_TLSv1_2
struct MaxTLSv1_2 {};
#endif
#if SUPPORT_MAX_TLSv1_3
struct MaxTLSv1_3 {};
#endif

class CaInfo {
  public:
    CaInfo(std::string&& p_filename) : filename(std::move(p_filename)) {}

    std::string filename;
};

class CaPath {
  public:
    CaPath(std::string&& p_filename) : filename(std::move(p_filename)) {}

    std::string filename;
};

#if SUPPORT_CURLOPT_SSL_CTX_FUNCTION
class CaBuffer {
  public:
    CaBuffer(std::string&& p_buffer) : buffer(std::move(p_buffer)) {}

    const std::string buffer;
};
#endif

class Crl {
  public:
    Crl(std::string&& p_filename) : filename(std::move(p_filename)) {}

    std::string filename;
};

class Ciphers {
  public:
    Ciphers(std::string&& p_ciphers) : ciphers(std::move(p_ciphers)) {}

    std::string ciphers;
};

#if SUPPORT_TLSv13_CIPHERS
class TLS13_Ciphers {
  public:
    TLS13_Ciphers(std::string&& p_ciphers) : ciphers(std::move(p_ciphers)) {}

    std::string ciphers;
};
#endif

#if SUPPORT_SESSIONID_CACHE
class SessionIdCache {
  public:
    SessionIdCache() = default;
    SessionIdCache(bool p_enabled) : enabled(p_enabled) {}

    explicit operator bool() const {
        return enabled;
    }

    bool enabled = true;
};
#endif

#if SUPPORT_SSL_FALSESTART
class SslFastStart {
  public:
    SslFastStart() = default;
    SslFastStart(bool p_enabled) : enabled(p_enabled) {}

    explicit operator bool() const {
        return enabled;
    }

    bool enabled = false;
};
#endif

class NoRevoke {
  public:
    NoRevoke() = default;
    NoRevoke(bool p_enabled) : enabled(p_enabled) {}

    explicit operator bool() const {
        return enabled;
    }

    bool enabled = false;
};

} // namespace ssl

struct SslOptions {
    std::string cert_file;
    std::string cert_type;
    std::string key_file;
#if SUPPORT_CURLOPT_SSLKEY_BLOB
    std::string key_blob;
#endif
    std::string key_type;
    std::string key_pass;
    std::string pinned_public_key;
#if SUPPORT_ALPN
    bool enable_alpn = true;
#endif
#if SUPPORT_NPN
    bool enable_npn = true;
#endif
    bool verify_host = true;
    bool verify_peer = true;
    bool verify_status = false;
    int ssl_version = CURL_SSLVERSION_DEFAULT;
#if SUPPORT_SSL_NO_REVOKE
    bool ssl_no_revoke = false;
#endif
#if SUPPORT_MAX_TLS_VERSION
    int max_version = CURL_SSLVERSION_MAX_DEFAULT;
#endif
    std::string ca_info;
    std::string ca_path;
#if SUPPORT_CURLOPT_SSL_CTX_FUNCTION
    std::string ca_buffer;
#endif
    std::string crl_file;
    std::string ciphers;
#if SUPPORT_TLSv13_CIPHERS
    std::string tls13_ciphers;
#endif
#if SUPPORT_SESSIONID_CACHE
    bool session_id_cache = true;
#endif

    void SetOption(const ssl::CertFile& opt) {
        cert_file = opt.filename;
        cert_type = opt.GetCertType();
    }
    void SetOption(const ssl::KeyFile& opt) {
        key_file = opt.filename;
        key_type = opt.GetKeyType();
        key_pass = opt.password;
    }
#if SUPPORT_CURLOPT_SSLKEY_BLOB
    void SetOption(const ssl::KeyBlob& opt) {
        key_blob = opt.blob;
        key_type = opt.GetKeyType();
        key_pass = opt.password;
    }
#endif
    void SetOption(const ssl::PinnedPublicKey& opt) {
        pinned_public_key = opt.pinned_public_key;
    }

#if SUPPORT_ALPN
    void SetOption(const ssl::ALPN& opt) {
        enable_alpn = opt.enabled;
    }
#endif // SUPPORT_ALPN
#if SUPPORT_NPN
    void SetOption(const ssl::NPN& opt) {
        enable_npn = opt.enabled;
    }
#endif // SUPPORT_NPN
    void SetOption(const ssl::VerifyHost& opt) {
        verify_host = opt.enabled;
    }
    void SetOption(const ssl::VerifyPeer& opt) {
        verify_peer = opt.enabled;
    }
    void SetOption(const ssl::VerifyStatus& opt) {
        verify_status = opt.enabled;
    }
    void SetOption(const ssl::TLSv1& /*opt*/) {
        ssl_version = CURL_SSLVERSION_TLSv1;
    }
#if SUPPORT_SSL_NO_REVOKE
    void SetOption(const ssl::NoRevoke& opt) {
        ssl_no_revoke = opt.enabled;
    }
#endif
#if SUPPORT_SSLv2
    void SetOption(const ssl::SSLv2& /*opt*/) {
        ssl_version = CURL_SSLVERSION_SSLv2;
    }
#endif
#if SUPPORT_SSLv3
    void SetOption(const ssl::SSLv3& /*opt*/) {
        ssl_version = CURL_SSLVERSION_SSLv3;
    }
#endif
#if SUPPORT_TLSv1_0
    void SetOption(const ssl::TLSv1_0& /*opt*/) {
        ssl_version = CURL_SSLVERSION_TLSv1_0;
    }
#endif
#if SUPPORT_TLSv1_1
    void SetOption(const ssl::TLSv1_1& /*opt*/) {
        ssl_version = CURL_SSLVERSION_TLSv1_1;
    }
#endif
#if SUPPORT_TLSv1_2
    void SetOption(const ssl::TLSv1_2& /*opt*/) {
        ssl_version = CURL_SSLVERSION_TLSv1_2;
    }
#endif
#if SUPPORT_TLSv1_3
    void SetOption(const ssl::TLSv1_3& /*opt*/) {
        ssl_version = CURL_SSLVERSION_TLSv1_3;
    }
#endif
#if SUPPORT_MAX_TLS_VERSION
    void SetOption(const ssl::MaxTLSVersion& /*opt*/) {
        max_version = CURL_SSLVERSION_DEFAULT;
    }
#endif
#if SUPPORT_MAX_TLSv1_0
    void SetOption(const ssl::MaxTLSv1_0& opt) {
        max_version = CURL_SSLVERSION_MAX_TLSv1_0;
    }
#endif
#if SUPPORT_MAX_TLSv1_1
    void SetOption(const ssl::MaxTLSv1_1& /*opt*/) {
        max_version = CURL_SSLVERSION_MAX_TLSv1_1;
    }
#endif
#if SUPPORT_MAX_TLSv1_2
    void SetOption(const ssl::MaxTLSv1_2& /*opt*/) {
        max_version = CURL_SSLVERSION_MAX_TLSv1_2;
    }
#endif
#if SUPPORT_MAX_TLSv1_3
    void SetOption(const ssl::MaxTLSv1_3& /*opt*/) {
        max_version = CURL_SSLVERSION_MAX_TLSv1_3;
    }
#endif
    void SetOption(const ssl::CaInfo& opt) {
        ca_info = opt.filename;
    }
    void SetOption(const ssl::CaPath& opt) {
        ca_path = opt.filename;
    }
#if SUPPORT_CURLOPT_SSL_CTX_FUNCTION
    void SetOption(const ssl::CaBuffer& opt) {
        ca_buffer = opt.buffer;
    }
#endif
    void SetOption(const ssl::Crl& opt) {
        crl_file = opt.filename;
    }
    void SetOption(const ssl::Ciphers& opt) {
        ciphers = opt.ciphers;
    }
#if SUPPORT_TLSv13_CIPHERS
    void SetOption(const ssl::TLS13_Ciphers& opt) {
        tls13_ciphers = opt.ciphers;
    }
#endif
#if SUPPORT_SESSIONID_CACHE
    void SetOption(const ssl::SessionIdCache& opt) {
        session_id_cache = opt.enabled;
    }
#endif
};

namespace priv {

template <typename T>
void set_ssl_option(SslOptions& opts, T&& t) {
    opts.SetOption(std::forward<T>(t));
}

template <typename T, typename... Ts>
void set_ssl_option(SslOptions& opts, T&& t, Ts&&... ts) {
    set_ssl_option(opts, std::forward<T>(t));
    set_ssl_option(opts, std::move(ts)...);
}

} // namespace priv

template <typename... Ts>
SslOptions Ssl(Ts&&... ts) {
    SslOptions opts;
    priv::set_ssl_option(opts, std::move(ts)...);
    return opts;
}

} // namespace cpr

#endif
