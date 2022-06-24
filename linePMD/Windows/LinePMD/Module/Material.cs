using System;
using System.Collections.Generic;
using System.Windows.Forms;
using System.Drawing;

namespace LinePMD.Module
{
    public class Material
    {
        #region 建構子

        /// <summary>
        /// 初始化是否成功
        /// </summary>
        public static bool InitialDone { get; set; } = false;

        /// <summary>
        /// 終端色彩
        /// </summary>
        public static Color[] TerminalColor { get; set; } = new Color[]
        {
            Color.Black,
            Color.White,
            Color.Gray,
            Color.Red,
            Color.Orange,
            Color.Yellow,
            Color.Green,
            Color.Cyan,
            Color.Blue,
            Color.Purple,
        };

        /// <summary>
        /// 登入檢查
        /// </summary>
        public static bool IsLogin
        {
            get => ReadWrite.CheakIsLogin();
            set => ReadWrite.SetIsLogin(value);
        }

        /// <summary>
        /// 設置獲取目前路徑
        /// </summary>
        public static string thispath { get; set; }

        /// <summary>
        /// DOS input標頭字節流
        /// </summary>
        public static string[] ServoArgs { get; set; } = new string[]
        {
            "to",
            "text",
            "type",
            "from"
        };

        public static string[] ServoArgv { get; set; } = new string[]
        {
            "permission",
            "admin",
            "owner",
            "backdoor"
        };

        /// <summary>
        /// DOS input內容字節流
        /// </summary>
        public static string[] ServoValues { get; set; } = new string[4];

        /// <summary>
        /// 登入標頭
        /// </summary>
        public static string[] LoginTitle { get; set; } = new string[]
        {
            "<mid>",
            "<account>",
            "<password>",
            "<token>",
            "<cert>"
        };

        /// <summary>
        /// 權限標頭
        /// </summary>
        public static string[] permissiontypes { get; set; } = new string[]
        {
            "Admin",
            "Owner",
            "BackDoor"
        };

        public static string[] AllName = new string[]
        {
            "二進位",
            "八進位",
            "十進位",
            "十六進位"
        };

        public static uint[] AllCarry = new uint[]
        {
            2,8,10,16
        };

        public static uint All { get; set; } = 0x00;

        /// <summary>
        /// 登入存檔資訊
        /// </summary>
        public static Dictionary<int, List<string>> LoginInfo { get; set; } = new Dictionary<int, List<string>>();

        public static TextBox[] AllInputCarry { get; set; } = new TextBox[4];

        public static TextBox[] AllOutputCarry { get; set; } = new TextBox[4];

        /// <summary>
        /// 權限資訊
        /// </summary>
        public static Dictionary<string, List<string>> PermissionInfo { get; set; } = new Dictionary<string, List<string>>();

        public static Dictionary<int, string[]> GroupsInfo { get; set; } = new Dictionary<int, string[]>();

        public static Dictionary<int, string[]> GroupMembersInfo { get; set; } = new Dictionary<int, string[]>();

        public static Dictionary<int, string[]> GroupMembersNameInfo { get; set; } = new Dictionary<int, string[]>();

        public static int GroupsIndex { get; set; }

        public static int MembersIndex { get; set; }

        public static int UserFromIndex { get; set; }

        public static string HexExecuteTitle { get; set; }

        public static string HexExecuteArgs { get; set; }

        #endregion

        #region 訊息與終端

        /// <summary>
        /// 錯誤訊息與終端顯示
        /// </summary>
        /// <param name="text">訊息</param>
        public static void ErrorMessage(string text)
        {
            string[] msg = text.Split('\n');
            if (msg.Length > 1)
            {
                for (int i = 0; i < msg.Length; i++)
                {
                    ReadWrite.result.Add(msg[i]);
                }
            }
            else if (msg.Length == 1)
            {
                ReadWrite.result.Add(text);
            }
            MessageBox.Show(text, "錯誤", MessageBoxButtons.OK, MessageBoxIcon.Error);
        }

        #endregion

        public static void InterfaceInitial()
        {
            All = 0x0;
            string[] AdmixCarry = new string[4];
            CarryConversion(All, ref AdmixCarry);
            for (int i = 0;i < AllInputCarry.Length; i++)
            {
                AllOutputCarry[i].Text = AdmixCarry[i];
            }
        }

        public static int GetTerminal(int ItemsCount,int Height,int ItemHeight)
        {
            return ItemsCount - (Height / ItemHeight);
        }

        public static Tuple<string,int> SetTerminal(int top)
        {
            return Tuple.Create("\n", top);
        }

        public static void CarryConversion(uint counter, ref string[] carry)
        {
            carry[0] = Convert.ToString(counter, 2);
            carry[1] = Convert.ToString(counter, 8);
            carry[2] = Convert.ToString(counter);
            carry[3] = Convert.ToString(counter, 16);
        }

        public static void StringToCarry(string text, uint carry, ref uint result)
        {
            result = Convert.ToUInt32(text, Convert.ToInt32(carry));
        }

        public static void SingleConversion(int count)
        {
            try
            {
                uint result = 0x0;
                string[] AllOutput = new string[4];
                StringToCarry(AllInputCarry[count].Text, AllCarry[count], ref result);
                CarryConversion(result, ref AllOutput);
                for (int x = 0; x < AllOutputCarry.Length; x++)
                {
                    AllOutputCarry[x].Text = AllOutput[x];
                }
                HexExecute(AllOutput[3]);
            }
            catch
            {
                ErrorMessage($"轉換{AllName[count]}時錯誤\n進位規則不符!\n" +
                    $"Error converting {AllName[count]}\nCarrying rule does not match!");
                return;
            }
        }

        public static void HexExecute(string front)
        {
            if (!IsLogin)
            {
                ErrorMessage("請先登入!\nPlease login first!");
                return;
            }
            else
            {
                if (GroupsInfo.Count > 0 && PermissionInfo["owner"].Count > 0
                    && GroupsIndex > -1)
                {
                    front = $"0x{front}";
                    ServoValues[0] = GroupsInfo[GroupsIndex][1];
                    string HexText = HexExecuteArgs != string.Empty
                        ? $"{HexExecuteTitle} {front} {HexExecuteArgs}"
                        : $"{HexExecuteTitle} {front}";
                    ServoValues[1] = HexText;
                    ServoValues[2] = "0";
                    ServoValues[3] = PermissionInfo["owner"][UserFromIndex];
                    ReadWrite.WriteInstruction();
                    ServoValues = new string[4];
                }
                else
                {
                    ErrorMessage("群組列表或使用者為空!\n或未選擇!\n" +
                        "Group list or user is empty!\nOr not selected!");
                }
            }
        }

        public static void Execute_Click()
        {
            for (int i = 0; i < AllInputCarry.Length; i++)
            {
                if (AllInputCarry[i].Text != string.Empty)
                {
                    try
                    {
                        uint result = 0x0;
                        string[] AllOutput = new string[4];
                        StringToCarry(AllInputCarry[i].Text, AllCarry[i], ref result);
                        CarryConversion(result, ref AllOutput);
                        for (int x = 0; x < AllOutputCarry.Length; x++)
                        {
                            AllOutputCarry[x].Text = AllOutput[x];
                        }
                        HexExecute(AllOutput[3]);
                    }
                    catch
                    {
                        ErrorMessage($"轉換{AllName[i]}時錯誤\n進位規則不符!\n" +
                            $"Error converting {AllName[i]}\nCarrying rule does not match!");
                        return;
                    }
                }
            }
        }

        public static void SetExecute(string title,string args)
        {
            if (title == string.Empty || title == null)
            {
                ErrorMessage("程序錯誤,請回報給作者!\nProgram error, please report to the author");
                return;
            }
            HexExecuteTitle = title;
            HexExecuteArgs = args;
        }
    }
}
