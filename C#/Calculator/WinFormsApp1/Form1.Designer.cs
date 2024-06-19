namespace WinFormsApp1
{
    partial class Calculator
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Calculator));
            SaveButton = new Button();
            CloseButton = new Button();
            textBox1 = new TextBox();
            button1 = new Button();
            button2 = new Button();
            button3 = new Button();
            button4 = new Button();
            button5 = new Button();
            button6 = new Button();
            button7 = new Button();
            button9 = new Button();
            N1 = new Button();
            button8 = new Button();
            button11 = new Button();
            MinusBTN = new Button();
            button13 = new Button();
            button14 = new Button();
            button15 = new Button();
            button10 = new Button();
            button12 = new Button();
            SuspendLayout();
            // 
            // SaveButton
            // 
            SaveButton.BackColor = SystemColors.ButtonFace;
            SaveButton.Location = new Point(239, 586);
            SaveButton.Margin = new Padding(4);
            SaveButton.Name = "SaveButton";
            SaveButton.Size = new Size(175, 72);
            SaveButton.TabIndex = 0;
            SaveButton.Text = "8";
            SaveButton.UseVisualStyleBackColor = false;
            SaveButton.Click += button1_Click;
            // 
            // CloseButton
            // 
            CloseButton.Location = new Point(916, 702);
            CloseButton.Margin = new Padding(4);
            CloseButton.Name = "CloseButton";
            CloseButton.Size = new Size(175, 66);
            CloseButton.TabIndex = 1;
            CloseButton.Text = "close";
            CloseButton.UseVisualStyleBackColor = true;
            CloseButton.Click += CloseButton_Click;
            // 
            // textBox1
            // 
            textBox1.Location = new Point(69, 59);
            textBox1.Margin = new Padding(4);
            textBox1.Multiline = true;
            textBox1.Name = "textBox1";
            textBox1.Size = new Size(969, 193);
            textBox1.TabIndex = 2;
            // 
            // button1
            // 
            button1.BackColor = SystemColors.ButtonFace;
            button1.Location = new Point(15, 471);
            button1.Margin = new Padding(4);
            button1.Name = "button1";
            button1.Size = new Size(175, 72);
            button1.TabIndex = 3;
            button1.Text = "4";
            button1.UseVisualStyleBackColor = false;
            button1.Click += button1_Click_1;
            // 
            // button2
            // 
            button2.BackColor = SystemColors.ButtonFace;
            button2.Location = new Point(239, 355);
            button2.Margin = new Padding(4);
            button2.Name = "button2";
            button2.Size = new Size(175, 72);
            button2.TabIndex = 4;
            button2.Text = "2";
            button2.UseVisualStyleBackColor = false;
            button2.Click += button2_Click;
            // 
            // button3
            // 
            button3.BackColor = SystemColors.ButtonFace;
            button3.Location = new Point(15, 586);
            button3.Margin = new Padding(4);
            button3.Name = "button3";
            button3.Size = new Size(175, 72);
            button3.TabIndex = 5;
            button3.Text = "7";
            button3.UseVisualStyleBackColor = false;
            button3.Click += button3_Click;
            // 
            // button4
            // 
            button4.BackColor = SystemColors.ButtonFace;
            button4.Location = new Point(239, 702);
            button4.Margin = new Padding(4);
            button4.Name = "button4";
            button4.Size = new Size(175, 72);
            button4.TabIndex = 6;
            button4.Text = ".";
            button4.UseVisualStyleBackColor = false;
            button4.Click += button4_Click;
            // 
            // button5
            // 
            button5.BackColor = SystemColors.ButtonFace;
            button5.Location = new Point(471, 355);
            button5.Margin = new Padding(4);
            button5.Name = "button5";
            button5.Size = new Size(175, 72);
            button5.TabIndex = 7;
            button5.Text = "3";
            button5.UseVisualStyleBackColor = false;
            button5.Click += button5_Click;
            // 
            // button6
            // 
            button6.BackColor = SystemColors.ButtonFace;
            button6.Location = new Point(239, 470);
            button6.Margin = new Padding(4);
            button6.Name = "button6";
            button6.Size = new Size(175, 72);
            button6.TabIndex = 8;
            button6.Text = "5";
            button6.UseVisualStyleBackColor = false;
            button6.Click += button6_Click;
            // 
            // button7
            // 
            button7.BackColor = SystemColors.ButtonFace;
            button7.Location = new Point(15, 702);
            button7.Margin = new Padding(4);
            button7.Name = "button7";
            button7.Size = new Size(175, 72);
            button7.TabIndex = 9;
            button7.Text = "0";
            button7.UseVisualStyleBackColor = false;
            button7.Click += button7_Click;
            // 
            // button9
            // 
            button9.BackColor = SystemColors.ButtonFace;
            button9.Location = new Point(471, 470);
            button9.Margin = new Padding(4);
            button9.Name = "button9";
            button9.Size = new Size(175, 72);
            button9.TabIndex = 11;
            button9.Text = "6";
            button9.UseVisualStyleBackColor = false;
            button9.Click += button9_Click;
            // 
            // N1
            // 
            N1.BackColor = SystemColors.ButtonFace;
            N1.Location = new Point(15, 355);
            N1.Margin = new Padding(4);
            N1.Name = "N1";
            N1.Size = new Size(175, 72);
            N1.TabIndex = 13;
            N1.Text = "1";
            N1.UseVisualStyleBackColor = false;
            N1.Click += button11_Click;
            // 
            // button8
            // 
            button8.BackColor = SystemColors.ButtonFace;
            button8.Location = new Point(471, 586);
            button8.Margin = new Padding(4);
            button8.Name = "button8";
            button8.Size = new Size(175, 72);
            button8.TabIndex = 14;
            button8.Text = "9";
            button8.UseVisualStyleBackColor = false;
            button8.Click += button8_Click;
            // 
            // button11
            // 
            button11.BackColor = SystemColors.ButtonFace;
            button11.Location = new Point(916, 471);
            button11.Margin = new Padding(4);
            button11.Name = "button11";
            button11.Size = new Size(175, 72);
            button11.TabIndex = 15;
            button11.Text = "+";
            button11.UseVisualStyleBackColor = false;
            button11.Click += button11_Click_1;
            // 
            // MinusBTN
            // 
            MinusBTN.BackColor = SystemColors.ButtonFace;
            MinusBTN.Location = new Point(701, 470);
            MinusBTN.Margin = new Padding(4);
            MinusBTN.Name = "MinusBTN";
            MinusBTN.Size = new Size(175, 72);
            MinusBTN.TabIndex = 16;
            MinusBTN.Text = "-";
            MinusBTN.UseVisualStyleBackColor = false;
            MinusBTN.Click += button12_Click;
            // 
            // button13
            // 
            button13.BackColor = SystemColors.ButtonFace;
            button13.Location = new Point(701, 586);
            button13.Margin = new Padding(4);
            button13.Name = "button13";
            button13.Size = new Size(175, 72);
            button13.TabIndex = 17;
            button13.Text = "x";
            button13.UseVisualStyleBackColor = false;
            button13.Click += button13_Click;
            // 
            // button14
            // 
            button14.BackColor = SystemColors.ButtonFace;
            button14.Location = new Point(916, 586);
            button14.Margin = new Padding(4);
            button14.Name = "button14";
            button14.Size = new Size(175, 72);
            button14.TabIndex = 18;
            button14.Text = "÷";
            button14.UseVisualStyleBackColor = false;
            button14.Click += button14_Click;
            // 
            // button15
            // 
            button15.BackColor = SystemColors.ButtonFace;
            button15.Location = new Point(471, 702);
            button15.Margin = new Padding(4);
            button15.Name = "button15";
            button15.Size = new Size(175, 72);
            button15.TabIndex = 19;
            button15.Text = "=";
            button15.UseVisualStyleBackColor = false;
            button15.Click += button15_Click;
            // 
            // button10
            // 
            button10.BackColor = SystemColors.ButtonFace;
            button10.Location = new Point(701, 355);
            button10.Margin = new Padding(4);
            button10.Name = "button10";
            button10.Size = new Size(390, 72);
            button10.TabIndex = 20;
            button10.Text = "C";
            button10.UseVisualStyleBackColor = false;
            button10.Click += button10_Click_1;
            // 
            // button12
            // 
            button12.BackColor = SystemColors.ButtonFace;
            button12.Location = new Point(701, 702);
            button12.Margin = new Padding(4);
            button12.Name = "button12";
            button12.Size = new Size(175, 72);
            button12.TabIndex = 21;
            button12.Text = "DEL.";
            button12.UseVisualStyleBackColor = false;
            button12.Click += button12_Click_1;
            // 
            // Calculator
            // 
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            BackgroundImage = Properties.Resources.Background_Calculator;
            ClientSize = new Size(1116, 836);
            Controls.Add(button12);
            Controls.Add(button10);
            Controls.Add(button15);
            Controls.Add(button14);
            Controls.Add(button13);
            Controls.Add(MinusBTN);
            Controls.Add(button11);
            Controls.Add(button8);
            Controls.Add(N1);
            Controls.Add(button9);
            Controls.Add(button7);
            Controls.Add(button6);
            Controls.Add(button5);
            Controls.Add(button4);
            Controls.Add(button3);
            Controls.Add(button2);
            Controls.Add(button1);
            Controls.Add(textBox1);
            Controls.Add(CloseButton);
            Controls.Add(SaveButton);
            Font = new Font("Segoe UI", 11F, FontStyle.Regular, GraphicsUnit.Point);
            FormBorderStyle = FormBorderStyle.FixedSingle;
            Icon = (Icon)resources.GetObject("$this.Icon");
            Margin = new Padding(4);
            Name = "Calculator";
            Text = "Calculator";
            Load += Form1_Load;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button SaveButton;
        private Button CloseButton;
        private TextBox textBox1;
        private Button button1;
        private Button button2;
        private Button button3;
        private Button button4;
        private Button button5;
        private Button button6;
        private Button button7;
        private Button button9;
        private Button N1;
        private Button button8;
        private Button button11;
        private Button MinusBTN;
        private Button button13;
        private Button button14;
        private Button button15;
        private Button button10;
        private Button button12;
    }
}