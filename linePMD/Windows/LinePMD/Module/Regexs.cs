using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Text.RegularExpressions;

namespace LinePMD.Module
{
    public class Regexs
    {
        #region 正規表達式

        /// <summary>
        /// 正規表達式 找尋None
        /// </summary>
        /// <param name="text">查找字串</param>
        /// <returns></returns>
        public static bool FindNone(string text)
        {
            Regex regex = new Regex(@"None[\s]?$", RegexOptions.Compiled);
            Match match = regex.Match(text);
            return match.Success;
        }

        /// <summary>
        /// 正規表達式 找尋Mid
        /// </summary>
        /// <param name="text">查找字串</param>
        /// <returns></returns>
        public static Tuple<bool, string, List<string>> FindMid(string text)
        {
            string pattern = @"u[\da-fA-f]{32}";
            Regex regex = new Regex(pattern, RegexOptions.Compiled);
            Match match = regex.Match(text);
            List<string> matches = new List<string>();
            foreach (Match res in Regex.Matches(text, pattern))
            {
                matches.Add(res.ToString());
            }
            return Tuple.Create(match.Success, match.ToString(), matches);
        }

        /// <summary>
        /// 正規表達式 找尋Gid
        /// </summary>
        /// <param name="text">查找字串</param>
        /// <returns></returns>
        public static Tuple<bool, string, List<string>> FindGid(string text)
        {
            string pattern = @"c[\da-fA-F]{32}";
            Regex regex = new Regex(pattern, RegexOptions.Compiled);
            Match match = regex.Match(text);
            List<string> matches = new List<string>();
            foreach (Match res in Regex.Matches(text, pattern))
            {
                matches.Add(res.ToString());
            }
            return Tuple.Create(match.Success, match.ToString(), matches);
        }

        /// <summary>
        /// 正規表達式 找尋Mail
        /// </summary>
        /// <param name="text">查找字串</param>
        /// <returns></returns>
        public static Tuple<bool, string, List<string>> FindMail(string text)
        {
            string pattern = @"[^\s@]+@[^@]+\.[^@]+";
            Regex regex = new Regex(pattern, RegexOptions.Compiled);
            Match match = regex.Match(text);
            List<string> matches = new List<string>();
            foreach (Match res in Regex.Matches(text, pattern))
            {
                matches.Add(res.ToString());
            }
            return Tuple.Create(match.Success, match.ToString(), matches);
        }

        /// <summary>
        /// 正規表達式 找尋Password
        /// </summary>
        /// <param name="text">找尋字串</param>
        /// <returns></returns>
        public static Tuple<bool, string> FindPassword(string text)
        {
            Regex regex = new Regex(@"[pasword\s\=]{11}(?<PWD>(.+))", RegexOptions.Compiled);
            string match = regex.Match(text).Groups["PWD"].ToString();
            bool IsMatch = match != string.Empty ? true : false;
            return Tuple.Create(IsMatch, match);
        }

        /// <summary>
        /// 正規表達式 找尋Token
        /// </summary>
        /// <param name="text">找尋字串</param>
        /// <returns></returns>
        public static Tuple<bool, string, List<string>> FindToken(string text)
        {
            string pattern = @"[\d\w\/\+]{20}\.[\d\w\/\+]{22}\.[\d\w\/\+]{43}=$";
            Regex regex = new Regex(pattern, RegexOptions.Compiled);
            Match match = regex.Match(text);
            List<string> matches = new List<string>();
            foreach (Match res in Regex.Matches(text, pattern))
            {
                matches.Add(res.ToString());
            }
            return Tuple.Create(match.Success, match.ToString(), matches);
        }

        /// <summary>
        /// 正規表達式 找尋Cert
        /// </summary>
        /// <param name="text">找尋字串</param>
        /// <returns></returns>
        public static Tuple<bool, string, List<string>> FindCert(string text)
        {
            string pattern = @"[\da-fA-F]{64}";
            Regex regex = new Regex(pattern,RegexOptions.Compiled);
            Match match = regex.Match(text);
            List<string> matches = new List<string>();
            foreach (Match res in Regex.Matches(text, pattern))
            {
                matches.Add(res.ToString());
            }
            return Tuple.Create(match.Success, match.ToString(), matches);
        }

        public static Tuple<bool, string, List<string>> FindUrl(string text)
        {
            string pattern = @"[htp:|htps:]?/?/?line\.me/?R?/ti/g/(?<URL>([\w-]{10}))";
            Regex regex = new Regex(pattern, RegexOptions.Compiled);
            string match = regex.Match(text).Groups["URL"].ToString();
            bool IsMatch = match != string.Empty? true : false;
            List<string> matches = new List<string>();
            foreach (Match res in Regex.Matches(text, pattern))
            {
                matches.Add(regex.Match(res.ToString()).Groups["URL"].ToString());
            }
            return Tuple.Create(IsMatch, match, matches);
        }

        #endregion
    }
}
