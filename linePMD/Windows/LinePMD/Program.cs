using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace LinePMD
{
    internal static class Program
    {
        /// <summary>
        /// 應用程式的主要進入點。
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            if (IsOpen())
            {
                MessageBox.Show("應用程式已開啟!\n請勿重複開啟程序!","已開啟的應用",MessageBoxButtons.OK,MessageBoxIcon.Error);
                Environment.Exit(0);
            }
            FirstInitial();
            Application.Run(new MainForm());
        }

        static bool IsOpen()
        {
            if(Process.GetProcessesByName(Process.GetCurrentProcess().ProcessName).Length > 1)
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        static void FirstInitial()
        {
            string msgshow =  
              "使用事項"
            + "\n1.若首次開啟,請先安裝必備集合,否則機器無法生效!"
            + "\n2.登入前請先確保admin,owner與backdoor的設定"
            + "\n3.登入前請先設定你的mid(建議輸入owner用戶的mid)"
            + "\n4.單一命令與多道命令使用Windows Dos系統(cmd,bat)執行"
            + "\n5.雙擊介面終端機可以複製文字,便於管理"
            + "\n6.若指令沒反應,再多按多試幾次"
            + "\n7.若尚未登入卻登入失敗,請使用緊急停止"
            + "\n8.若看不懂使用可以詢問開發者,ID在下方附上"
            + "\n9.若視窗出現卡頓或者line bot完全沒有反應,請立即關閉視窗程序"
            + "\n\n若有相關問題諮詢或錯誤回報請洽Line id"
            + "\n彼雅(不常上線) : pea.rose_love"
            + "\n狄刻 : s1229abcdb2";
            msgshow +=
                "\n----------------------------------------------------------------------------" +
                "\nUse matters" +
                "\n1. If you open it for the first time, please install the necessary set first, otherwise the machine will not take effect!" +
                "\n2. Please ensure admin, owner and backdoor settings before logging in" +
                "\n3. Please set your mid before logging in (it is recommended to enter the mid of the owner user)" +
                "\n4. Use Windows Dos system (cmd, bat) to execute single command and multi-channel command" +
                "\n5. Double-click the interface terminal to copy text for easy management" +
                "\n6. If the command does not respond, press and try again" +
                "\n7. If you have not logged in but failed to log in, please use emergency stop" +
                "\n8. If you don't understand how to use it, you can ask the developer, the ID is attached below" +
                "\n9. If the window freezes or the line bot does not respond at all, please close the window program immediately" +
                "\n\nIf you have any questions or errors, please contact Line id" +
                "\nPea (not often online) : pea.rose_love" +
                "\nDick : s1229abcdb2";
            MessageBox.Show(msgshow, "使用說明", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }
    }
}
