using System;

namespace FinalHomework
{
    internal class Program
    {
        static void Main(string[] args)
        {
            static void Changestr(string[] strings)
        {
            
            int count = 0;
            foreach(var item in strings)
            {
                if (item.Length <= 3)
                {
                   
                    count++;
                }
            }
            string[] NewStrings = new string[count];
            count = 0;
            foreach (var item in strings)
            {
                if (item.Length <=3)
                {
                    NewStrings[count] = item;
                    Console.WriteLine(NewStrings[count]);
                    count++;
                }
            }
           
         
        }    
           
        }
    }
}