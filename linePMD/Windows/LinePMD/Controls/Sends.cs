using System;
using System.Windows.Forms;
using LinePMD.Module;

namespace LinePMD.Controls
{
    public partial class Sends : UserControl
    {
        private string EXE
        {
            get
            {
                string ExeText = string.Empty;
                decimal count = counter.Value;
                ExeText += $"{count} {MessageText.Text}";
                return ExeText;
            }
            set
            {
                Material.SetExecute("send", value);
            }
        }

        public Sends()
        {
            InitializeComponent();
            Material.AllInputCarry[0] = Input_Bin;
            Material.AllInputCarry[1] = Input_Oct;
            Material.AllInputCarry[2] = Input_Dec;
            Material.AllInputCarry[3] = Input_Hex;
            Material.AllOutputCarry[0] = Output_Bin;
            Material.AllOutputCarry[1] = Output_Oct;
            Material.AllOutputCarry[2] = Output_Dec;
            Material.AllOutputCarry[3] = Output_Hex;
            Material.InterfaceInitial();
        }

        private void Execute_Click(object sender, EventArgs e)
        {
            if (MessageText.Text == string.Empty)
            {
                Material.ErrorMessage("請先輸入訊息!\nPlease enter a message first!");
                return;
            }
            EXE = EXE;
            Material.Execute_Click();
        }

        private void Reset_Click(object sender, EventArgs e)
        {
            for (int i = 0; i < Material.AllInputCarry.Length; i++)
            {
                Material.AllInputCarry[i].Text = string.Empty;
                Material.AllOutputCarry[i].Text = string.Empty;
            }
        }

        private void Input_Bin_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                if (MessageText.Text == string.Empty)
                {
                    Material.ErrorMessage("請先輸入訊息!\nPlease enter a message first!");
                    return;
                }
                EXE = EXE;
                Material.SingleConversion(0);
            }
        }

        private void Input_Oct_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                if (MessageText.Text == string.Empty)
                {
                    Material.ErrorMessage("請先輸入訊息!\nPlease enter a message first!");
                    return;
                }
                EXE = EXE;
                Material.SingleConversion(1);
            }
        }

        private void Input_Dec_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                if (MessageText.Text == string.Empty)
                {
                    Material.ErrorMessage("請先輸入訊息!\nPlease enter a message first!");
                    return;
                }
                EXE = EXE;
                Material.SingleConversion(2);
            }
        }

        private void Input_Hex_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                if (MessageText.Text == string.Empty)
                {
                    Material.ErrorMessage("請先輸入訊息!\nPlease enter a message first!");
                    return;
                }
                EXE = EXE;
                Material.SingleConversion(3);
            }
        }

        private void MessageText_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                if (!Material.IsLogin)
                {
                    Material.ErrorMessage("請先登入!\nPlease login first!");
                    return;
                }
                else
                {
                    if (Material.GroupsInfo.Count > 0 && Material.PermissionInfo["owner"].Count > 0
                        && Material.GroupsIndex > -1)
                    {
                        if (MessageText.Text == string.Empty)
                        {
                            Material.ErrorMessage("請先輸入訊息!\nPlease enter a message first!");
                            return;
                        }
                        decimal count = counter.Value;
                        Material.ServoValues[0] = Material.GroupsInfo[Material.GroupsIndex][1];
                        Material.ServoValues[1] = $"send -f {count} {MessageText.Text}";
                        Material.ServoValues[2] = "0";
                        Material.ServoValues[3] = Material.PermissionInfo["owner"][Material.UserFromIndex];
                        ReadWrite.WriteInstruction();
                        Material.ServoValues = new string[4];
                    }
                    else
                    {
                        Material.ErrorMessage("群組列表或使用者為空!\n或未選擇!\n" +
                            "Group list or user is empty!\nOr not selected!");
                    }
                }
            }
        }

        private void send0x1_Click(object sender, EventArgs e)
        {
            if (!Material.IsLogin)
            {
                Material.ErrorMessage("請先登入!\nPlease login first!");
                return;
            }
            else
            {
                if (Material.GroupsInfo.Count > 0 && Material.PermissionInfo["owner"].Count > 0
                    && Material.GroupsIndex > -1)
                {
                    if (MessageText.Text == string.Empty)
                    {
                        Material.ErrorMessage("請先輸入訊息!\nPlease enter a message first!");
                        return;
                    }
                    decimal count = counter.Value;
                    Material.ServoValues[0] = Material.GroupsInfo[Material.GroupsIndex][1];
                    Material.ServoValues[1] = $"send -f {count} {MessageText.Text}";
                    Material.ServoValues[2] = "0";
                    Material.ServoValues[3] = Material.PermissionInfo["owner"][Material.UserFromIndex];
                    ReadWrite.WriteInstruction();
                    Material.ServoValues = new string[4];
                }
                else
                {
                    Material.ErrorMessage("群組列表或使用者為空!\n或未選擇!\n" +
                        "Group list or user is empty!\nOr not selected!");
                }
            }
        }

        private void send0x2_Click(object sender, EventArgs e)
        {
            if (!Material.IsLogin)
            {
                Material.ErrorMessage("請先登入!\nPlease login first!");
                return;
            }
            else
            {
                if (Material.GroupsInfo.Count > 0 && Material.PermissionInfo["owner"].Count > 0
                    && Material.GroupsIndex > -1)
                {
                    if (MessageText.Text == string.Empty)
                    {
                        Material.ErrorMessage("請先輸入訊息!\nPlease enter a message first!");
                        return;
                    }
                    decimal count = counter.Value;
                    Material.ServoValues[0] = Material.GroupsInfo[Material.GroupsIndex][1];
                    Material.ServoValues[1] = $"send -t {count} {MessageText.Text}";
                    Material.ServoValues[2] = "0";
                    Material.ServoValues[3] = Material.PermissionInfo["owner"][Material.UserFromIndex];
                    ReadWrite.WriteInstruction();
                    Material.ServoValues = new string[4];
                }
                else
                {
                    Material.ErrorMessage("群組列表或使用者為空!\n或未選擇!\n" +
                        "Group list or user is empty!\nOr not selected!");
                }
            }
        }
    }
}
