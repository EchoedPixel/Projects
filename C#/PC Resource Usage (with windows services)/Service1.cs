using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Net.Mail;
using System.Reflection;
using System.ServiceProcess;
using System.Text;
using System.Threading.Tasks;
using System.Timers;

namespace MyFirstService
{
    public partial class Service1 : ServiceBase
    {
        PerformanceCounter CPUCounter = new PerformanceCounter("Processor","% Processor Time","_Total");
        PerformanceCounter RAMCounter = new PerformanceCounter("Memory", "Available MBytes");
        PerformanceCounter DISKRCounter = new PerformanceCounter("LogicalDisk", "Avg. Disk Bytes/Read", "_Total");
        PerformanceCounter DISKWCounter = new PerformanceCounter("LogicalDisk", "Avg. Disk Bytes/Write", "_Total");
        //PerformanceCounter NETCounter = new PerformanceCounter("Network Interface", "% Network Utilization", "_Total");

        Timer timer = new Timer();

        public Service1()
        {
            InitializeComponent();
        }

        private void SendEmail(string fileName)
        {
            string fromEmail = "senderemail@domain.com";
            string toEmail = "recieveremail@domain.com";
            string subject = "System Information";
            string body = "Please find the attached system information.";

            using (MailMessage mail = new MailMessage(fromEmail, toEmail))
            {
                mail.Subject = subject;
                mail.Body = body;

                mail.Attachments.Add(new Attachment(fileName));

                using (SmtpClient smtp = new SmtpClient("smtp.example.com", 587))
                {
                    smtp.Credentials = new System.Net.NetworkCredential("senderemail@example.com", "sender password");
                    smtp.EnableSsl = true;
                    smtp.Send(mail);
                }
            }
        }

        protected override void OnStart(string[] args)
        {
            WriteToFile("Service is started at " + DateTime.Now);
            timer.Elapsed += new ElapsedEventHandler(OnElapsedTime);
            timer.Interval = 1000; //number in milisecinds
            timer.Enabled = true;
        }
        protected override void OnStop()
        {
            WriteToFile("Service is stopped at " + DateTime.Now);
        }
        private void OnElapsedTime(object source, ElapsedEventArgs e)
        {
            WriteToFile("Service is recall at " + DateTime.Now);
            float CPU = CPUCounter.NextValue();
            float RAM = RAMCounter.NextValue();
            float DISKR = DISKRCounter.NextValue()/1000000; // the devide to convert it from byte to mb
            float DISKW = DISKWCounter.NextValue()/1000000; // the devide to convert it from byte to mb
            //double Net = NETCounter.NextValue()/1000000; // the devide to convert it from byte to mb
            WriteToFile($"CPU Usage: {(int)CPU}%");
            WriteToFile($"RAM Usage: {RAM}MB");
            WriteToFile($"DISK Read Usage: {DISKR}MB/Sec");
            WriteToFile($"DISK Write Usage: {DISKW}MB/Sec \n");
            //WriteToFile($"Network Total Usage: {Net}MB");
        }
        public void WriteToFile(string Message)
        {
            string path = AppDomain.CurrentDomain.BaseDirectory + "\\Logs";
            if (!Directory.Exists(path))
            {
                Directory.CreateDirectory(path);
            }
            string filepath = AppDomain.CurrentDomain.BaseDirectory + "\\Logs\\ServiceLog_" + DateTime.Now.Date.ToShortDateString().Replace('/', '_') + ".txt";
            if (!File.Exists(filepath))
            {
                // Create a file to write to.
                using (StreamWriter sw = File.CreateText(filepath))
                {
                    sw.WriteLine(Message);
                    SendEmail(filepath);
                }
            }
            else
            {
                using (StreamWriter sw = File.AppendText(filepath))
                {
                    sw.WriteLine(Message);
                    SendEmail(filepath);
                }
            }
        }
    }
}