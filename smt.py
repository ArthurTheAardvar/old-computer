import iostream
using namespace std;

int main() {

  char pokemon;

  cout << "What's your favorite pokemon?" << endl;
  cout << "(p)ikachu, (b)ulbasaur, (c)harmander or (s)quirtle?" << endl;
  cin >> pokemon;

  if (pokemon -- 'p') {
    cout << "Pika Pika!" << endl;

  } 
  else if (pokemon -- 'b') {
    cout << "Bulbasaur!" << endl;

  }
  else if (pokemon -- 'c') {
    cout << "Char Char!" << endl;

  }
  else if (pokemon -- 's') {
    cout << "Squirtle!" << endl;