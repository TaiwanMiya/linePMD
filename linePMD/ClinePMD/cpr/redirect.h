#ifndef CPR_REDIRECT_H
#define CPR_REDIRECT_H

#include <cstdint>

namespace cpr {
enum class PostRedirectFlags : uint8_t {
    POST_301 = 0x1 << 0,
    POST_302 = 0x1 << 1,
    POST_303 = 0x1 << 2,
    POST_ALL = POST_301 | POST_302 | POST_303,
    NONE = 0x0
};

PostRedirectFlags operator|(PostRedirectFlags lhs, PostRedirectFlags rhs);
PostRedirectFlags operator&(PostRedirectFlags lhs, PostRedirectFlags rhs);
PostRedirectFlags operator^(PostRedirectFlags lhs, PostRedirectFlags rhs);
PostRedirectFlags operator~(PostRedirectFlags flag);
PostRedirectFlags& operator|=(PostRedirectFlags& lhs, PostRedirectFlags rhs);
PostRedirectFlags& operator&=(PostRedirectFlags& lhs, PostRedirectFlags rhs);
PostRedirectFlags& operator^=(PostRedirectFlags& lhs, PostRedirectFlags rhs);
bool any(PostRedirectFlags flag);

class Redirect {
  public:
    long maximum{50L};
    bool follow{true};
    bool cont_send_cred{false};
    PostRedirectFlags post_flags{PostRedirectFlags::POST_ALL};

    Redirect() = default;
    Redirect(long p_maximum, bool p_follow, bool p_cont_send_cred, PostRedirectFlags p_post_flags) : maximum(p_maximum), follow(p_follow), cont_send_cred(p_cont_send_cred), post_flags(p_post_flags){};
    explicit Redirect(long p_maximum) : maximum(p_maximum){};
    explicit Redirect(bool p_follow) : follow(p_follow){};
    Redirect(bool p_follow, bool p_cont_send_cred) : follow(p_follow), cont_send_cred(p_cont_send_cred){};
    explicit Redirect(PostRedirectFlags p_post_flags) : post_flags(p_post_flags){};
};
} // namespace cpr

#endif
