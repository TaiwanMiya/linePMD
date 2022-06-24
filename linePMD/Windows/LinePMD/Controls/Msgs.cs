using System;
using System.Windows.Forms;
using LinePMD.Module;

namespace LinePMD.Controls
{
    public partial class Msgs : UserControl
    {
        private string EXE
        {
            get
            {
                decimal count = counter.Value;
                if (GidList.Items.Count < 1)
                {
                    return Convert.ToString(count);
                }
                else
                {
                    string ExeText = $"{count} ";
                    for (int i = 0; i < GidList.Items.Count; i++)
                    {
                        ExeText += GidList.Items[i] + " ";
                    }
                    return ExeText;
                }
            }
            set
            {
                Material.SetExecute("msg", value);
            }
        }

        public Msgs()
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

        private void GidText_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                var gid = Regexs.FindGid(GidText.Text);
                if (gid.Item1)
                {
                    for (int i = 0; i < gid.Item3.Count; i++)
                    {
                        GidList.Items.Add(gid.Item3[i]);
                    }
                    GidList.SelectedIndex = GidList.Items.Count - 1;
                }
                else
                {
                    Material.ErrorMessage("無效的GID!\nInvalid Gid");
                }
            }
        }

        private void GidAppend_Click(object sender, EventArgs e)
        {
            var gid = Regexs.FindGid(GidText.Text);
            if (gid.Item1)
            {
                for (int i = 0; i < gid.Item3.Count; i++)
                {
                    GidList.Items.Add(gid.Item3[i]);
                }
                GidList.SelectedIndex = GidList.Items.Count - 1;
            }
            else
            {
                Material.ErrorMessage("無效的GID!\nInvalid Gid");
            }
        }

        private void GidDelete_Click(object sender, EventArgs e)
        {
            if (GidList.SelectedIndex > -1)
            {
                GidList.Items.RemoveAt(GidList.SelectedIndex);
                GidList.SelectedIndex = GidList.Items.Count - 1;
            }
        }

        private void GidList_SelectedIndexChanged(object sender, EventArgs e)
        {
            ReadWrite.result.Add(GidList.SelectedItem.ToString());
        }

        private void msg0x1_Click(object sender, EventArgs e)
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
                    string gids = string.Empty;
                    decimal count = counter.Value;
                    if (GidList.Items.Count >= 1)
                    {
                        for (int i = 0; i < GidList.Items.Count; i++)
                        {
                            gids += GidList.Items[i] + " ";
                        }
                    }
                    else
                    {
                        gids += Material.GroupsInfo[Material.GroupsIndex][1] + " ";
                    }
                    Material.ServoValues[0] = Material.GroupsInfo[Material.GroupsIndex][1];
                    Material.ServoValues[1] = $"msg -u {count} {gids}";
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
