/*
    Programa: Jogo da velha (TicTacToe);
    Versão: 2.0;
    data: 17/04/2022.
*/
#include <iostream>

using namespace std;
//função que verifica se o jogador de jogada v ganhou.
bool ganhou(char m[5][5], char v){
    //Verifição das linhas
    if(m[0][0] == v && m[0][2] == v && m[0][4] == v || m[2][0] == v && m[2][2] == v && m[2][4] == v || m[4][0] == v && m[4][2] == v && m[4][4] == v){
        return true;
    }
    //Verifição das colunas
    if(m[0][0] == v && m[2][0] == v && m[4][0] == v || m[0][2] == v && m[2][2] == v && m[4][2] == v || m[0][4] == v && m[2][4] == v && m[4][4] == v){
        return true;
    }
    //Verifição das diagonais
    if(m[0][0] == v && m[2][2] == v && m[4][4] == v || m[0][4] == v && m[2][2] == v && m[4][0] == v){
        return true;
    }
    return false;
}

int main(){
    //Declaração da grade da velha e da variável jogada.
    char s, v, velha[5][5] = {{'1', '|', '2', '|', '3'}, {'-', ' ', '-', ' ', '-'}, {'4', '|', '5', '|', '6'}, {'-', ' ', '-', ' ', '-'}, {'7', '|', '8', '|', '9'}};
    int cond = 1, c = 0, vencedor = 0, E[9] = {};
    string J, J1, J2;
    //Leitura do primeiro jogador.
    cout << "Insira o nome do jogador 1 (X): ";
    getline(cin, J1);
    cout << endl;
    //Leitura do segundo jogador.
    cout << "Insira o nome do jogador 2 (O): ";
    getline(cin, J2);
    cout << endl;
    //Nome base caso nenhum tenha sido digitado.
    if(J1 == "") J1 = "Jogador 1";
    if(J2 == "") J2 = "Jogador 2";
    //Impressão da grade da velha
    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 5; j++){
            for(int k = 0; k < 5; k++){
                cout << velha[j][k];
            }
            cout << endl;
        }
        cout << endl;
        //Leitura da jogada
        if(c % 2 == 0){
            s = 'X';
            J = J1;
        }
        else{
            s = 'O';
            J = J2;
        }do{
            cout << J << ", sua jogada: ";
            cin >> v;
            cout << endl;
            v = (int) v - 48;
            if(v <= 0 || v > 9 || E[v-1] == 1){
                cond = 0;
                cout << "Jogada inválida! Digite outra opção!\n";
            }else{
                E[v-1] = 1;
                cond = 1;
            }
        }while(cond == 0);
        switch(v){
            case 1:
                velha[0][0] = s;
                break;
            case 2:
                velha[0][2] = s;
                break;
            case 3:
                velha[0][4] = s;
                break;
            case 4:
                velha[2][0] = s;
                break;
            case 5:
                velha[2][2] = s;
                break;
            case 6:
                velha[2][4] = s;
                break;
            case 7:
                velha[4][0] = s;
                break;
            case 8:
                velha[4][2] = s;
                break;
            case 9:
                velha[4][4] = s;
                break;     
        }
        //Verificar se ganhou
        if(ganhou(velha, s)){
            vencedor = c % 2 + 1;
            for(int j = 0; j < 5; j++){
                for(int k = 0; k < 5; k++){
                    cout << velha[j][k];
                }
            cout << endl;
            }
            cout << endl;
            break;
        }
        c++;
    }
    if(vencedor == 1) cout << J1 << " é o vencedor!\n";
    else if(vencedor == 2) cout << J2 << " é o vencedor!\n";
    else cout << "Deu velha! (Empate)\n";
    return 0;
}