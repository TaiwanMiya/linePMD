namespace LinePMD.Controls
{
    partial class Friends
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

        #region 元件設計工具產生的程式碼

        /// <summary> 
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改
        /// 這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.groupBox5 = new System.Windows.Forms.GroupBox();
            this.Reset = new System.Windows.Forms.Button();
            this.Execute = new System.Windows.Forms.Button();
            this.groupBox4 = new System.Windows.Forms.GroupBox();
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.Input_Hex = new System.Windows.Forms.TextBox();
            this.Input_Oct = new System.Windows.Forms.TextBox();
            this.Input_Dec = new System.Windows.Forms.TextBox();
            this.Input_Bin = new System.Windows.Forms.TextBox();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.label4 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.Output_Hex = new System.Windows.Forms.TextBox();
            this.Output_Oct = new System.Windows.Forms.TextBox();
            this.Output_Dec = new System.Windows.Forms.TextBox();
            this.Output_Bin = new System.Windows.Forms.TextBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.friend0x2 = new System.Windows.Forms.Button();
            this.friend0x1 = new System.Windows.Forms.Button();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.MidDelete = new System.Windows.Forms.Button();
            this.MidList = new System.Windows.Forms.ComboBox();
            this.label10 = new System.Windows.Forms.Label();
            this.MidAppend = new System.Windows.Forms.Button();
            this.label9 = new System.Windows.Forms.Label();
            this.MidText = new System.Windows.Forms.TextBox();
            this.groupBox5.SuspendLayout();
            this.groupBox4.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox5
            // 
            this.groupBox5.Controls.Add(this.Reset);
            this.groupBox5.Controls.Add(this.Execute);
            this.groupBox5.Location = new System.Drawing.Point(59, 431);
            this.groupBox5.Name = "groupBox5";
            this.groupBox5.Size = new System.Drawing.Size(400, 100);
            this.groupBox5.TabIndex = 16;
            this.groupBox5.TabStop = false;
            this.groupBox5.Text = "Operate 操作";
            // 
            // Reset
            // 
            this.Reset.Location = new System.Drawing.Point(246, 44);
            this.Reset.Name = "Reset";
            this.Reset.Size = new System.Drawing.Size(75, 23);
            this.Reset.TabIndex = 13;
            this.Reset.TabStop = false;
            this.Reset.Text = "重置";
            this.Reset.UseVisualStyleBackColor = true;
            this.Reset.Click += new System.EventHandler(this.Reset_Click);
            // 
            // Execute
            // 
            this.Execute.Location = new System.Drawing.Point(59, 44);
            this.Execute.Name = "Execute";
            this.Execute.Size = new System.Drawing.Size(75, 23);
            this.Execute.TabIndex = 12;
            this.Execute.TabStop = false;
            this.Execute.Text = "執行";
            this.Execute.UseVisualStyleBackColor = true;
            this.Execute.Click += new System.EventHandler(this.Execute_Click);
            // 
            // groupBox4
            // 
            this.groupBox4.Controls.Add(this.label5);
            this.groupBox4.Controls.Add(this.label6);
            this.groupBox4.Controls.Add(this.label7);
            this.groupBox4.Controls.Add(this.label8);
            this.groupBox4.Controls.Add(this.Input_Hex);
            this.groupBox4.Controls.Add(this.Input_Oct);
            this.groupBox4.Controls.Add(this.Input_Dec);
            this.groupBox4.Controls.Add(this.Input_Bin);
            this.groupBox4.Location = new System.Drawing.Point(59, 158);
            this.groupBox4.Name = "groupBox4";
            this.groupBox4.Size = new System.Drawing.Size(400, 119);
            this.groupBox4.TabIndex = 15;
            this.groupBox4.TabStop = false;
            this.groupBox4.Text = "Input 輸入";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(192, 79);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(24, 12);
            this.label5.TabIndex = 14;
            this.label5.Text = "Hex";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(6, 79);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(43, 12);
            this.label6.TabIndex = 13;
            this.label6.Text = "Decimal";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(192, 34);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(29, 12);
            this.label7.TabIndex = 12;
            this.label7.Text = "Octal";
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(6, 34);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(37, 12);
            this.label8.TabIndex = 10;
            this.label8.Text = "Binary";
            // 
            // Input_Hex
            // 
            this.Input_Hex.Location = new System.Drawing.Point(246, 76);
            this.Input_Hex.Name = "Input_Hex";
            this.Input_Hex.Size = new System.Drawing.Size(100, 22);
            this.Input_Hex.TabIndex = 4;
            this.Input_Hex.KeyDown += new System.Windows.Forms.KeyEventHandler(this.Input_Hex_KeyDown);
            // 
            // Input_Oct
            // 
            this.Input_Oct.Location = new System.Drawing.Point(246, 31);
            this.Input_Oct.Name = "Input_Oct";
            this.Input_Oct.Size = new System.Drawing.Size(100, 22);
            this.Input_Oct.TabIndex = 2;
            this.Input_Oct.KeyDown += new System.Windows.Forms.KeyEventHandler(this.Input_Oct_KeyDown);
            // 
            // Input_Dec
            // 
            this.Input_Dec.Location = new System.Drawing.Point(59, 76);
            this.Input_Dec.Name = "Input_Dec";
            this.Input_Dec.Size = new System.Drawing.Size(100, 22);
            this.Input_Dec.TabIndex = 3;
            this.Input_Dec.KeyDown += new System.Windows.Forms.KeyEventHandler(this.Input_Dec_KeyDown);
            // 
            // Input_Bin
            // 
            this.Input_Bin.Location = new System.Drawing.Point(59, 31);
            this.Input_Bin.Name = "Input_Bin";
            this.Input_Bin.Size = new System.Drawing.Size(100, 22);
            this.Input_Bin.TabIndex = 1;
            this.Input_Bin.KeyDown += new System.Windows.Forms.KeyEventHandler(this.Input_Bin_KeyDown);
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.label4);
            this.groupBox3.Controls.Add(this.label3);
            this.groupBox3.Controls.Add(this.label2);
            this.groupBox3.Controls.Add(this.label1);
            this.groupBox3.Controls.Add(this.Output_Hex);
            this.groupBox3.Controls.Add(this.Output_Oct);
            this.groupBox3.Controls.Add(this.Output_Dec);
            this.groupBox3.Controls.Add(this.Output_Bin);
            this.groupBox3.Location = new System.Drawing.Point(59, 292);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(400, 119);
            this.groupBox3.TabIndex = 14;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "Output 輸出";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(192, 79);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(24, 12);
            this.label4.TabIndex = 14;
            this.label4.Text = "Hex";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(6, 79);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(43, 12);
            this.label3.TabIndex = 13;
            this.label3.Text = "Decimal";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(192, 34);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(29, 12);
            this.label2.TabIndex = 12;
            this.label2.Text = "Octal";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(6, 34);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(37, 12);
            this.label1.TabIndex = 10;
            this.label1.Text = "Binary";
            // 
            // Output_Hex
            // 
            this.Output_Hex.Location = new System.Drawing.Point(246, 76);
            this.Output_Hex.Name = "Output_Hex";
            this.Output_Hex.ReadOnly = true;
            this.Output_Hex.Size = new System.Drawing.Size(100, 22);
            this.Output_Hex.TabIndex = 11;
            this.Output_Hex.TabStop = false;
            // 
            // Output_Oct
            // 
            this.Output_Oct.Location = new System.Drawing.Point(246, 31);
            this.Output_Oct.Name = "Output_Oct";
            this.Output_Oct.ReadOnly = true;
            this.Output_Oct.Size = new System.Drawing.Size(100, 22);
            this.Output_Oct.TabIndex = 10;
            this.Output_Oct.TabStop = false;
            // 
            // Output_Dec
            // 
            this.Output_Dec.Location = new System.Drawing.Point(59, 76);
            this.Output_Dec.Name = "Output_Dec";
            this.Output_Dec.ReadOnly = true;
            this.Output_Dec.Size = new System.Drawing.Size(100, 22);
            this.Output_Dec.TabIndex = 9;
            this.Output_Dec.TabStop = false;
            // 
            // Output_Bin
            // 
            this.Output_Bin.Location = new System.Drawing.Point(59, 31);
            this.Output_Bin.Name = "Output_Bin";
            this.Output_Bin.ReadOnly = true;
            this.Output_Bin.Size = new System.Drawing.Size(100, 22);
            this.Output_Bin.TabIndex = 8;
            this.Output_Bin.TabStop = false;
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.friend0x2);
            this.groupBox1.Controls.Add(this.friend0x1);
            this.groupBox1.Location = new System.Drawing.Point(59, 16);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(400, 50);
            this.groupBox1.TabIndex = 21;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Friend Items";
            // 
            // friend0x2
            // 
            this.friend0x2.Location = new System.Drawing.Point(246, 18);
            this.friend0x2.Name = "friend0x2";
            this.friend0x2.Size = new System.Drawing.Size(75, 23);
            this.friend0x2.TabIndex = 5;
            this.friend0x2.TabStop = false;
            this.friend0x2.Text = "Check";
            this.friend0x2.UseVisualStyleBackColor = true;
            this.friend0x2.Click += new System.EventHandler(this.friend0x2_Click);
            // 
            // friend0x1
            // 
            this.friend0x1.Location = new System.Drawing.Point(59, 18);
            this.friend0x1.Name = "friend0x1";
            this.friend0x1.Size = new System.Drawing.Size(75, 23);
            this.friend0x1.TabIndex = 4;
            this.friend0x1.TabStop = false;
            this.friend0x1.Text = "Append";
            this.friend0x1.UseVisualStyleBackColor = true;
            this.friend0x1.Click += new System.EventHandler(this.friend0x1_Click);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.MidDelete);
            this.groupBox2.Controls.Add(this.MidList);
            this.groupBox2.Controls.Add(this.label10);
            this.groupBox2.Controls.Add(this.MidAppend);
            this.groupBox2.Controls.Add(this.label9);
            this.groupBox2.Controls.Add(this.MidText);
            this.groupBox2.Location = new System.Drawing.Point(59, 72);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(400, 80);
            this.groupBox2.TabIndex = 22;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Friend Function 好友功能";
            // 
            // MidDelete
            // 
            this.MidDelete.Location = new System.Drawing.Point(246, 49);
            this.MidDelete.Name = "MidDelete";
            this.MidDelete.Size = new System.Drawing.Size(75, 23);
            this.MidDelete.TabIndex = 19;
            this.MidDelete.TabStop = false;
            this.MidDelete.Text = "Delete";
            this.MidDelete.UseVisualStyleBackColor = true;
            this.MidDelete.Click += new System.EventHandler(this.MidDelete_Click);
            // 
            // MidList
            // 
            this.MidList.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.MidList.FormattingEnabled = true;
            this.MidList.Location = new System.Drawing.Point(59, 51);
            this.MidList.Name = "MidList";
            this.MidList.Size = new System.Drawing.Size(121, 20);
            this.MidList.TabIndex = 18;
            this.MidList.SelectedIndexChanged += new System.EventHandler(this.MidList_SelectedIndexChanged);
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Location = new System.Drawing.Point(10, 54);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(41, 12);
            this.label10.TabIndex = 17;
            this.label10.Text = "MidList";
            // 
            // MidAppend
            // 
            this.MidAppend.Location = new System.Drawing.Point(246, 19);
            this.MidAppend.Name = "MidAppend";
            this.MidAppend.Size = new System.Drawing.Size(75, 23);
            this.MidAppend.TabIndex = 16;
            this.MidAppend.TabStop = false;
            this.MidAppend.Text = "Append";
            this.MidAppend.UseVisualStyleBackColor = true;
            this.MidAppend.Click += new System.EventHandler(this.MidAppend_Click);
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(20, 25);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(24, 12);
            this.label9.TabIndex = 15;
            this.label9.Text = "Mid";
            // 
            // MidText
            // 
            this.MidText.Location = new System.Drawing.Point(59, 21);
            this.MidText.Name = "MidText";
            this.MidText.Size = new System.Drawing.Size(100, 22);
            this.MidText.TabIndex = 14;
            this.MidText.KeyDown += new System.Windows.Forms.KeyEventHandler(this.MidText_KeyDown);
            // 
            // Friends
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.groupBox5);
            this.Controls.Add(this.groupBox4);
            this.Controls.Add(this.groupBox3);
            this.Name = "Friends";
            this.Size = new System.Drawing.Size(530, 610);
            this.groupBox5.ResumeLayout(false);
            this.groupBox4.ResumeLayout(false);
            this.groupBox4.PerformLayout();
            this.groupBox3.ResumeLayout(false);
            this.groupBox3.PerformLayout();
            this.groupBox1.ResumeLayout(false);
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion
        public System.Windows.Forms.GroupBox groupBox5;
        public System.Windows.Forms.Button Reset;
        public System.Windows.Forms.Button Execute;
        public System.Windows.Forms.GroupBox groupBox4;
        public System.Windows.Forms.Label label5;
        public System.Windows.Forms.Label label6;
        public System.Windows.Forms.Label label7;
        public System.Windows.Forms.Label label8;
        public System.Windows.Forms.TextBox Input_Hex;
        public System.Windows.Forms.TextBox Input_Oct;
        public System.Windows.Forms.TextBox Input_Dec;
        public System.Windows.Forms.TextBox Input_Bin;
        public System.Windows.Forms.GroupBox groupBox3;
        public System.Windows.Forms.Label label4;
        public System.Windows.Forms.Label label3;
        public System.Windows.Forms.Label label2;
        public System.Windows.Forms.Label label1;
        public System.Windows.Forms.TextBox Output_Hex;
        public System.Windows.Forms.TextBox Output_Oct;
        public System.Windows.Forms.TextBox Output_Dec;
        public System.Windows.Forms.TextBox Output_Bin;
        public System.Windows.Forms.GroupBox groupBox1;
        public System.Windows.Forms.Button friend0x2;
        public System.Windows.Forms.Button friend0x1;
        private System.Windows.Forms.GroupBox groupBox2;
        public System.Windows.Forms.Button MidDelete;
        private System.Windows.Forms.ComboBox MidList;
        private System.Windows.Forms.Label label10;
        public System.Windows.Forms.Button MidAppend;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.TextBox MidText;
    }
}
