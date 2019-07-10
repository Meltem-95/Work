#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

class UAV
{
	public:
	char name;
	bool is_landing {false};
	bool is_takeoff = false;
	void takeoff();
};
class Drone : public UAV
{
	public:
	Drone(char drone_name);
	bool takeoff()
	{
		if(is_landing == true)
			return false;
		else if(is_landing == false)
			is_takeoff = true;
		    return true;
	}
	
};
Drone::Drone(char drone_name)
{
	name = drone_name;	
};
int main(int argc, char** argv) {
	return 0;
}
