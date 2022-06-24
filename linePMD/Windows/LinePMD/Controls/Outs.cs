using System;
using System.Windows.Forms;
using LinePMD.Module;

namespace LinePMD.Controls
{
    public partial class Outs : UserControl
    {
        public Outs()
        {
            InitializeComponent();
        }

        private void out0x1_Click(object sender, EventArgs e)
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
                    Material.ServoValues[1] = $"out";
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
