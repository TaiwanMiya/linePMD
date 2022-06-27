using System;
using System.Collections.Generic;
using System.Linq;
using System.Drawing;
using System.Threading.Tasks;
using System.IO;
using System.Diagnostics;
using System.Windows.Forms;
using LinePMD.Controls;
using LinePMD.Module;

namespace LinePMD
{

    public partial class MainForm : Form
    {
        #region 建構子

        private Speed sp = new Speed();

        private Contacts contacts = new Contacts();

        private Chats chats = new Chats();

        private Sends sends = new Sends();

        private Threadings threads = new Threadings();

        private Friends friends = new Friends();

        private Msgs msgs = new Msgs();

        private Urls urls = new Urls();

        private Acts acts = new Acts();

        private Outs outs = new Outs();

        /// <summary>
        /// 終端置底
        /// </summary>
        public int TerminalToTheEnd
        {
            get
            {
                return Material.GetTerminal(terminal.Items.Count, terminal.Height, terminal.ItemHeight);
            }
            set
            {
                var TerminalSettings = Material.SetTerminal(value);
                terminal.Items.Add(TerminalSettings.Item1);
                terminal.TopIndex = TerminalSettings.Item2;
            }
        }

        #endregion

        #region 主程式進入點

        public MainForm()
        {
            InitializeComponent();
            InitialTerminal();
        }

        #endregion

        #region 初始化

        /// <summary>
        /// 載入介面流
        /// </summary>
        private void InitialTerminal()
        {
            Material.thispath = ReadWrite.CheakPathRoute();
            UsersRead();
            PermissionRead();
            InterfaceIninial();
            Material.InitialDone = true;
        }

        /// <summary>
        /// 初始化介面
        /// </summary>
        private void InterfaceIninial()
        {
            string[] terminalcolor = new string[]
            {
               "Black",
               "White",
               "Gray",
               "Red",
               "Orange",
               "Yellow",
               "Green",
               "Cyan",
               "Blue",
               "Purple"
            };
            string[] instructionestypes = new string[]
            {
                "sp/測速",
                "mid/用戶",
                "gid/群組",
                "send/發話",
                "thread/執行續",
                "friend/好友",
                "msg/訊息作動",
                "url/網址",
                "act/組作動",
                "out/退出"
            };
            TextBox[] textbox = new TextBox[]
            {
                pwdtext,
                tokentext,
                certtext
            };
            ComboBox[] combo = new ComboBox[]
            {
                TerminalFontColor,
                TerminalBackColor,
                permission,
                LoginComboBox,
                UsersComboBox,
                user_from
            };
            for (int i = 0; i < terminalcolor.Length; i++)
            {
                combo[1].Items.Add(terminalcolor[i]);
                combo[0].Items.Add(terminalcolor[i]);
            }
            for (int i = 0; i < Material.permissiontypes.Length; i++)
            {
                combo[2].Items.Add(Material.permissiontypes[i]);
            }
            for(int i = 0;i < Material.PermissionInfo["owner"].Count; i++)
            {
                combo[5].Items.Add(Material.PermissionInfo["owner"][i]);
            }
            for (int i = 0; i < instructionestypes.Length; i++)
            {
                InstructionType.Items.Add(instructionestypes[i]);
            }

            for (int i = 0; i < textbox.Length; i++)
            {
                textbox[i].PasswordChar = '*';
            }
            for (int i = 0; i < combo.Length; i++)
            {
                if (i == 0) combo[i].SelectedIndex = 1;
                else if(combo[i].Items.Count > 0) combo[i].SelectedIndex = 0;
            }
            Material.GroupsIndex = -1;
        }

        #endregion

        #region DOS

        /// <summary>
        /// 執行非同步處理 => DOS指令/程式碼
        /// </summary>
        /// <param name="method"></param>
        /// <param name="echo"></param>
        private void DosExecute(string method,bool echo=false)
        {
            Task.Run(() => DosRun(method, echo));
        }

        /// <summary>
        /// 執行DOS指令/程式碼
        /// </summary>
        /// <param name="method"></param>
        /// <param name="echo"></param>
        private void DosRun(string method, bool echo)
        {
            Process process = new Process();
            process.StartInfo.UseShellExecute = false;   // 是否使用外殼程式 
            process.StartInfo.CreateNoWindow = true;   //是否在新視窗中啟動該程序的值 
            process.StartInfo.RedirectStandardInput = true;  // 重定向輸入流 
            process.StartInfo.RedirectStandardOutput = true;  //重定向輸出流 
            process.StartInfo.RedirectStandardError = true;  //重定向錯誤流
            process.StartInfo.FileName = "cmd.exe";//待輸入的執行檔案路徑
            process.Start();
            process.StandardInput.AutoFlush = true;
            if (!echo)
            {
                process.StandardInput.WriteLine("echo off");
            }
            process.StandardInput.WriteLine(method); //輸入資訊到輸入流
            process.StandardInput.WriteLine("exit"); // 前面一個命令不管是否執行成功都執行後面(exit)命令，如果不執行exit命令，後面呼叫ReadToEnd()方法會假死
            StreamReader reader = process.StandardOutput;//獲取exe處理之後的輸出資訊
            string stringline = reader.ReadLine();
            ReadWrite.result = new List<string>();
            while (stringline != null)
            {
                ReadWrite.result.Add(stringline);
                stringline = reader.ReadLine();
            }
            process.WaitForExit();  //等待程式執行完退出程序
            process.Close(); //close程序
            reader.Close(); //close程序
        }

        /// <summary>
        /// 處理DOS回傳結果
        /// </summary>
        /// <param name="results">字節列表</param>
        private void CheakInstruction(List<string> results)
        {
            if (results[0].Trim() == "login")
            {
                Material.IsLogin = true;
            }
            else if (results[0].Trim() == "this new groups")
            {
                GroupsDealwith(results);
            }
            else if (results[0].Trim() == "success")
            {
                terminal.Items.Add(results[1].Trim());
            }
        }

        #endregion

        #region 讀寫權限

        /// <summary>
        /// 讀取所有權限
        /// </summary>
        private void PermissionRead()
        {
            Material.PermissionInfo.Clear();
            StreamReader reader = new StreamReader(Material.thispath + "\\Txt\\Permission.txt");
            string line = reader.ReadLine();
            List<string> staging = new List<string>();
            int settings = 0;
            while (line != null)
            {
                if (Material.permissiontypes[0].ToLower() == line.ToLower()) settings = 1;
                else if (Material.permissiontypes[1].ToLower() == line.ToLower())
                {
                    settings = 2;
                    Material.PermissionInfo.Add("admin", staging);
                    staging = new List<string>();
                }
                else if (Material.permissiontypes[2].ToLower() == line.ToLower())
                {
                    settings = 3;
                    Material.PermissionInfo.Add("owner", staging);
                    staging = new List<string>();
                }
                else if (settings == 1) staging.Add(line);
                else if (settings == 2) staging.Add(line);
                else if (settings == 3) staging.Add(line);
                line = reader.ReadLine();
            }
            Material.PermissionInfo.Add("backdoor", staging);
            reader.Close();
        }

        /// <summary>
        /// 寫入所有權限
        /// </summary>
        private void PermissionWrite()
        {
            StreamWriter writer = new StreamWriter(Material.thispath + "\\Txt\\Permission.txt");
            foreach (KeyValuePair<string, List<string>> info in Material.PermissionInfo)
            {
                writer.WriteLine(info.Key);
                for (int i = 0; i < info.Value.Count; i++)
                {
                    writer.WriteLine(info.Value[i]);
                }
            }
            writer.Close();
        }

        #endregion

        #region 讀寫登入存檔

        /// <summary>
        /// 讀取所有登入存檔
        /// </summary>
        private void UsersRead()
        {
            LoginComboBox.Items.Clear();
            UsersComboBox.Items.Clear();
            StreamReader reader = new StreamReader(Material.thispath + "\\Txt\\MyUsers.ini");
            string line = reader.ReadLine();
            int key = 0;
            string[] info = new string[5];
            bool IsEnd = false;
            while (line != null)
            {
                if (line.StartsWith("[") && line.EndsWith("]")){
                    key = Convert.ToInt32(line.Trim('[', ']'));
                    LoginComboBox.Items.Add(key);
                    UsersComboBox.Items.Add(key);
                }
                else if (line.StartsWith("mid = "))
                {
                    var mid = Regexs.FindMid(line);
                    if (mid.Item1)
                    {
                        info[0] = mid.Item2;
                    }
                    else
                    {
                        Material.ErrorMessage("文件中有無效的mid\nInvalid mid in file");
                        break;
                    }
                }
                else if (line.StartsWith("account = "))
                {
                    var account = Regexs.FindMail(line);
                    if (account.Item1)
                    {
                        info[1] = account.Item2;
                    }
                    else
                    {
                        if (Regexs.FindNone(line)) info[1] = "None";
                        else
                        {
                            Material.ErrorMessage("文件中有無效的mail\nInvalid mail in file");
                            break;
                        }
                    }
                }
                else if (line.StartsWith("password = "))
                {
                    var password = Regexs.FindPassword(line);
                    if (password.Item1)
                    {
                        info[2] = password.Item2;
                    }
                    else
                    {
                        if (Regexs.FindNone(line)) info[3] = "None";
                        else
                        {
                            Material.ErrorMessage("文件中有無效的password\nInvalid password in file");
                            break;
                        }
                    }
                }
                else if (line.StartsWith("token = "))
                {
                    var token = Regexs.FindToken(line);
                    if (token.Item1)
                    {
                        info[3] = token.Item2;
                    }
                    else
                    {
                        if (Regexs.FindNone(line)) info[3] = "None";
                        else
                        {
                            Material.ErrorMessage("文件中有無效的token\nInvalid token in file");
                            break;
                        }
                    }
                }
                else if (line.StartsWith("cert = "))
                {
                    var cert = Regexs.FindCert(line);
                    if (cert.Item1)
                    {
                        info[4] = cert.Item2;
                    }
                    else
                    {
                        if (Regexs.FindNone(line)) info[4] = "None";
                        else
                        {
                            Material.ErrorMessage("文件中有無效的cert\nInvalid cert in file");
                            break;
                        }
                    }
                    IsEnd = true;
                }
                if (IsEnd)
                {
                    try
                    {
                        Material.LoginInfo.Add(key, info.ToList());
                    }
                    catch (ArgumentException)
                    {
                        Material.LoginInfo[key] = info.ToList();
                    }
                    info = new string[5];
                    IsEnd = false;
                }
                line = reader.ReadLine();
            }
            reader.Close();
        }

        /// <summary>
        /// 寫入所有登入存檔
        /// </summary>
        private void UsersWrite()
        {
            StreamWriter writer = new StreamWriter(Material.thispath + "\\Txt\\MyUsers.ini");
            foreach(KeyValuePair<int,List<string>> info in Material.LoginInfo)
            {
                writer.WriteLine($"[{info.Key}]");
                string[] All = info.Value.ToArray();
                writer.WriteLine($"mid = {All[0]}");
                writer.WriteLine($"account = {All[1]}");
                writer.WriteLine($"password = {All[2]}");
                writer.WriteLine($"token = {All[3]}");
                writer.WriteLine($"cert = {All[4]}");
            }
            writer.Close();
        }

        #endregion

        #region 計時器

        /// <summary>
        /// 迴圈計時
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void timer1_Tick(object sender, EventArgs e)
        {
            if (ReadWrite.result.Count > 0)
            {
                for (int i = 0; i < ReadWrite.result.Count; i++)
                {
                    if (ReadWrite.result[i] != null) terminal.Items.Add(ReadWrite.result[i]);
                    else terminal.Items.Add(string.Empty);
                }
                ReadWrite.result = new List<string>();
                TerminalToTheEnd = TerminalToTheEnd;
            }
            var res = ReadWrite.ReadInstruction();
            if (res.Item1 && res.Item2 > -1)
            {
                if (res.Item2 == 0)
                {
                    CheakInstruction(res.Item3);
                }
                else if (res.Item2 == 1)
                {
                    res.Item3.RemoveAt(0);
                    foreach (string i in res.Item3)
                    {
                        terminal.Items.Add(i.Trim());
                    }
                    TerminalToTheEnd = TerminalToTheEnd;
                }
            }
        }

        #endregion

        #region 群組處理

        private void GroupsDealwith(List<string> results)
        {
            bool NewGroup = false;
            bool IsName = true;
            int NewGroupCount = 0;
            int CheakGroupCount = 0;
            List<string> names = new List<string>();
            List<string> gids = new List<string>();
            List<string> displayNames = new List<string>();
            List<string> mids = new List<string>();
            Material.GroupsInfo.Clear();
            Material.GroupMembersNameInfo.Clear();
            Material.GroupMembersInfo.Clear();
            Groups.Items.Clear();
            for (int i = 0; i < results.Count; i++)
            {
                if (results[i].Trim() == "this new groups")
                {
                    if (i > 0)
                    {
                        string[] InsertDict = new string[]
                        {
                            names[NewGroupCount],
                            gids[NewGroupCount]
                        };
                        Material.GroupsInfo.Add(NewGroupCount, InsertDict);
                        Material.GroupMembersNameInfo.Add(NewGroupCount, displayNames.ToArray());
                        Material.GroupMembersInfo.Add(NewGroupCount, mids.ToArray());
                        Groups.Items.Add(Material.GroupsInfo[NewGroupCount][0]);
                        NewGroupCount++;
                        CheakGroupCount = 0;
                        displayNames.Clear();
                        mids.Clear();
                    }
                    NewGroup = true;
                }
                else if (NewGroup)
                {
                    if (CheakGroupCount == 0)
                    {
                        names.Add(results[i].Trim());
                        CheakGroupCount++;
                    }
                    else if (CheakGroupCount == 1)
                    {
                        gids.Add(results[i].Trim());
                        CheakGroupCount++;
                    }
                    else if (CheakGroupCount > 1 && IsName)
                    {
                        displayNames.Add(results[i].Trim());
                        IsName = false;
                    }
                    else if (CheakGroupCount > 1 && !IsName)
                    {
                        mids.Add(results[i].Trim());
                        IsName = true;
                    }
                }
            }
            string[] InsertDictFinally = new string[]
            {
                names[NewGroupCount],
                gids[NewGroupCount]
            };
            Material.GroupsInfo.Add(NewGroupCount, InsertDictFinally);
            Material.GroupMembersNameInfo.Add(NewGroupCount, displayNames.ToArray());
            Material.GroupMembersInfo.Add(NewGroupCount, mids.ToArray());
            Groups.Items.Add(Material.GroupsInfo[NewGroupCount][0]);
            NewGroupCount++;
            CheakGroupCount = 0;
            displayNames.Clear();
            mids.Clear();
        }

        #endregion

        #region Windows介面

        /// <summary>
        /// 單個DOS指令執行(鍵入式)
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void customize_Click(object sender, EventArgs e)
        {
            DosExecute(CmdExecute.Text);
        }

        /// <summary>
        /// 單個DOS指令執行(點擊式)
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void CmdExecute_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter) DosExecute(CmdExecute.Text);
        }

        /// <summary>
        /// 多個DOS指令執行
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void customizes_Click(object sender, EventArgs e)
        {
            string ListExec = string.Empty;
            foreach (string item in CmdExecuteArray.Items) ListExec += item + "\n";
            DosExecute(ListExec);
        }

        /// <summary>
        /// 新增下一個DOS指令(鍵入式)
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void CmdExecutes_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                CmdExecuteArray.Items.Add(CmdExecutes.Text);
                CmdExecuteArray.SelectedIndex = CmdExecuteArray.Items.Count - 1;
            }
        }

        /// <summary>
        /// 新增下一個DOS指令(點擊式)
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void AppendExecute_Click(object sender, EventArgs e)
        {
            CmdExecuteArray.Items.Add(CmdExecutes.Text);
            CmdExecuteArray.SelectedIndex = CmdExecuteArray.Items.Count - 1;
        }

        /// <summary>
        /// 刪除列表上DOS指令
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void RemoveExecute_Click(object sender, EventArgs e)
        {
            if (CmdExecuteArray.Items.Count > 0)
            {
                CmdExecuteArray.Items.Remove(CmdExecuteArray.Items[CmdExecuteArray.SelectedIndex]);
                CmdExecuteArray.SelectedIndex = CmdExecuteArray.Items.Count - 1;
            }
        }

        /// <summary>
        /// 安裝必備所需程序
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void mustpip_Click(object sender, EventArgs e)
        {
            if (MessageBox.Show("要開始執行必備安裝程序?", "安裝", MessageBoxButtons.YesNo, MessageBoxIcon.Question) == DialogResult.Yes)
            {
                bool CheakPythonInstallIsSuccess = false;
                if (MessageBox.Show("需要安裝python嗎?\nVersion:3.8.10",
                    "python安裝", MessageBoxButtons.YesNo, MessageBoxIcon.Question) == DialogResult.Yes)
                {
                    string PyInstall = $"cd {Material.thispath}\\loading\npython-3.8.10-amd64.exe";
                    DosExecute(PyInstall);
                    CheakPythonInstallIsSuccess = true;
                }
                while (CheakPythonInstallIsSuccess)
                {
                    if (MessageBox.Show("是否已安裝完畢Python?","安裝確認",
                        MessageBoxButtons.YesNo,MessageBoxIcon.Question) == DialogResult.Yes)
                    {
                        CheakPythonInstallIsSuccess = false;
                    }
                };
                MessageBox.Show("將進行驅動程序安裝", "驅動安裝", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                DosExecute($"cd {Material.thispath}\\loading\nmsodbcsql.msi");
                MessageBox.Show("將進行Python包安裝", "python庫安裝");
                string package = "pip install requests\n" +
                    "pip install numpy\n" +
                    "pip install cloudscraper\n" +
                    "pip install pyodbc\n" +
                    "pip install six\n";
                DosExecute(package);
            }
        }

        /// <summary>
        /// 終端背景顏色更改
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void TerminalBackColor_SelectedIndexChanged(object sender, EventArgs e)
        {
            terminal.BackColor = Material.TerminalColor[TerminalBackColor.SelectedIndex];
        }

        /// <summary>
        /// 終端字體顏色更改
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void TerminalFontColor_SelectedIndexChanged(object sender, EventArgs e)
        {
            terminal.ForeColor = Material.TerminalColor[TerminalFontColor.SelectedIndex];
        }

        /// <summary>
        /// 終端文字清除
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void TerminalClear_Click(object sender, EventArgs e)
        {
            terminal.Items.Clear();
        }

        /// <summary>
        /// 關閉介面
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void MainForm_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (MessageBox.Show("確定關閉LinePMD?","關閉程序",MessageBoxButtons.YesNo,MessageBoxIcon.Question) == DialogResult.Yes)
                e.Cancel = false;
            else e.Cancel = true;
        }

        /// <summary>
        /// 新增權限
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void permissionAppend_Click(object sender, EventArgs e)
        {
            string Args = permissionInput.Text;
            var mid = Regexs.FindMid(Args);
            var gid = Regexs.FindGid(Args);
            if (mid.Item1)
            {
                if (permission.SelectedIndex == 0)
                {
                    Material.PermissionInfo["admin"].Add(mid.Item2);
                    Material.PermissionInfo["admin"] = Material.PermissionInfo["admin"].Distinct().ToList();
                }
                else if (permission.SelectedIndex == 1)
                {
                    Material.PermissionInfo["owner"].Add(mid.Item2);
                    Material.PermissionInfo["owner"] = Material.PermissionInfo["owner"].Distinct().ToList();
                }
                else
                {
                    Material.ErrorMessage("只能選擇\n1.Admin\n2.Owner\n\ncan only choose\n1.Admin\n2.Owner");
                }
            }
            else if (gid.Item1)
            {
                if (permission.SelectedIndex == 2) Material.PermissionInfo["backdoor"][0] = gid.Item2;
                else
                {
                    Material.ErrorMessage("只能選擇\n3.BackDoor\ncan only choose\n3.BackDoor");
                }
            }
            else
            {
                Material.ErrorMessage($"以下格式錯誤\n{Args}\nThe following format is incorrect{Args}");
            }
            PermissionWrite();
            if (Material.IsLogin)
            {
                ReadWrite.WritePermission();
            }
        }

        /// <summary>
        /// 刪除權限
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void permissionRemove_Click(object sender, EventArgs e)
        {
            string Args = permissionInput.Text;
            if (Args == string.Empty)
            {
                Material.ErrorMessage("輸入值為空白!\nInput value is blank");
                return;
            }
            var mid = Regexs.FindMid(Args);
            var gid = Regexs.FindGid(Args);
            bool notin = true;
            if (mid.Item1)
            {
                if (permission.SelectedIndex == 0)
                {
                    for (int i = 0;i < Material.PermissionInfo["admin"].Count; i++)
                    {
                        if (mid.Item2.ToLower() == Material.PermissionInfo["admin"][i].ToLower())
                        {
                            Material.PermissionInfo["admin"].RemoveAt(i);
                            notin = false;
                        }
                    }
                    if (notin)
                    {
                        Material.ErrorMessage($"用戶{Args}不在admin內\nuser {Args} not in admin");
                        return;
                    }
                }
                else if (permission.SelectedIndex == 1)
                {
                    for (int i = 0; i < Material.PermissionInfo["owner"].Count; i++)
                    {
                        if (mid.Item2.ToLower() == Material.PermissionInfo["owner"][i].ToLower())
                        {
                            Material.PermissionInfo["owner"].RemoveAt(i);
                            notin = false;
                        }
                    }
                    if (notin)
                    {
                        Material.ErrorMessage($"用戶{Args}不在owner內\nuser {Args} not in owner");
                        return;
                    }
                }
                else
                {
                    Material.ErrorMessage("只能選擇\n1.Admin\n2.Owner\n\ncan only choose\n1.Admin\n2.Owner");
                    return;
                }
            }
            else if (gid.Item1)
            {
                Material.ErrorMessage("不能移除後台\n只能修改!" +
                    "\nThe background cannot be removed\nCan only be modified!");
                return;
            }
            else
            {
                Material.ErrorMessage($"以下格式錯誤\n{Args}" +
                    $"\nThe following format is incorrect\n{Args}");
                return;
            }
            PermissionWrite();
            if (Material.IsLogin)
            {
                ReadWrite.WritePermission();
            }
        }

        /// <summary>
        /// 新增登入存檔
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void UsersAppend_Click(object sender, EventArgs e)
        {
            string msgshow = string.Empty;
            string[] Indexs = new string[5];
            if (midtext.Text != string.Empty)
            {
                var mid = Regexs.FindMid(midtext.Text);
                if (mid.Item1) Indexs[0] = mid.Item2;
                else if (!mid.Item1) msgshow += "Mid格式錯誤!\nMid format error\n";
            }
            else msgshow += "使用者mid必須填入!\n";
            if (mailtext.Text != string.Empty)
            {
                var mail = Regexs.FindMail(mailtext.Text);
                if (mail.Item1) Indexs[1] = mail.Item2;
                else if (!mail.Item1) msgshow += "Mail格式錯誤!\nMial format error\n";
            }
            else Indexs[1] = "None";
            if (tokentext.Text != string.Empty)
            {
                var token = Regexs.FindToken(tokentext.Text);
                if (token.Item1) Indexs[3] = token.Item2;
                else if (!token.Item1) msgshow += "Token格式錯誤!\nToken format error\n";
                
            }
            else Indexs[3] = "None";
            if (certtext.Text != string.Empty)
            {
                var cert = Regexs.FindCert(certtext.Text);
                if (cert.Item1) Indexs[4] = cert.Item2;
                else if (!cert.Item1) msgshow += "Cert格式錯誤!\nCert format error\n";
            }
            else Indexs[4] = "None";
            if (pwdtext.Text != string.Empty) Indexs[2] = pwdtext.Text;
            else Indexs[2] = "None";
            if (msgshow != string.Empty)
            {
                Material.ErrorMessage(msgshow);
                return;
            }
            Material.LoginInfo.Add(Material.LoginInfo.Count, Indexs.ToList());
            UsersWrite();
            UsersRead();
        }

        /// <summary>
        /// 刪除登入存檔
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void UsersRemove_Click(object sender, EventArgs e)
        {
            int lastdel = -1;
            foreach (KeyValuePair<int, List<string>> info in Material.LoginInfo)
            {
                if (info.Key == UsersComboBox.SelectedIndex)
                {
                    lastdel = info.Key;
                }
            }
            
            if (MessageBox.Show($"確定要刪除\n{Material.LoginInfo[lastdel][0]}",
                "刪除?", MessageBoxButtons.YesNo, MessageBoxIcon.Warning) == DialogResult.No)
            {
                return;
            }
            if (lastdel > -1)
            {
                Material.LoginInfo.Remove(lastdel);
            }
            else
            {
                Material.ErrorMessage("無效的選項!\ninvalid option");
                return;
            }
            if (!Material.LoginInfo.ContainsKey(lastdel))
            {
                for (int i = lastdel; i < Material.LoginInfo.Keys.Count; i++)
                {
                    if (Material.LoginInfo.Keys.Count -1 == i)
                    {
                        Material.LoginInfo.Remove(i);
                        break;
                    }
                    else
                    {
                        Material.LoginInfo[i] = Material.LoginInfo[i+1];
                    }
                }
            }
            UsersWrite();
            UsersRead();
        }

        /// <summary>
        /// 複製終端文字
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void terminal_DoubleClick(object sender, EventArgs e)
        {
            try
            {
                if (terminal.SelectedIndex > -1)
                    Clipboard.SetText(terminal.Items[terminal.SelectedIndex].ToString());
            }
            catch (ArgumentNullException)
            {
                Material.ErrorMessage("複製的值為空!\nThe copied value is empty!");
            }
        }

        /// <summary>
        /// 登入帳戶
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void login_Click(object sender, EventArgs e)
        {
            if (!Material.IsLogin)
            {
                bool trying = false;
                foreach(KeyValuePair<int, List<string>> info in Material.LoginInfo)
                {
                    if (info.Key == Convert.ToInt32(LoginComboBox.SelectedItem))
                    {
                        DosExecute($"cd {Material.thispath}\npy -u main.py {info.Key} servo");
                        trying = true;
                    }
                }
                if (!trying)
                    Material.ErrorMessage("登入失敗\nLogin failed");
            }
            else
            {
                Material.ErrorMessage("登入狀態中,請勿再次登入!\nYou are logged in, please do not log in again!");
            }
        }

        /// <summary>
        /// 登出帳戶
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void logout_Click(object sender, EventArgs e)
        {
            if (Material.IsLogin)
            {
                int pid = ReadWrite.PID;
                DosExecute($"taskkill /f /pid {pid}");
                Material.IsLogin = false;
                Material.GroupsInfo.Clear();
                Material.GroupMembersInfo.Clear();
                Material.GroupMembersNameInfo.Clear();
                Groups.Items.Clear();
                GroupMembers.Items.Clear();
                Material.GroupsIndex = -1;
                Material.MembersIndex = -1;
            }
            else
            {
                Material.ErrorMessage("尚未登入,故無法登出!\nNot logged in, so can't log out!");
            }
        }

        /// <summary>
        /// 緊急重置
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void ResetError_Click(object sender, EventArgs e)
        {
            if (MessageBox.Show("確定要緊急重置嗎?\n若無嚴重錯誤請勿隨意重置\n否則有機會無法使用!\n" +
                "Are you sure you want an emergency reset?\n" +
                "If there is no serious error, please do not reset at will\n" +
                "Otherwise, there is a chance that it cannot be used!",
                "緊急重置",MessageBoxButtons.YesNo,MessageBoxIcon.Warning) == DialogResult.Yes)
            {
                string[] AllFile = new string[]
                {
                    Material.thispath + "\\Txt\\IsLogin.txt",
                    Material.thispath + "\\Txt\\ServoPid.txt",
                    Material.thispath + "\\Txt\\ServoArgs.txt",
                    Material.thispath + "\\Txt\\ServoResult.txt"
                };
                for (int i = 0; i < AllFile.Length; i++)
                {
                    try
                    {
                        File.Delete(AllFile[i]);
                    }
                    catch (DirectoryNotFoundException)
                    {
                        Material.ErrorMessage("路徑已被刪除或移動\n檔案無法使用!\n" +
                            "The path has been deleted or moved\nThe file cannot be used!");
                    }
                    catch (UnauthorizedAccessException)
                    {
                        Material.ErrorMessage("系統權限不足\n建議使用管理員身分執行!\n" +
                            "Insufficient system privileges\nIt is recommended to execute as an administrator!");
                    }
                    catch (FileNotFoundException) { }
                    catch (IOException) { }
                }
                DosExecute("taskkill /f /im py.exe");
                Material.IsLogin = false;
                Material.HexExecuteTitle = string.Empty;
                Material.HexExecuteArgs = string.Empty;
                Material.AllInputCarry = new TextBox[4];
                Material.AllOutputCarry = new TextBox[4];
                Material.GroupsInfo.Clear();
                Material.GroupMembersNameInfo.Clear();
                Material.GroupMembersInfo.Clear();
                Material.ServoValues = new string[4];
                Groups.Items.Clear();
                GroupMembers.Items.Clear();
                InstructionPanel.Controls.Clear();
                terminal.Items.Clear();
            }
        }

        /// <summary>
        /// 登入帳戶切換
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void LoginComboBox_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (Material.InitialDone)
            {
                foreach (KeyValuePair<int, List<string>> info in Material.LoginInfo)
                {
                    if (info.Key == LoginComboBox.SelectedIndex)
                    {
                        terminal.Items.Add(info.Key);
                        for (int i = 0; i < info.Value.Count; i++)
                        {
                            terminal.Items.Add(Material.LoginTitle[i]);
                            terminal.Items.Add(info.Value[i]);
                        }
                    }
                }
                TerminalToTheEnd = TerminalToTheEnd;
            }
        }

        /// <summary>
        /// 登入管理帳戶切換
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void UsersComboBox_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (Material.InitialDone)
            {
                foreach (KeyValuePair<int, List<string>> info in Material.LoginInfo)
                {
                    if (info.Key == UsersComboBox.SelectedIndex)
                    {
                        terminal.Items.Add(info.Key);
                        for (int i = 0; i < info.Value.Count; i++)
                        {
                            terminal.Items.Add(Material.LoginTitle[i]);
                            terminal.Items.Add(info.Value[i]);
                        }
                    }
                }
                TerminalToTheEnd = TerminalToTheEnd;
            }
        }

        /// <summary>
        /// 權限管理切換
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void permission_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (Material.InitialDone)
            {
                StreamReader reader = new StreamReader(Material.thispath + "\\Txt\\Permission.txt");
                string line = reader.ReadLine();
                bool IsSelect = false;
                while (line != null)
                {
                    var mid = Regexs.FindMid(line);
                    var gid = Regexs.FindGid(line);
                    if (!mid.Item1 && !gid.Item1 && !IsSelect && line.ToLower() == permission.SelectedItem.ToString().ToLower())
                    {
                        terminal.Items.Add(line);
                        IsSelect = true;
                    }
                    else if (IsSelect && mid.Item1) terminal.Items.Add(line);
                    else if (IsSelect && gid.Item1) terminal.Items.Add(line);
                    else if (IsSelect && !mid.Item1 && !gid.Item1)
                    {
                        IsSelect = false;
                    }
                    line = reader.ReadLine();
                }
                TerminalToTheEnd = TerminalToTheEnd;
                reader.Close();
            }
        }

        /// <summary>
        /// 設置輸入遮蔽
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void showpwd_CheckedChanged(object sender, EventArgs e)
        {
            if (showpwd.Checked)
            {
                pwdtext.PasswordChar = '*';
                tokentext.PasswordChar = '*';
                certtext.PasswordChar = '*';
            }
            else if (!showpwd.Checked)
            {
                pwdtext.PasswordChar = '\0';
                tokentext.PasswordChar = '\0';
                certtext.PasswordChar = '\0';
            }
        }

        #endregion

        #region 指令介面

        /// <summary>
        /// 切換使用者
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void user_from_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (Material.InitialDone)
            {
                Material.UserFromIndex = user_from.SelectedIndex;
                terminal.Items.Add("使用者以切換為 :");
                terminal.Items.Add(user_from.SelectedItem);
                TerminalToTheEnd = TerminalToTheEnd;
            }
        }

        private void InstructionType_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (Material.InitialDone)
            {
                InstructionPanel.Controls.Clear();
                switch (InstructionType.SelectedIndex)
                {
                    case 0:
                        sp.Name = "SpeedPanel";
                        sp.Parent = InstructionPanel;
                        sp.Location = new Point() { X = 0, Y = 0 };
                        break;
                    case 1:
                        contacts.Name = "ContactsPanel";
                        contacts.Parent = InstructionPanel;
                        contacts.Location = new Point() { X = 0, Y = 0 };
                        break;
                    case 2:
                        chats.Name = "ChatsPanel";
                        chats.Parent = InstructionPanel;
                        chats.Location = new Point() { X = 0, Y = 0 };
                        break;
                    case 3:
                        sends.Name = "SendsPanel";
                        sends.Parent = InstructionPanel;
                        sends.Location = new Point() { X = 0, Y = 0 };
                        break;
                    case 4:
                        threads.Name = "ThreadingsPanel";
                        threads.Parent = InstructionPanel;
                        threads.Location = new Point() { X = 0, Y = 0 };
                        break;
                    case 5:
                        friends.Name = "FriendsPanel";
                        friends.Parent = InstructionPanel;
                        friends.Location = new Point() { X = 0, Y = 0 };
                        break;
                    case 6:
                        msgs.Name = "MsgsPanel";
                        msgs.Parent = InstructionPanel;
                        msgs.Location = new Point() { X = 0, Y = 0 };
                        break;
                    case 7:
                        urls.Name = "UrlsPanel";
                        urls.Parent = InstructionPanel;
                        urls.Location = new Point() { X = 0, Y = 0 };
                        break;
                    case 8:
                        acts.Name = "ActsPanel";
                        acts.Parent = InstructionPanel;
                        acts.Location = new Point() { X = 0, Y = 0 };
                        break;
                    case 9:
                        outs.Name = "OutsPanel";
                        outs.Parent = InstructionPanel;
                        outs.Location = new Point() { X = 0, Y = 0 };
                        break;
                    default:
                        break;
                }
            }
        }

        private void Groups_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (Material.InitialDone)
            {
                Material.GroupsIndex = Groups.SelectedIndex;
                terminal.Items.Add("<<<群組名稱>>>");
                terminal.Items.Add(Material.GroupsInfo[Groups.SelectedIndex][0]);
                terminal.Items.Add("<<<群組GID>>>");
                terminal.Items.Add(Material.GroupsInfo[Groups.SelectedIndex][1]);
                TerminalToTheEnd = TerminalToTheEnd;
                GroupMembers.Items.Clear();
                for (int i = 0; i < Material.GroupMembersNameInfo[Groups.SelectedIndex].Length; i++)
                {
                    GroupMembers.Items.Add(Material.GroupMembersNameInfo[Groups.SelectedIndex][i]);
                }
            }
        }

        private void GroupMembers_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (Groups.SelectedIndex > -1)
            {
                Material.MembersIndex = GroupMembers.SelectedIndex;
                terminal.Items.Add("<<<用戶名稱>>>");
                terminal.Items.Add(Material.GroupMembersNameInfo[Groups.SelectedIndex][GroupMembers.SelectedIndex]);
                terminal.Items.Add("<<<用戶MID>>>");
                terminal.Items.Add(Material.GroupMembersInfo[Groups.SelectedIndex][GroupMembers.SelectedIndex]);
                TerminalToTheEnd = TerminalToTheEnd;
            }
        }

        #endregion
    }
}
