namespace LinePMD.Controls
{
    partial class Urls
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
            this.url0x8 = new System.Windows.Forms.Button();
            this.url0x4 = new System.Windows.Forms.Button();
            this.url0x2 = new System.Windows.Forms.Button();
            this.url0x1 = new System.Windows.Forms.Button();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.URLDelete = new System.Windows.Forms.Button();
            this.URLList = new System.Windows.Forms.ComboBox();
            this.label11 = new System.Windows.Forms.Label();
            this.URLAppend = new System.Windows.Forms.Button();
            this.label12 = new System.Windows.Forms.Label();
            this.URLText = new System.Windows.Forms.TextBox();
            this.GidDelete = new System.Windows.Forms.Button();
            this.GidList = new System.Windows.Forms.ComboBox();
            this.label10 = new System.Windows.Forms.Label();
            this.GidAppend = new System.Windows.Forms.Button();
            this.label9 = new System.Windows.Forms.Label();
            this.GidText = new System.Windows.Forms.TextBox();
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
            this.groupBox5.Location = new System.Drawing.Point(59, 503);
            this.groupBox5.Name = "groupBox5";
            this.groupBox5.Size = new System.Drawing.Size(400, 100);
            this.groupBox5.TabIndex = 21;
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
            this.groupBox4.Location = new System.Drawing.Point(59, 230);
            this.groupBox4.Name = "groupBox4";
            this.groupBox4.Size = new System.Drawing.Size(400, 119);
            this.groupBox4.TabIndex = 20;
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
            this.groupBox3.Location = new System.Drawing.Point(59, 364);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(400, 119);
            this.groupBox3.TabIndex = 19;
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
            this.groupBox1.Controls.Add(this.url0x8);
            this.groupBox1.Controls.Add(this.url0x4);
            this.groupBox1.Controls.Add(this.url0x2);
            this.groupBox1.Controls.Add(this.url0x1);
            this.groupBox1.Location = new System.Drawing.Point(59, 16);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(400, 50);
            this.groupBox1.TabIndex = 23;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Groups URL Items";
            // 
            // url0x8
            // 
            this.url0x8.Location = new System.Drawing.Point(300, 18);
            this.url0x8.Name = "url0x8";
            this.url0x8.Size = new System.Drawing.Size(75, 23);
            this.url0x8.TabIndex = 7;
            this.url0x8.TabStop = false;
            this.url0x8.Text = "URL OFF";
            this.url0x8.UseVisualStyleBackColor = true;
            this.url0x8.Click += new System.EventHandler(this.url0x8_Click);
            // 
            // url0x4
            // 
            this.url0x4.Location = new System.Drawing.Point(210, 18);
            this.url0x4.Name = "url0x4";
            this.url0x4.Size = new System.Drawing.Size(75, 23);
            this.url0x4.TabIndex = 6;
            this.url0x4.TabStop = false;
            this.url0x4.Text = "URL ON";
            this.url0x4.UseVisualStyleBackColor = true;
            this.url0x4.Click += new System.EventHandler(this.url0x4_Click);
            // 
            // url0x2
            // 
            this.url0x2.Location = new System.Drawing.Point(120, 18);
            this.url0x2.Name = "url0x2";
            this.url0x2.Size = new System.Drawing.Size(75, 23);
            this.url0x2.TabIndex = 5;
            this.url0x2.TabStop = false;
            this.url0x2.Text = "Join Group";
            this.url0x2.UseVisualStyleBackColor = true;
            this.url0x2.Click += new System.EventHandler(this.url0x2_Click);
            // 
            // url0x1
            // 
            this.url0x1.Location = new System.Drawing.Point(30, 18);
            this.url0x1.Name = "url0x1";
            this.url0x1.Size = new System.Drawing.Size(75, 23);
            this.url0x1.TabIndex = 4;
            this.url0x1.TabStop = false;
            this.url0x1.Text = "Find Group";
            this.url0x1.UseVisualStyleBackColor = true;
            this.url0x1.Click += new System.EventHandler(this.url0x1_Click);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.URLDelete);
            this.groupBox2.Controls.Add(this.URLList);
            this.groupBox2.Controls.Add(this.label11);
            this.groupBox2.Controls.Add(this.URLAppend);
            this.groupBox2.Controls.Add(this.label12);
            this.groupBox2.Controls.Add(this.URLText);
            this.groupBox2.Controls.Add(this.GidDelete);
            this.groupBox2.Controls.Add(this.GidList);
            this.groupBox2.Controls.Add(this.label10);
            this.groupBox2.Controls.Add(this.GidAppend);
            this.groupBox2.Controls.Add(this.label9);
            this.groupBox2.Controls.Add(this.GidText);
            this.groupBox2.Location = new System.Drawing.Point(59, 72);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(400, 152);
            this.groupBox2.TabIndex = 23;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "gid選項";
            // 
            // URLDelete
            // 
            this.URLDelete.Location = new System.Drawing.Point(257, 117);
            this.URLDelete.Name = "URLDelete";
            this.URLDelete.Size = new System.Drawing.Size(75, 23);
            this.URLDelete.TabIndex = 25;
            this.URLDelete.TabStop = false;
            this.URLDelete.Text = "Delete";
            this.URLDelete.UseVisualStyleBackColor = true;
            this.URLDelete.Click += new System.EventHandler(this.URLDelete_Click);
            // 
            // URLList
            // 
            this.URLList.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.URLList.FormattingEnabled = true;
            this.URLList.Location = new System.Drawing.Point(246, 51);
            this.URLList.Name = "URLList";
            this.URLList.Size = new System.Drawing.Size(100, 20);
            this.URLList.TabIndex = 24;
            this.URLList.SelectedIndexChanged += new System.EventHandler(this.URLList_SelectedIndexChanged);
            // 
            // label11
            // 
            this.label11.AutoSize = true;
            this.label11.Location = new System.Drawing.Point(197, 54);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(45, 12);
            this.label11.TabIndex = 23;
            this.label11.Text = "URLList";
            // 
            // URLAppend
            // 
            this.URLAppend.Location = new System.Drawing.Point(257, 87);
            this.URLAppend.Name = "URLAppend";
            this.URLAppend.Size = new System.Drawing.Size(75, 23);
            this.URLAppend.TabIndex = 22;
            this.URLAppend.TabStop = false;
            this.URLAppend.Text = "Append";
            this.URLAppend.UseVisualStyleBackColor = true;
            this.URLAppend.Click += new System.EventHandler(this.URLAppend_Click);
            // 
            // label12
            // 
            this.label12.AutoSize = true;
            this.label12.Location = new System.Drawing.Point(207, 25);
            this.label12.Name = "label12";
            this.label12.Size = new System.Drawing.Size(28, 12);
            this.label12.TabIndex = 21;
            this.label12.Text = "URL";
            // 
            // URLText
            // 
            this.URLText.Location = new System.Drawing.Point(246, 21);
            this.URLText.Name = "URLText";
            this.URLText.Size = new System.Drawing.Size(100, 22);
            this.URLText.TabIndex = 20;
            this.URLText.KeyDown += new System.Windows.Forms.KeyEventHandler(this.URLText_KeyDown);
            // 
            // GidDelete
            // 
            this.GidDelete.Location = new System.Drawing.Point(70, 117);
            this.GidDelete.Name = "GidDelete";
            this.GidDelete.Size = new System.Drawing.Size(75, 23);
            this.GidDelete.TabIndex = 19;
            this.GidDelete.TabStop = false;
            this.GidDelete.Text = "Delete";
            this.GidDelete.UseVisualStyleBackColor = true;
            this.GidDelete.Click += new System.EventHandler(this.GidDelete_Click);
            // 
            // GidList
            // 
            this.GidList.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.GidList.FormattingEnabled = true;
            this.GidList.Location = new System.Drawing.Point(59, 51);
            this.GidList.Name = "GidList";
            this.GidList.Size = new System.Drawing.Size(100, 20);
            this.GidList.TabIndex = 18;
            this.GidList.SelectedIndexChanged += new System.EventHandler(this.GidList_SelectedIndexChanged);
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Location = new System.Drawing.Point(10, 54);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(39, 12);
            this.label10.TabIndex = 17;
            this.label10.Text = "GidList";
            // 
            // GidAppend
            // 
            this.GidAppend.Location = new System.Drawing.Point(70, 87);
            this.GidAppend.Name = "GidAppend";
            this.GidAppend.Size = new System.Drawing.Size(75, 23);
            this.GidAppend.TabIndex = 16;
            this.GidAppend.TabStop = false;
            this.GidAppend.Text = "Append";
            this.GidAppend.UseVisualStyleBackColor = true;
            this.GidAppend.Click += new System.EventHandler(this.GidAppend_Click);
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(20, 25);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(22, 12);
            this.label9.TabIndex = 15;
            this.label9.Text = "Gid";
            // 
            // GidText
            // 
            this.GidText.Location = new System.Drawing.Point(59, 21);
            this.GidText.Name = "GidText";
            this.GidText.Size = new System.Drawing.Size(100, 22);
            this.GidText.TabIndex = 14;
            this.GidText.KeyDown += new System.Windows.Forms.KeyEventHandler(this.GidText_KeyDown);
            // 
            // Urls
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.groupBox5);
            this.Controls.Add(this.groupBox4);
            this.Controls.Add(this.groupBox3);
            this.Name = "Urls";
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
        public System.Windows.Forms.Button url0x8;
        public System.Windows.Forms.Button url0x4;
        public System.Windows.Forms.Button url0x2;
        public System.Windows.Forms.Button url0x1;
        private System.Windows.Forms.GroupBox groupBox2;
        public System.Windows.Forms.Button GidDelete;
        private System.Windows.Forms.ComboBox GidList;
        private System.Windows.Forms.Label label10;
        public System.Windows.Forms.Button GidAppend;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.TextBox GidText;
        public System.Windows.Forms.Button URLDelete;
        private System.Windows.Forms.ComboBox URLList;
        private System.Windows.Forms.Label label11;
        public System.Windows.Forms.Button URLAppend;
        private System.Windows.Forms.Label label12;
        private System.Windows.Forms.TextBox URLText;
    }
}
