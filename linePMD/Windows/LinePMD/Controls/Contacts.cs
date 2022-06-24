using System;
using System.Windows.Forms;
using LinePMD.Module;

namespace LinePMD.Controls
{
    public partial class Contacts : UserControl
    {
        private string EXE
        {
            get
            {
                if (MidList.Items.Count < 1)
                {
                    return string.Empty;
                }
                else
                {
                    string ExeText = string.Empty;
                    for (int i = 0; i < MidList.Items.Count; i++)
                    {
                        ExeText += MidList.Items[i] + " ";
                    }
                    return ExeText;
                }
            }
            set
            {
                Material.SetExecute("mid", value);
            }
        }

        public Contacts()
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
                EXE = EXE;
                Material.SingleConversion(0);
            }
        }

        private void Input_Oct_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                EXE = EXE;
                Material.SingleConversion(1);
            }
        }

        private void Input_Dec_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                EXE = EXE;
                Material.SingleConversion(2);
            }
        }

        private void Input_Hex_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                EXE = EXE;
                Material.SingleConversion(3);
            }
        }

        private void MidText_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                var mid = Regexs.FindMid(MidText.Text);
                if (mid.Item1)
                {
                    for (int i = 0; i < mid.Item3.Count; i++)
                    {
                        MidList.Items.Add(mid.Item3[i]);
                    }
                    MidList.SelectedIndex = MidList.Items.Count - 1;
                }
                else
                {
                    Material.ErrorMessage("無效的MID!\nInvalid Mid");
                }
            }
        }

        private void MidAppend_Click(object sender, EventArgs e)
        {
            var mid = Regexs.FindMid(MidText.Text);
            if (mid.Item1)
            {
                for (int i = 0; i < mid.Item3.Count; i++)
                {
                    MidList.Items.Add(mid.Item3[i]);
                }
                MidList.SelectedIndex = MidList.Items.Count - 1;
            }
            else
            {
                Material.ErrorMessage("無效的MID!\nInvalid Mid");
            }
        }

        private void MidDelete_Click(object sender, EventArgs e)
        {
            if (MidList.SelectedIndex > -1)
            {
                MidList.Items.RemoveAt(MidList.SelectedIndex);
                MidList.SelectedIndex = MidList.Items.Count - 1;
            }
        }

        private void MidList_SelectedIndexChanged(object sender, EventArgs e)
        {
            ReadWrite.result.Add(MidList.SelectedItem.ToString());
        }

        private void mid0x1_Click(object sender, EventArgs e)
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
                    if (MidList.Items.Count < 1)
                    {
                        Material.ErrorMessage("請先輸入mid列表\nPlease enter the mid list first");
                        return;
                    }
                    string mids = string.Empty;
                    for (int i = 0;i < MidList.Items.Count; i++)
                    {
                        mids += MidList.Items[i] + " ";
                    }
                    Material.ServoValues[0] = Material.GroupsInfo[Material.GroupsIndex][1];
                    Material.ServoValues[1] = $"mid {mids}";
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

        private void mid0x2_Click(object sender, EventArgs e)
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
                    if (MidList.Items.Count < 1)
                    {
                        Material.ErrorMessage("請先輸入mid列表\nPlease enter the mid list first");
                        return;
                    }
                    string mids = string.Empty;
                    for (int i = 0; i < MidList.Items.Count; i++)
                    {
                        mids += MidList.Items[i] + " ";
                    }
                    Material.ServoValues[0] = Material.GroupsInfo[Material.GroupsIndex][1];
                    Material.ServoValues[1] = $"mid -c {mids}";
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

        private void mid0x4_Click(object sender, EventArgs e)
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
                    if (MidList.Items.Count < 1)
                    {
                        Material.ErrorMessage("請先輸入mid列表Please enter the mid list first");
                        return;
                    }
                    string mids = string.Empty;
                    for (int i = 0; i < MidList.Items.Count; i++)
                    {
                        mids += MidList.Items[i] + " ";
                    }
                    Material.ServoValues[0] = Material.GroupsInfo[Material.GroupsIndex][1];
                    Material.ServoValues[1] = $"mid -p {mids}";
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

        private void mid0x8_Click(object sender, EventArgs e)
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
                    Material.ServoValues[0] = Material.GroupsInfo[Material.GroupsIndex][1];
                    Material.ServoValues[1] = $"mid -m";
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
