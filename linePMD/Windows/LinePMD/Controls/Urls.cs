using System;
using System.Windows.Forms;
using LinePMD.Module;

namespace LinePMD.Controls
{
    public partial class Urls : UserControl
    {
        private string EXE
        {
            get
            {
                string ExeText = string.Empty;
                if (GidList.Items.Count > 0)
                {
                    for (int i = 0; i < GidList.Items.Count; i++)
                    {
                        ExeText += GidList.Items[i] + " ";
                    }
                }
                if (URLList.Items.Count > 0)
                {
                    for (int i = 0; i < URLList.Items.Count; i++)
                    {
                        ExeText += URLList.Items[i] + " ";
                    }
                }
                return ExeText;
            }
            set
            {
                Material.SetExecute("url", value);
            }
        }

        public Urls()
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

        private void URLText_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                var url = Regexs.FindUrl(URLText.Text);
                if (url.Item1)
                {
                    for (int i = 0;i < url.Item3.Count; i++)
                    {
                        URLList.Items.Add("https://line.me/R/ti/g/" + url.Item3[i]);
                    }
                    URLList.SelectedIndex = URLList.Items.Count - 1;
                }
                else
                {
                    Material.ErrorMessage("無效的URL!\nInvalid URL");
                }
            }
        }

        private void URLAppend_Click(object sender, EventArgs e)
        {
            var url = Regexs.FindUrl(URLText.Text);
            if (url.Item1)
            {
                for (int i = 0; i < url.Item3.Count; i++)
                {
                    URLList.Items.Add("https://line.me/R/ti/g/" + url.Item3[i]);
                }
                URLList.SelectedIndex = URLList.Items.Count - 1;
            }
            else
            {
                Material.ErrorMessage("無效的URL!\nInvalid URL");
            }
        }

        private void URLDelete_Click(object sender, EventArgs e)
        {
            if (URLList.SelectedIndex > -1)
            {
                URLList.Items.RemoveAt(URLList.SelectedIndex);
                URLList.SelectedIndex = URLList.Items.Count - 1;
            }
        }

        private void URLList_SelectedIndexChanged(object sender, EventArgs e)
        {
            ReadWrite.result.Add(URLList.SelectedItem.ToString());
        }

        private void url0x1_Click(object sender, EventArgs e)
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
                    if (URLList.Items.Count < 1)
                    {
                        Material.ErrorMessage("請先輸入URL列表\nPlease enter the URL list first");
                        return;
                    }
                    string urls = string.Empty;
                    for (int i = 0; i < URLList.Items.Count; i++)
                    {
                        urls += URLList.Items[i] + " ";
                    }
                    Material.ServoValues[0] = Material.GroupsInfo[Material.GroupsIndex][1];
                    Material.ServoValues[1] = $"url -f {urls}";
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

        private void url0x2_Click(object sender, EventArgs e)
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
                    if (URLList.Items.Count < 1)
                    {
                        Material.ErrorMessage("請先輸入URL列表\nPlease enter the URL list first");
                        return;
                    }
                    string urls = string.Empty;
                    for (int i = 0; i < URLList.Items.Count; i++)
                    {
                        urls += URLList.Items[i] + " ";
                    }
                    Material.ServoValues[0] = Material.GroupsInfo[Material.GroupsIndex][1];
                    Material.ServoValues[1] = $"url -j {urls}";
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

        private void url0x4_Click(object sender, EventArgs e)
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
                    string urls = string.Empty;
                    if (URLList.Items.Count < 1 && GidList.Items.Count < 1)
                    {
                        urls += Material.GroupsInfo[Material.GroupsIndex][1] + " ";
                    }
                    if (URLList.Items.Count > 0)
                    {
                        for (int i = 0; i < URLList.Items.Count; i++)
                        {
                            urls += URLList.Items[i] + " ";
                        }
                    }
                    if (GidList.Items.Count > 0)
                    {
                        for (int i = 0; i < GidList.Items.Count; i++)
                        {
                            urls += GidList.Items[i] + " ";
                        }
                    }
                    Material.ServoValues[0] = Material.GroupsInfo[Material.GroupsIndex][1];
                    Material.ServoValues[1] = $"url -on {urls}";
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

        private void url0x8_Click(object sender, EventArgs e)
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
                    string urls = string.Empty;
                    if (URLList.Items.Count < 1 && GidList.Items.Count < 1)
                    {
                        urls += Material.GroupsInfo[Material.GroupsIndex][1] + " ";
                    }
                    if (URLList.Items.Count > 0)
                    {
                        for (int i = 0; i < URLList.Items.Count; i++)
                        {
                            urls += URLList.Items[i] + " ";
                        }
                    }
                    if (GidList.Items.Count > 0)
                    {
                        for (int i = 0; i < GidList.Items.Count; i++)
                        {
                            urls += GidList.Items[i] + " ";
                        }
                    }
                    Material.ServoValues[0] = Material.GroupsInfo[Material.GroupsIndex][1];
                    Material.ServoValues[1] = $"url -off {urls}";
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
