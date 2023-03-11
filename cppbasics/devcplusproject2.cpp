// Created: Jan 27, 2017 | Edited: Mar 11, 2023

#include <iostream>
using namespace std;
int main ()
{
	int x, y, z;
	cout << "Xosh gorduk. Gelin deyishenlere verilecek qiymetlerle bir sira emelleri yerine yetirek.";
	x = 5;
	y = 2;
	z = x + y;
	cout << "\nEdedleri topladiq."<<" Cavab = ";
	cout << z;
	z = x-y;
	cout << "\nBirinci ededden ikinci ededi chixdiq."<<" Cavab = ";
	cout << z;
	cout << "\nChixma emelinden aldighimiz cavabi beshe bolduk."<<" Cavab = ";
	cout << z/5;
	z = x/y;
	cout << "\nBirinci ededi ikinci edede bolduk."<<" Cavab = ";
	cout << z;
	z = x * y;
	cout << "\nEdedleri bir-birine vurduq."<<" Cavab = ";
	cout << z;
	cout << "\n(x+y)/(x-y) ifadesini hell etdik."<<" Cavab = ";
	cout << (x + y) / ( x - y);
}
