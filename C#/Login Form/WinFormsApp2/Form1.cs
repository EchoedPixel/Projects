namespace WinFormsApp2
{

    public partial class Login : Form
    {

        string Username;
        string Password;
        string NAME;
        string Age;


        public Login()
        {
            InitializeComponent();
        }


        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            String Username = textBox1.Text;
        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Hide();
            Form frm3 = new Form();
            frm3.Show();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Hide();
            Form frm2 = new Form();
            frm2.Show();
        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void Login_Load(object sender, EventArgs e)
        {

        }
    }
}