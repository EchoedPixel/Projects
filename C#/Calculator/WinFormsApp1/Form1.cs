using Microsoft.VisualBasic.ApplicationServices;

namespace WinFormsApp1
{
    public partial class Calculator : Form
    {
        private decimal valueFirst = 0.0m;
        private decimal valueSecond = 0.0m;
        private decimal valueThird = 0.0m;
        private decimal Result = 0.0m;
        private string operators = "+";


        public Calculator()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            textBox1.Text = textBox1.Text + "8";

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void CloseButton_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button11_Click(object sender, EventArgs e)
        {
            textBox1.Text = textBox1.Text + "1";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            textBox1.Text = textBox1.Text + "4";
        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            textBox1.Text = textBox1.Text + "4";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            textBox1.Text = textBox1.Text + "6";

        }

        private void button3_Click(object sender, EventArgs e)
        {
            textBox1.Text = textBox1.Text + "7";

        }

        private void button15_Click(object sender, EventArgs e)
        {
            switch (operators)
            {
                case "-":
                    valueSecond = decimal.Parse(textBox1.Text);
                    Result = valueFirst - valueSecond;
                    textBox1.Text = Result.ToString();
                    break;
                case "+":
                    valueSecond = decimal.Parse(textBox1.Text);
                    Result = valueFirst + valueSecond;
                    textBox1.Text = Result.ToString();
                    break;
                case "X":
                    valueSecond = decimal.Parse(textBox1.Text);
                    Result = valueFirst * valueSecond;
                    textBox1.Text = Result.ToString();
                    break;
                case "÷":
                    valueSecond = decimal.Parse(textBox1.Text);
                    Result = valueFirst / valueSecond;
                    textBox1.Text = Result.ToString();
                    break;

            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox1.Text = textBox1.Text + "2";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            textBox1.Text = textBox1.Text + "3";
        }

        private void button11_Click_1(object sender, EventArgs e)
        {
            valueFirst = decimal.Parse(textBox1.Text);
            textBox1.Clear();
            operators = "+";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            textBox1.Text = textBox1.Text + "5";

        }

        private void button8_Click(object sender, EventArgs e)
        {
            textBox1.Text = textBox1.Text + "9";

        }

        private void button7_Click(object sender, EventArgs e)
        {
            textBox1.Text = textBox1.Text + "0";

        }

        private void button4_Click(object sender, EventArgs e)
        {
            textBox1.Text = textBox1.Text + ".";

        }

        private void button12_Click(object sender, EventArgs e)
        {
            valueFirst = decimal.Parse(textBox1.Text);
            textBox1.Clear();
            operators = "-";
        }

        private void button13_Click(object sender, EventArgs e)
        {
            valueFirst = decimal.Parse(textBox1.Text);
            textBox1.Clear();
            operators = "X";
        }

        private void button14_Click(object sender, EventArgs e)
        {
            valueFirst = decimal.Parse(textBox1.Text);
            textBox1.Clear();
            operators = "÷";
        }

        private void button10_Click_1(object sender, EventArgs e)
        {
            valueFirst = 0.0m;
            valueSecond = 0.0m;
            textBox1.Clear();
        }

        private void button12_Click_1(object sender, EventArgs e)
        {
            textBox1.Text = textBox1.Text.Remove(textBox1.Text.Length - 1);
        }
    }
}