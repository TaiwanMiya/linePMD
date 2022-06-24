namespace LinePMD
{
    partial class MainForm
    {
        /// <summary>
        /// 設計工具所需的變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清除任何使用中的資源。
        /// </summary>
        /// <param name="disposing">如果應該處置受控資源則為 true，否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 設計工具產生的程式碼

        /// <summary>
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改
        /// 這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
            this.terminal = new System.Windows.Forms.ListBox();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.tabControl1 = new System.Windows.Forms.TabControl();
            this.tabPage1 = new System.Windows.Forms.TabPage();
            this.groupBox5 = new System.Windows.Forms.GroupBox();
            this.groupBox7 = new System.Windows.Forms.GroupBox();
            this.showpwd = new System.Windows.Forms.CheckBox();
            this.label7 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.UsersComboBox = new System.Windows.Forms.ComboBox();
            this.UsersRemove = new System.Windows.Forms.Button();
            this.UsersAppend = new System.Windows.Forms.Button();
            this.certtext = new System.Windows.Forms.TextBox();
            this.tokentext = new System.Windows.Forms.TextBox();
            this.pwdtext = new System.Windows.Forms.TextBox();
            this.mailtext = new System.Windows.Forms.TextBox();
            this.midtext = new System.Windows.Forms.TextBox();
            this.groupBox6 = new System.Windows.Forms.GroupBox();
            this.permissionRemove = new System.Windows.Forms.Button();
            this.permissionAppend = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.permissionInput = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.permission = new System.Windows.Forms.ComboBox();
            this.groupBox4 = new System.Windows.Forms.GroupBox();
            this.ResetError = new System.Windows.Forms.Button();
            this.LoginComboBox = new System.Windows.Forms.ComboBox();
            this.logout = new System.Windows.Forms.Button();
            this.login = new System.Windows.Forms.Button();
            this.TerminalAdmin = new System.Windows.Forms.GroupBox();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.CmdExecutes = new System.Windows.Forms.TextBox();
            this.customizes = new System.Windows.Forms.Button();
            this.CmdExecuteArray = new System.Windows.Forms.ComboBox();
            this.AppendExecute = new System.Windows.Forms.Button();
            this.RemoveExecute = new System.Windows.Forms.Button();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.CmdExecute = new System.Windows.Forms.TextBox();
            this.customize = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.TerminalClear = new System.Windows.Forms.Button();
            this.TerminalFontColor = new System.Windows.Forms.ComboBox();
            this.TerminalBackColor = new System.Windows.Forms.ComboBox();
            this.TerminalFontcolor_Label = new System.Windows.Forms.Label();
            this.TerminalBackcolor_Label = new System.Windows.Forms.Label();
            this.InstallerGroup = new System.Windows.Forms.GroupBox();
            this.mustpip = new System.Windows.Forms.Button();
            this.tabPage2 = new System.Windows.Forms.TabPage();
            this.groupBox8 = new System.Windows.Forms.GroupBox();
            this.GroupMembers = new System.Windows.Forms.ComboBox();
            this.groupBox11 = new System.Windows.Forms.GroupBox();
            this.Groups = new System.Windows.Forms.ComboBox();
            this.groupBox10 = new System.Windows.Forms.GroupBox();
            this.InstructionType = new System.Windows.Forms.ComboBox();
            this.InstructionPanel = new System.Windows.Forms.Panel();
            this.groupBox9 = new System.Windows.Forms.GroupBox();
            this.user_from = new System.Windows.Forms.ComboBox();
            this.tabControl1.SuspendLayout();
            this.tabPage1.SuspendLayout();
            this.groupBox5.SuspendLayout();
            this.groupBox7.SuspendLayout();
            this.groupBox6.SuspendLayout();
            this.groupBox4.SuspendLayout();
            this.TerminalAdmin.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.InstallerGroup.SuspendLayout();
            this.tabPage2.SuspendLayout();
            this.groupBox8.SuspendLayout();
            this.groupBox11.SuspendLayout();
            this.groupBox10.SuspendLayout();
            this.groupBox9.SuspendLayout();
            this.SuspendLayout();
            // 
            // terminal
            // 
            this.terminal.BackColor = System.Drawing.SystemColors.WindowText;
            this.terminal.ForeColor = System.Drawing.SystemColors.Window;
            this.terminal.FormattingEnabled = true;
            this.terminal.ItemHeight = 12;
            this.terminal.Location = new System.Drawing.Point(582, 8);
            this.terminal.Name = "terminal";
            this.terminal.Size = new System.Drawing.Size(600, 796);
            this.terminal.TabIndex = 2;
            this.terminal.TabStop = false;
            this.terminal.DoubleClick += new System.EventHandler(this.terminal_DoubleClick);
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // tabControl1
            // 
            this.tabControl1.Controls.Add(this.tabPage1);
            this.tabControl1.Controls.Add(this.tabPage2);
            this.tabControl1.Location = new System.Drawing.Point(12, 8);
            this.tabControl1.Name = "tabControl1";
            this.tabControl1.SelectedIndex = 0;
            this.tabControl1.Size = new System.Drawing.Size(564, 796);
            this.tabControl1.TabIndex = 7;
            // 
            // tabPage1
            // 
            this.tabPage1.Controls.Add(this.groupBox5);
            this.tabPage1.Controls.Add(this.groupBox4);
            this.tabPage1.Controls.Add(this.TerminalAdmin);
            this.tabPage1.Controls.Add(this.groupBox1);
            this.tabPage1.Controls.Add(this.InstallerGroup);
            this.tabPage1.Location = new System.Drawing.Point(4, 22);
            this.tabPage1.Name = "tabPage1";
            this.tabPage1.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage1.Size = new System.Drawing.Size(556, 770);
            this.tabPage1.TabIndex = 0;
            this.tabPage1.Text = "登入與操作";
            this.tabPage1.UseVisualStyleBackColor = true;
            // 
            // groupBox5
            // 
            this.groupBox5.Controls.Add(this.groupBox7);
            this.groupBox5.Controls.Add(this.groupBox6);
            this.groupBox5.Location = new System.Drawing.Point(7, 430);
            this.groupBox5.Name = "groupBox5";
            this.groupBox5.Size = new System.Drawing.Size(406, 313);
            this.groupBox5.TabIndex = 11;
            this.groupBox5.TabStop = false;
            this.groupBox5.Text = "存檔操作";
            // 
            // groupBox7
            // 
            this.groupBox7.Controls.Add(this.showpwd);
            this.groupBox7.Controls.Add(this.label7);
            this.groupBox7.Controls.Add(this.label5);
            this.groupBox7.Controls.Add(this.label6);
            this.groupBox7.Controls.Add(this.label4);
            this.groupBox7.Controls.Add(this.label3);
            this.groupBox7.Controls.Add(this.UsersComboBox);
            this.groupBox7.Controls.Add(this.UsersRemove);
            this.groupBox7.Controls.Add(this.UsersAppend);
            this.groupBox7.Controls.Add(this.certtext);
            this.groupBox7.Controls.Add(this.tokentext);
            this.groupBox7.Controls.Add(this.pwdtext);
            this.groupBox7.Controls.Add(this.mailtext);
            this.groupBox7.Controls.Add(this.midtext);
            this.groupBox7.Location = new System.Drawing.Point(206, 21);
            this.groupBox7.Name = "groupBox7";
            this.groupBox7.Size = new System.Drawing.Size(194, 286);
            this.groupBox7.TabIndex = 8;
            this.groupBox7.TabStop = false;
            this.groupBox7.Text = "登入管理";
            // 
            // showpwd
            // 
            this.showpwd.AutoSize = true;
            this.showpwd.Checked = true;
            this.showpwd.CheckState = System.Windows.Forms.CheckState.Checked;
            this.showpwd.Location = new System.Drawing.Point(58, 214);
            this.showpwd.Name = "showpwd";
            this.showpwd.Size = new System.Drawing.Size(72, 16);
            this.showpwd.TabIndex = 26;
            this.showpwd.Text = "遮蔽輸入";
            this.showpwd.UseVisualStyleBackColor = true;
            this.showpwd.CheckedChanged += new System.EventHandler(this.showpwd_CheckedChanged);
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(22, 181);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(25, 12);
            this.label7.TabIndex = 25;
            this.label7.Text = "Cert";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(22, 121);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(48, 12);
            this.label5.TabIndex = 23;
            this.label5.Text = "Password";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(22, 151);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(35, 12);
            this.label6.TabIndex = 22;
            this.label6.Text = "Token";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(22, 91);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(44, 12);
            this.label4.TabIndex = 21;
            this.label4.Text = "Account";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(22, 61);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(27, 12);
            this.label3.TabIndex = 20;
            this.label3.Text = "MID";
            // 
            // UsersComboBox
            // 
            this.UsersComboBox.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.UsersComboBox.FormattingEnabled = true;
            this.UsersComboBox.Location = new System.Drawing.Point(37, 18);
            this.UsersComboBox.Name = "UsersComboBox";
            this.UsersComboBox.Size = new System.Drawing.Size(121, 20);
            this.UsersComboBox.TabIndex = 19;
            this.UsersComboBox.TabStop = false;
            this.UsersComboBox.SelectedIndexChanged += new System.EventHandler(this.UsersComboBox_SelectedIndexChanged);
            // 
            // UsersRemove
            // 
            this.UsersRemove.Location = new System.Drawing.Point(105, 245);
            this.UsersRemove.Name = "UsersRemove";
            this.UsersRemove.Size = new System.Drawing.Size(75, 20);
            this.UsersRemove.TabIndex = 18;
            this.UsersRemove.TabStop = false;
            this.UsersRemove.Text = "刪除";
            this.UsersRemove.UseVisualStyleBackColor = true;
            this.UsersRemove.Click += new System.EventHandler(this.UsersRemove_Click);
            // 
            // UsersAppend
            // 
            this.UsersAppend.Location = new System.Drawing.Point(24, 245);
            this.UsersAppend.Name = "UsersAppend";
            this.UsersAppend.Size = new System.Drawing.Size(75, 20);
            this.UsersAppend.TabIndex = 17;
            this.UsersAppend.TabStop = false;
            this.UsersAppend.Text = "新增";
            this.UsersAppend.UseVisualStyleBackColor = true;
            this.UsersAppend.Click += new System.EventHandler(this.UsersAppend_Click);
            // 
            // certtext
            // 
            this.certtext.Location = new System.Drawing.Point(80, 176);
            this.certtext.Name = "certtext";
            this.certtext.Size = new System.Drawing.Size(100, 22);
            this.certtext.TabIndex = 16;
            // 
            // tokentext
            // 
            this.tokentext.Location = new System.Drawing.Point(80, 146);
            this.tokentext.Name = "tokentext";
            this.tokentext.Size = new System.Drawing.Size(100, 22);
            this.tokentext.TabIndex = 15;
            // 
            // pwdtext
            // 
            this.pwdtext.Location = new System.Drawing.Point(80, 116);
            this.pwdtext.Name = "pwdtext";
            this.pwdtext.Size = new System.Drawing.Size(100, 22);
            this.pwdtext.TabIndex = 14;
            // 
            // mailtext
            // 
            this.mailtext.Location = new System.Drawing.Point(80, 86);
            this.mailtext.Name = "mailtext";
            this.mailtext.Size = new System.Drawing.Size(100, 22);
            this.mailtext.TabIndex = 13;
            // 
            // midtext
            // 
            this.midtext.Location = new System.Drawing.Point(80, 56);
            this.midtext.Name = "midtext";
            this.midtext.Size = new System.Drawing.Size(100, 22);
            this.midtext.TabIndex = 12;
            // 
            // groupBox6
            // 
            this.groupBox6.Controls.Add(this.permissionRemove);
            this.groupBox6.Controls.Add(this.permissionAppend);
            this.groupBox6.Controls.Add(this.label2);
            this.groupBox6.Controls.Add(this.permissionInput);
            this.groupBox6.Controls.Add(this.label1);
            this.groupBox6.Controls.Add(this.permission);
            this.groupBox6.Location = new System.Drawing.Point(6, 21);
            this.groupBox6.Name = "groupBox6";
            this.groupBox6.Size = new System.Drawing.Size(194, 286);
            this.groupBox6.TabIndex = 7;
            this.groupBox6.TabStop = false;
            this.groupBox6.Text = "權限後臺管理";
            // 
            // permissionRemove
            // 
            this.permissionRemove.Location = new System.Drawing.Point(99, 193);
            this.permissionRemove.Name = "permissionRemove";
            this.permissionRemove.Size = new System.Drawing.Size(75, 20);
            this.permissionRemove.TabIndex = 11;
            this.permissionRemove.TabStop = false;
            this.permissionRemove.Text = "刪除";
            this.permissionRemove.UseVisualStyleBackColor = true;
            this.permissionRemove.Click += new System.EventHandler(this.permissionRemove_Click);
            // 
            // permissionAppend
            // 
            this.permissionAppend.Location = new System.Drawing.Point(18, 193);
            this.permissionAppend.Name = "permissionAppend";
            this.permissionAppend.Size = new System.Drawing.Size(75, 20);
            this.permissionAppend.TabIndex = 10;
            this.permissionAppend.TabStop = false;
            this.permissionAppend.Text = "新增";
            this.permissionAppend.UseVisualStyleBackColor = true;
            this.permissionAppend.Click += new System.EventHandler(this.permissionAppend_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(71, 102);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(41, 12);
            this.label2.TabIndex = 9;
            this.label2.Text = "輸入欄";
            // 
            // permissionInput
            // 
            this.permissionInput.Location = new System.Drawing.Point(40, 131);
            this.permissionInput.Name = "permissionInput";
            this.permissionInput.Size = new System.Drawing.Size(100, 22);
            this.permissionInput.TabIndex = 8;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(75, 32);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(29, 12);
            this.label1.TabIndex = 7;
            this.label1.Text = "類型";
            // 
            // permission
            // 
            this.permission.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.permission.FormattingEnabled = true;
            this.permission.Location = new System.Drawing.Point(33, 56);
            this.permission.Name = "permission";
            this.permission.Size = new System.Drawing.Size(121, 20);
            this.permission.TabIndex = 6;
            this.permission.TabStop = false;
            this.permission.SelectedIndexChanged += new System.EventHandler(this.permission_SelectedIndexChanged);
            // 
            // groupBox4
            // 
            this.groupBox4.Controls.Add(this.ResetError);
            this.groupBox4.Controls.Add(this.LoginComboBox);
            this.groupBox4.Controls.Add(this.logout);
            this.groupBox4.Controls.Add(this.login);
            this.groupBox4.Location = new System.Drawing.Point(219, 6);
            this.groupBox4.Name = "groupBox4";
            this.groupBox4.Size = new System.Drawing.Size(200, 206);
            this.groupBox4.TabIndex = 10;
            this.groupBox4.TabStop = false;
            this.groupBox4.Text = "登入與登出";
            // 
            // ResetError
            // 
            this.ResetError.Location = new System.Drawing.Point(66, 161);
            this.ResetError.Name = "ResetError";
            this.ResetError.Size = new System.Drawing.Size(75, 20);
            this.ResetError.TabIndex = 8;
            this.ResetError.TabStop = false;
            this.ResetError.Text = "緊急重置";
            this.ResetError.UseVisualStyleBackColor = true;
            this.ResetError.Click += new System.EventHandler(this.ResetError_Click);
            // 
            // LoginComboBox
            // 
            this.LoginComboBox.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.LoginComboBox.FormattingEnabled = true;
            this.LoginComboBox.Location = new System.Drawing.Point(42, 21);
            this.LoginComboBox.Name = "LoginComboBox";
            this.LoginComboBox.Size = new System.Drawing.Size(121, 20);
            this.LoginComboBox.TabIndex = 7;
            this.LoginComboBox.TabStop = false;
            this.LoginComboBox.SelectedIndexChanged += new System.EventHandler(this.LoginComboBox_SelectedIndexChanged);
            // 
            // logout
            // 
            this.logout.Location = new System.Drawing.Point(66, 118);
            this.logout.Name = "logout";
            this.logout.Size = new System.Drawing.Size(75, 20);
            this.logout.TabIndex = 6;
            this.logout.TabStop = false;
            this.logout.Text = "登出";
            this.logout.UseVisualStyleBackColor = true;
            this.logout.Click += new System.EventHandler(this.logout_Click);
            // 
            // login
            // 
            this.login.Location = new System.Drawing.Point(66, 68);
            this.login.Name = "login";
            this.login.Size = new System.Drawing.Size(75, 20);
            this.login.TabIndex = 4;
            this.login.TabStop = false;
            this.login.Text = "登入";
            this.login.UseVisualStyleBackColor = true;
            this.login.Click += new System.EventHandler(this.login_Click);
            // 
            // TerminalAdmin
            // 
            this.TerminalAdmin.Controls.Add(this.groupBox3);
            this.TerminalAdmin.Controls.Add(this.groupBox2);
            this.TerminalAdmin.Location = new System.Drawing.Point(6, 218);
            this.TerminalAdmin.Name = "TerminalAdmin";
            this.TerminalAdmin.Size = new System.Drawing.Size(413, 206);
            this.TerminalAdmin.TabIndex = 9;
            this.TerminalAdmin.TabStop = false;
            this.TerminalAdmin.Text = "終端管理";
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.CmdExecutes);
            this.groupBox3.Controls.Add(this.customizes);
            this.groupBox3.Controls.Add(this.CmdExecuteArray);
            this.groupBox3.Controls.Add(this.AppendExecute);
            this.groupBox3.Controls.Add(this.RemoveExecute);
            this.groupBox3.Location = new System.Drawing.Point(213, 21);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(194, 179);
            this.groupBox3.TabIndex = 3;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "多道命令";
            // 
            // CmdExecutes
            // 
            this.CmdExecutes.Location = new System.Drawing.Point(52, 21);
            this.CmdExecutes.Name = "CmdExecutes";
            this.CmdExecutes.Size = new System.Drawing.Size(100, 22);
            this.CmdExecutes.TabIndex = 7;
            this.CmdExecutes.KeyDown += new System.Windows.Forms.KeyEventHandler(this.CmdExecutes_KeyDown);
            // 
            // customizes
            // 
            this.customizes.Location = new System.Drawing.Point(66, 142);
            this.customizes.Name = "customizes";
            this.customizes.Size = new System.Drawing.Size(75, 20);
            this.customizes.TabIndex = 6;
            this.customizes.TabStop = false;
            this.customizes.Text = "執行命令";
            this.customizes.UseVisualStyleBackColor = true;
            this.customizes.Click += new System.EventHandler(this.customizes_Click);
            // 
            // CmdExecuteArray
            // 
            this.CmdExecuteArray.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.CmdExecuteArray.FormattingEnabled = true;
            this.CmdExecuteArray.Location = new System.Drawing.Point(42, 63);
            this.CmdExecuteArray.Name = "CmdExecuteArray";
            this.CmdExecuteArray.Size = new System.Drawing.Size(121, 20);
            this.CmdExecuteArray.TabIndex = 5;
            this.CmdExecuteArray.TabStop = false;
            // 
            // AppendExecute
            // 
            this.AppendExecute.Location = new System.Drawing.Point(18, 110);
            this.AppendExecute.Name = "AppendExecute";
            this.AppendExecute.Size = new System.Drawing.Size(75, 20);
            this.AppendExecute.TabIndex = 3;
            this.AppendExecute.TabStop = false;
            this.AppendExecute.Text = "新增命令";
            this.AppendExecute.UseVisualStyleBackColor = true;
            this.AppendExecute.Click += new System.EventHandler(this.AppendExecute_Click);
            // 
            // RemoveExecute
            // 
            this.RemoveExecute.Location = new System.Drawing.Point(113, 110);
            this.RemoveExecute.Name = "RemoveExecute";
            this.RemoveExecute.Size = new System.Drawing.Size(75, 20);
            this.RemoveExecute.TabIndex = 4;
            this.RemoveExecute.TabStop = false;
            this.RemoveExecute.Text = "刪除命令";
            this.RemoveExecute.UseVisualStyleBackColor = true;
            this.RemoveExecute.Click += new System.EventHandler(this.RemoveExecute_Click);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.CmdExecute);
            this.groupBox2.Controls.Add(this.customize);
            this.groupBox2.Location = new System.Drawing.Point(7, 19);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(200, 181);
            this.groupBox2.TabIndex = 6;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "單一命令";
            // 
            // CmdExecute
            // 
            this.CmdExecute.Location = new System.Drawing.Point(54, 52);
            this.CmdExecute.Name = "CmdExecute";
            this.CmdExecute.Size = new System.Drawing.Size(100, 22);
            this.CmdExecute.TabIndex = 2;
            this.CmdExecute.KeyDown += new System.Windows.Forms.KeyEventHandler(this.CmdExecute_KeyDown);
            // 
            // customize
            // 
            this.customize.Location = new System.Drawing.Point(65, 112);
            this.customize.Name = "customize";
            this.customize.Size = new System.Drawing.Size(75, 20);
            this.customize.TabIndex = 1;
            this.customize.TabStop = false;
            this.customize.Text = "執行";
            this.customize.UseVisualStyleBackColor = true;
            this.customize.Click += new System.EventHandler(this.customize_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.TerminalClear);
            this.groupBox1.Controls.Add(this.TerminalFontColor);
            this.groupBox1.Controls.Add(this.TerminalBackColor);
            this.groupBox1.Controls.Add(this.TerminalFontcolor_Label);
            this.groupBox1.Controls.Add(this.TerminalBackcolor_Label);
            this.groupBox1.Location = new System.Drawing.Point(6, 82);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(207, 130);
            this.groupBox1.TabIndex = 8;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "終端設定";
            // 
            // TerminalClear
            // 
            this.TerminalClear.Location = new System.Drawing.Point(72, 94);
            this.TerminalClear.Name = "TerminalClear";
            this.TerminalClear.Size = new System.Drawing.Size(75, 20);
            this.TerminalClear.TabIndex = 6;
            this.TerminalClear.TabStop = false;
            this.TerminalClear.Text = "終端清理";
            this.TerminalClear.UseVisualStyleBackColor = true;
            this.TerminalClear.Click += new System.EventHandler(this.TerminalClear_Click);
            // 
            // TerminalFontColor
            // 
            this.TerminalFontColor.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.TerminalFontColor.FormattingEnabled = true;
            this.TerminalFontColor.Location = new System.Drawing.Point(80, 58);
            this.TerminalFontColor.Name = "TerminalFontColor";
            this.TerminalFontColor.Size = new System.Drawing.Size(121, 20);
            this.TerminalFontColor.TabIndex = 5;
            this.TerminalFontColor.TabStop = false;
            this.TerminalFontColor.SelectedIndexChanged += new System.EventHandler(this.TerminalFontColor_SelectedIndexChanged);
            // 
            // TerminalBackColor
            // 
            this.TerminalBackColor.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.TerminalBackColor.FormattingEnabled = true;
            this.TerminalBackColor.Location = new System.Drawing.Point(80, 21);
            this.TerminalBackColor.Name = "TerminalBackColor";
            this.TerminalBackColor.Size = new System.Drawing.Size(121, 20);
            this.TerminalBackColor.TabIndex = 4;
            this.TerminalBackColor.TabStop = false;
            this.TerminalBackColor.SelectedIndexChanged += new System.EventHandler(this.TerminalBackColor_SelectedIndexChanged);
            // 
            // TerminalFontcolor_Label
            // 
            this.TerminalFontcolor_Label.AutoSize = true;
            this.TerminalFontcolor_Label.Location = new System.Drawing.Point(23, 61);
            this.TerminalFontcolor_Label.Name = "TerminalFontcolor_Label";
            this.TerminalFontcolor_Label.Size = new System.Drawing.Size(53, 12);
            this.TerminalFontcolor_Label.TabIndex = 1;
            this.TerminalFontcolor_Label.Text = "文字顏色";
            // 
            // TerminalBackcolor_Label
            // 
            this.TerminalBackcolor_Label.AutoSize = true;
            this.TerminalBackcolor_Label.Location = new System.Drawing.Point(23, 27);
            this.TerminalBackcolor_Label.Name = "TerminalBackcolor_Label";
            this.TerminalBackcolor_Label.Size = new System.Drawing.Size(53, 12);
            this.TerminalBackcolor_Label.TabIndex = 0;
            this.TerminalBackcolor_Label.Text = "背景顏色";
            // 
            // InstallerGroup
            // 
            this.InstallerGroup.Controls.Add(this.mustpip);
            this.InstallerGroup.Location = new System.Drawing.Point(6, 6);
            this.InstallerGroup.Name = "InstallerGroup";
            this.InstallerGroup.Size = new System.Drawing.Size(207, 70);
            this.InstallerGroup.TabIndex = 7;
            this.InstallerGroup.TabStop = false;
            this.InstallerGroup.Text = "必備安裝";
            // 
            // mustpip
            // 
            this.mustpip.Location = new System.Drawing.Point(50, 21);
            this.mustpip.Name = "mustpip";
            this.mustpip.Size = new System.Drawing.Size(100, 25);
            this.mustpip.TabIndex = 0;
            this.mustpip.TabStop = false;
            this.mustpip.Text = "必備安裝集合庫";
            this.mustpip.UseVisualStyleBackColor = true;
            this.mustpip.Click += new System.EventHandler(this.mustpip_Click);
            // 
            // tabPage2
            // 
            this.tabPage2.Controls.Add(this.groupBox8);
            this.tabPage2.Controls.Add(this.groupBox11);
            this.tabPage2.Controls.Add(this.groupBox10);
            this.tabPage2.Controls.Add(this.InstructionPanel);
            this.tabPage2.Controls.Add(this.groupBox9);
            this.tabPage2.Location = new System.Drawing.Point(4, 22);
            this.tabPage2.Name = "tabPage2";
            this.tabPage2.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage2.Size = new System.Drawing.Size(556, 770);
            this.tabPage2.TabIndex = 1;
            this.tabPage2.Text = "指令介面";
            this.tabPage2.UseVisualStyleBackColor = true;
            // 
            // groupBox8
            // 
            this.groupBox8.Controls.Add(this.GroupMembers);
            this.groupBox8.Location = new System.Drawing.Point(415, 6);
            this.groupBox8.Name = "groupBox8";
            this.groupBox8.Size = new System.Drawing.Size(130, 53);
            this.groupBox8.TabIndex = 1;
            this.groupBox8.TabStop = false;
            this.groupBox8.Text = "群組用戶";
            // 
            // GroupMembers
            // 
            this.GroupMembers.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.GroupMembers.FormattingEnabled = true;
            this.GroupMembers.Location = new System.Drawing.Point(6, 21);
            this.GroupMembers.Name = "GroupMembers";
            this.GroupMembers.Size = new System.Drawing.Size(121, 20);
            this.GroupMembers.TabIndex = 0;
            this.GroupMembers.TabStop = false;
            this.GroupMembers.SelectedIndexChanged += new System.EventHandler(this.GroupMembers_SelectedIndexChanged);
            // 
            // groupBox11
            // 
            this.groupBox11.Controls.Add(this.Groups);
            this.groupBox11.Location = new System.Drawing.Point(279, 6);
            this.groupBox11.Name = "groupBox11";
            this.groupBox11.Size = new System.Drawing.Size(130, 53);
            this.groupBox11.TabIndex = 11;
            this.groupBox11.TabStop = false;
            this.groupBox11.Text = "群組列表";
            // 
            // Groups
            // 
            this.Groups.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.Groups.FormattingEnabled = true;
            this.Groups.Location = new System.Drawing.Point(6, 21);
            this.Groups.Name = "Groups";
            this.Groups.Size = new System.Drawing.Size(121, 20);
            this.Groups.TabIndex = 3;
            this.Groups.TabStop = false;
            this.Groups.SelectedIndexChanged += new System.EventHandler(this.Groups_SelectedIndexChanged);
            // 
            // groupBox10
            // 
            this.groupBox10.Controls.Add(this.InstructionType);
            this.groupBox10.Location = new System.Drawing.Point(146, 6);
            this.groupBox10.Name = "groupBox10";
            this.groupBox10.Size = new System.Drawing.Size(130, 53);
            this.groupBox10.TabIndex = 4;
            this.groupBox10.TabStop = false;
            this.groupBox10.Text = "指令類型";
            // 
            // InstructionType
            // 
            this.InstructionType.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.InstructionType.FormattingEnabled = true;
            this.InstructionType.Location = new System.Drawing.Point(6, 21);
            this.InstructionType.Name = "InstructionType";
            this.InstructionType.Size = new System.Drawing.Size(121, 20);
            this.InstructionType.TabIndex = 2;
            this.InstructionType.TabStop = false;
            this.InstructionType.SelectedIndexChanged += new System.EventHandler(this.InstructionType_SelectedIndexChanged);
            // 
            // InstructionPanel
            // 
            this.InstructionPanel.Location = new System.Drawing.Point(6, 65);
            this.InstructionPanel.Name = "InstructionPanel";
            this.InstructionPanel.Size = new System.Drawing.Size(544, 626);
            this.InstructionPanel.TabIndex = 3;
            // 
            // groupBox9
            // 
            this.groupBox9.Controls.Add(this.user_from);
            this.groupBox9.Location = new System.Drawing.Point(6, 6);
            this.groupBox9.Name = "groupBox9";
            this.groupBox9.Size = new System.Drawing.Size(130, 53);
            this.groupBox9.TabIndex = 2;
            this.groupBox9.TabStop = false;
            this.groupBox9.Text = "使用者";
            // 
            // user_from
            // 
            this.user_from.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.user_from.FormattingEnabled = true;
            this.user_from.Location = new System.Drawing.Point(6, 21);
            this.user_from.Name = "user_from";
            this.user_from.Size = new System.Drawing.Size(121, 20);
            this.user_from.TabIndex = 1;
            this.user_from.TabStop = false;
            this.user_from.SelectedIndexChanged += new System.EventHandler(this.user_from_SelectedIndexChanged);
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1184, 811);
            this.Controls.Add(this.tabControl1);
            this.Controls.Add(this.terminal);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "MainForm";
            this.Text = "LinePMD";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.MainForm_FormClosing);
            this.tabControl1.ResumeLayout(false);
            this.tabPage1.ResumeLayout(false);
            this.groupBox5.ResumeLayout(false);
            this.groupBox7.ResumeLayout(false);
            this.groupBox7.PerformLayout();
            this.groupBox6.ResumeLayout(false);
            this.groupBox6.PerformLayout();
            this.groupBox4.ResumeLayout(false);
            this.TerminalAdmin.ResumeLayout(false);
            this.groupBox3.ResumeLayout(false);
            this.groupBox3.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.InstallerGroup.ResumeLayout(false);
            this.tabPage2.ResumeLayout(false);
            this.groupBox8.ResumeLayout(false);
            this.groupBox11.ResumeLayout(false);
            this.groupBox10.ResumeLayout(false);
            this.groupBox9.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion
        public System.Windows.Forms.ListBox terminal;
        public System.Windows.Forms.Timer timer1;
        public System.Windows.Forms.TabControl tabControl1;
        public System.Windows.Forms.TabPage tabPage1;
        public System.Windows.Forms.GroupBox groupBox5;
        public System.Windows.Forms.GroupBox groupBox7;
        public System.Windows.Forms.GroupBox groupBox6;
        public System.Windows.Forms.Button permissionAppend;
        public System.Windows.Forms.Label label2;
        public System.Windows.Forms.TextBox permissionInput;
        public System.Windows.Forms.Label label1;
        public System.Windows.Forms.ComboBox permission;
        public System.Windows.Forms.GroupBox groupBox4;
        public System.Windows.Forms.ComboBox LoginComboBox;
        public System.Windows.Forms.Button logout;
        public System.Windows.Forms.Button login;
        public System.Windows.Forms.GroupBox TerminalAdmin;
        public System.Windows.Forms.GroupBox groupBox3;
        public System.Windows.Forms.TextBox CmdExecutes;
        public System.Windows.Forms.Button customizes;
        public System.Windows.Forms.ComboBox CmdExecuteArray;
        public System.Windows.Forms.Button AppendExecute;
        public System.Windows.Forms.Button RemoveExecute;
        public System.Windows.Forms.GroupBox groupBox2;
        public System.Windows.Forms.TextBox CmdExecute;
        public System.Windows.Forms.Button customize;
        public System.Windows.Forms.GroupBox groupBox1;
        public System.Windows.Forms.ComboBox TerminalFontColor;
        public System.Windows.Forms.ComboBox TerminalBackColor;
        public System.Windows.Forms.Label TerminalFontcolor_Label;
        public System.Windows.Forms.Label TerminalBackcolor_Label;
        public System.Windows.Forms.GroupBox InstallerGroup;
        public System.Windows.Forms.Button mustpip;
        public System.Windows.Forms.TabPage tabPage2;
        public System.Windows.Forms.Button permissionRemove;
        public System.Windows.Forms.Label label7;
        public System.Windows.Forms.Label label5;
        public System.Windows.Forms.Label label6;
        public System.Windows.Forms.Label label4;
        public System.Windows.Forms.Label label3;
        public System.Windows.Forms.ComboBox UsersComboBox;
        public System.Windows.Forms.Button UsersRemove;
        public System.Windows.Forms.Button UsersAppend;
        public System.Windows.Forms.TextBox certtext;
        public System.Windows.Forms.TextBox tokentext;
        public System.Windows.Forms.TextBox mailtext;
        public System.Windows.Forms.TextBox midtext;
        public System.Windows.Forms.TextBox pwdtext;
        public System.Windows.Forms.CheckBox showpwd;
        public System.Windows.Forms.GroupBox groupBox8;
        public System.Windows.Forms.ComboBox GroupMembers;
        public System.Windows.Forms.GroupBox groupBox9;
        public System.Windows.Forms.ComboBox user_from;
        public System.Windows.Forms.GroupBox groupBox10;
        public System.Windows.Forms.ComboBox InstructionType;
        public System.Windows.Forms.Panel InstructionPanel;
        public System.Windows.Forms.GroupBox groupBox11;
        public System.Windows.Forms.ComboBox Groups;
        public System.Windows.Forms.Button TerminalClear;
        public System.Windows.Forms.Button ResetError;
    }
}

