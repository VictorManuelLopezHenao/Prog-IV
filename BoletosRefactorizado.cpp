#include<iostream>
using namespace std;

int sumamitad(int boleto[], int inicio, int final);

int main(){
    int tamañoBoleto;
    int boleto[30];

    cout<<"\n\tVerificacion de boletos ";
    cout<<"\n\nDigite el tamaño del boleto: "; cin>>tamañoBoleto;

    if(tamañoBoleto % 2 != 0){
        cout<<"\nEl tamaño del boleto debe ser par\n";
        return 0;
    }
    
    cout << "\nDe esta manera: 1 2 3 4 5..." << endl;
    cout << "Ingrese los dígitos del boleto: ";
    for (int i = 0; i < tamañoBoleto; i++) {
        cin >> boleto[i];
    }

    int mitad = tamañoBoleto / 2;
    int primeramitad = sumamitad(boleto, 0, mitad);


    int segundamitad = 0;
    for(int i = tamañoBoleto - 1; i>=mitad; i--){
        segundamitad += boleto[i];
    }

    if(primeramitad == segundamitad){
        cout<<endl<<primeramitad<<" "<<segundamitad;
        cout<<"\nTicket valido";
    } else {
        cout<<"\nTicket no valido";
    }

    return 0;
}

int sumamitad(int boleto[], int inicio, int final){
    int suma = 0;
    for(int i = inicio; i<final; i++){
        suma += boleto[i];
    }
    return suma;
}
