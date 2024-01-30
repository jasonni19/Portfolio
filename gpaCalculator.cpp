#include <iomanip>
#include <iostream>
#include <windows.h>

using namespace std;

void calcGPA(string letter, int& classNum, int numUnits, int& totalUnits, double& gpaPoints);
void printGPA(int classNum, int totalUnits, double& gpaPoints);

const double GRADES[12][6] = { 
	{4.0,8.0,12.0,16.0,20.0,24.0},
	{3.7,7.4,11.1,14.8,18.5,22.2},
	{3.3,6.6,9.9,13.2,16.5,19.8},
	{3.0,6.0,9.0,12.0,15.0,18.0},
	{2.7,5.4,8.1,10.8,13.5,16.2},
	{2.3,4.6,6.9,9.2,11.5,13.8},
	{2.0,4.0,6.0,8.0,10.0,12.0},
	{1.7,3.4,5.1,6.8,8.5,10.2},
	{1.3,2.6,3.9,5.2,6.5,7.8},
	{1.0,2.0,3.0,4.0,5.0,6.0},
	{0.7,1.4,2.1,2.8,3.5,4.2},
	{0.0,0.0,0.0,0.0,0.0,0.0}

};

int main() {

	string letter;
	int classNum = 1;
	int numUnits = 0;
	int totalUnits = 0;
	double gpaPoints = 0;

	cout << "WELCOME TO JASON'S " << endl;
	cout << R"(   __  __________    ___       __________  ___       _________    __    ________  ____    ___  __________  ____ 
  / / / / ____/ /   /   |     / ____/ __ \/   |     / ____/   |  / /   / ____/ / / / /   /   |/_  __/ __ \/ __ \
 / / / / /   / /   / /| |    / / __/ /_/ / /| |    / /   / /| | / /   / /   / / / / /   / /| | / / / / / / /_/ /
/ /_/ / /___/ /___/ ___ |   / /_/ / ____/ ___ |   / /___/ ___ |/ /___/ /___/ /_/ / /___/ ___ |/ / / /_/ / _, _/ 
\____/\____/_____/_/  |_|   \____/_/   /_/  |_|   \____/_/  |_/_____/\____/\____/_____/_/  |_/_/  \____/_/ |_|  
                                                                                                                )" << endl;
	cout << "The valid units for each UCLA class are 1,2,3,4,5,6" << endl;
	cout << "The valid letter grades at UCLA are the following: A, A-, B+, B, B-, C+, C, C-, D+, D, D-, F" << endl;
	cout << "--------------------------------------------------------------------------------------------" << endl;

	calcGPA(letter, classNum, numUnits, totalUnits, gpaPoints);
	printGPA(classNum,totalUnits,gpaPoints);

	return 0;
}

void calcGPA(string letter, int& classNum, int numUnits, int& totalUnits, double& gpaPoints) {
	while (true) {

		cout << "Class " << classNum << ": Enter the number of units of the class proceeded with your letter grade, enter 0 to stop. (Ex. 4A-)" << endl;

		cin >> numUnits;

		if (numUnits == 0) {
			classNum -= 1;
			break;
		}

		if (numUnits < 1 || numUnits > 6) {
			cin.ignore(1000, '\n');
			cout << "TRY AGAIN, INVALID NUMBER OF UNITS" << endl;
			cout << "--------------------------------------------------------------------------------------------" << endl;
			continue;
		}

		cin >> letter;

		totalUnits += numUnits;

		if (letter == "A" || letter == "a") {
			gpaPoints += GRADES[0][numUnits - 1];
		}

		else if (letter == "A-" || letter == "a-") {
			gpaPoints += GRADES[1][numUnits - 1];
		}

		else if (letter == "B+" || letter == "b+") {
			gpaPoints += GRADES[2][numUnits - 1];
		}

		else if (letter == "B" || letter == "b") {
			gpaPoints += GRADES[3][numUnits - 1];
		}

		else if (letter == "B-" || letter == "b-") {
			gpaPoints += GRADES[4][numUnits - 1];
		}

		else if (letter == "C+" || letter == "c+") {
			gpaPoints += GRADES[5][numUnits - 1];
		}

		else if (letter == "C" || letter == "c") {
			gpaPoints += GRADES[6][numUnits - 1];
		}

		else if (letter == "C-" || letter == "c-") {
			gpaPoints += GRADES[7][numUnits - 1];
		}

		else if (letter == "D+" || letter == "d+") {
			gpaPoints += GRADES[8][numUnits - 1];
		}

		else if (letter == "D" || letter == "d") {
			gpaPoints += GRADES[9][numUnits - 1];
		}

		else if (letter == "D-" || letter == "d-") {
			gpaPoints += GRADES[10][numUnits - 1];
		}

		else if (letter == "F" || letter == "f") {
			gpaPoints += GRADES[11][numUnits - 1];
		}

		else {
			cout << "NOT A VALID LETTER LETTER GRADE, TRY AGAIN" << endl;
			cout << "--------------------------------------------------------------------------------------------" << endl;
			if (classNum != 1) {
				classNum -= 1;
			}
			totalUnits -= numUnits;
			cin.ignore(1000, '\n');
			continue;
		}
		classNum++;
		cout << endl;

	}
}

void printGPA(int classNum, int totalUnits, double &gpaPoints) {
	cout << "--------------------------------------------------------------------------------------------" << endl;

	if (classNum != 0) {
		cout << "Calculating..." << endl;
		Sleep(2000);

		cout << fixed << setprecision(2) << "Your GPA this quarter is " << gpaPoints / totalUnits << "." << endl;

		if (classNum != 1) {
			cout << "You took " << classNum << " classes." << endl;
		}
		else {
			cout << "You took " << classNum << " class." << endl;
		}
	}

	else {
		cout << "You did not input any classes. If you neglected to input a number of units before a letter grade, run the program again." << endl;
	}
}


