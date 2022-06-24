using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;

namespace LinePMD.Module
{
    public class ReadWrite
    {
        /// <summary>
        /// 非同步處理,獲取終端DOS打印訊息
        /// </summary>
        public static List<string> result { get; set; } = new List<string>();

        public static int PID
        {
            get { return GetPidInDos(); }
        }

        /// <summary>
        /// 遞增獲取上級目錄
        /// </summary>
        /// <param name="path">路徑</param>
        /// <param name="upLevel">遞增數量</param>
        /// <returns></returns>
        public static string GetupLevelDirectory(string path, int upLevel)
        {
            var directory = File.GetAttributes(path).HasFlag(FileAttributes.Directory)
                ? path
                : Path.GetDirectoryName(path);

            upLevel = upLevel < 0 ? 0 : upLevel;
            for (var i = 0; i < upLevel; i++)
            {
                directory = Path.GetDirectoryName(directory);
            }
            return directory;
        }

        /// <summary>
        /// 獲取目前目錄
        /// </summary>
        /// <returns></returns>
        public static string CheakPathRoute()
        {
            string selectpath = Environment.CurrentDirectory;
            selectpath = selectpath.EndsWith("Debug")
                ? GetupLevelDirectory(selectpath, 4)
                : selectpath;
            return selectpath;
        }

        public static bool CheakIsLogin()
        {
            try
            {
                StreamReader reader = new StreamReader(CheakPathRoute()+"\\Txt\\IsLogin.txt");
                reader.Close();
                return true;
            }
            catch (FileNotFoundException)
            {
                return false;
            }
        }

        public static void SetIsLogin(bool onoff)
        {
            if (onoff)
            {
                StreamWriter writer = new StreamWriter(CheakPathRoute()+"\\Txt\\IsLogin.txt");
                writer.WriteLine("");
                writer.Close();
            }
            else
            {
                try
                {
                    File.Delete(CheakPathRoute()+"\\Txt\\IsLogin.txt");
                }
                catch (FileNotFoundException) { }
            }
        }

        public static int GetPidInDos()
        {
            StreamReader reader = new StreamReader(CheakPathRoute() + "\\Txt\\ServoPid.txt");
            int pid = Convert.ToInt32(reader.ReadLine());
            reader.Close();
            File.Delete(CheakPathRoute() + "\\Txt\\ServoPid.txt");
            return pid;
        }

        /// <summary>
        /// 讀取DOS全部字節流
        /// </summary>
        /// <returns></returns>
        public static Tuple<bool, int, List<string>> ReadInstruction()
        {
            bool codecheak = false;
            bool resultcheak = false;
            int code = -1;
            List<string> results = new List<string>();
            try
            {
                StreamReader reader = new StreamReader(Material.thispath + "\\Txt\\ServoResult.txt");
                string line = reader.ReadLine();
                while (line != null)
                {
                    if (line.Trim() == "code")
                    {
                        codecheak = true;
                    }
                    else if (codecheak && line.Trim().All(char.IsDigit))
                    {
                        code = Convert.ToInt32(line.Trim());
                        codecheak = false;
                    }
                    else if (!codecheak && line.Trim() == "result")
                    {
                        resultcheak = true;
                    }
                    else if (resultcheak)
                    {
                        results.Add(line.Trim());
                    }
                    line = reader.ReadLine();
                }
                reader.Close();
                File.Delete(Material.thispath + "\\Txt\\ServoResult.txt");
                return Tuple.Create(true, code, results);
            }
            catch (FileNotFoundException)
            {
                return Tuple.Create(false, code, results);
            }
            catch (IOException)
            {
                return ReadInstruction();
            }
        }

        /// <summary>
        /// 寫入DOS全部字節流
        /// </summary>
        public static void WriteInstruction()
        {
            StreamWriter writer = new StreamWriter(Material.thispath + "\\Txt\\ServoArgs.txt");
            for (int i = 0; i < Material.ServoArgs.Length; i++)
            {
                writer.WriteLine(Material.ServoArgs[i]);
                writer.WriteLine(Material.ServoValues[i]);
                writer.Flush();
            }
            writer.Close();
        }

        /// <summary>
        /// 更新DOS全部權限
        /// </summary>
        public static void WritePermission()
        {
            StreamWriter writer = new StreamWriter(Material.thispath + "\\Txt\\ServoArgs.txt");
            StreamReader reader = new StreamReader(Material.thispath + "\\Txt\\Permission.txt");
            writer.WriteLine("permission");
            string line = reader.ReadLine();
            while (line != null)
            {
                writer.WriteLine(line);
                line = reader.ReadLine();
            }
            reader.Close();
            writer.Close();
        }
    }
}
