/*
    信息安全实验5：RSA现代非对称加密算法

    Alice的公钥为
        （N , e） = （33，3）
    加密 M = 19 求密文C
    加密 M = 25 求数字签名的值S 

*/

#include <cmath>
#include <iostream>

using namespace std;

void RSA(int N, int e, int d, int M, int mode)
{
    uint64_t C, S;
    if (mode == 1)
    {
        C = pow(M, e);
        C = C % N;

        cout << "公钥加密密文为：" << C << endl;
    }

    if (mode == 2)
    {
        S = pow(M, d);
        S = S % N;

        cout << "私钥数字签名为：" << S << endl;
    }
}

int main(int argc, char const *argv[])
{
    int mode;

    //公钥和d
    int N, e, d, M, C, S;

    cout << "RSA加密算法实现加密和数字签名" << endl;

    cout << "请输入公钥 N,e 空格分开" << endl;
    cin >> N;
    cin >> e;
    cout << "请输入私钥d" << endl;
    cin >> d;

    cout << "请输入明文：" << endl;
    cin >> M;

    cout << "请选择方式：1.公钥加密 2.私钥数字签名" << endl;
    cin >> mode;

    cout << "正在加密中，请稍等。。。。。" << endl;

    RSA(N, e, d, M, mode);

    return 0;
}