#include <cstdio>

#define ABS(a) ((a)>=0?(a):-(a))

int N;
int Answer;

int B[12][12];
void place(int rest, int row) {
    int col = rest - 1;
    // .... .... ..
    for (int i = 0; i < N; i++) {
        if (B[row][i] != -1) return;
        if (B[i][col] != -1) return;
    }

    // ... .... ..
    for (int i = 1; i < N; i++) {
        if (row + i < N && col + i < N && B[row + i][col + i] != -1) return;
        if (row + i < N && col - i >= 0 && B[row + i][col - i] != -1) return;
        if (row - i >= 0 && col + i < N && B[row - i][col + i] != -1) return;
        if (row - i >= 0 && col - i >= 0 && B[row - i][col - i] != -1) return;
    }
    if (rest == 1) {
        Answer++;
        return;
    }

    B[row][col] = rest;
    for (int i = 0; i < N; i++) {
        place(rest-1, i);
    }
    B[row][col] = -1;
}

int L[12][2]; // [][0] ..., [][1] ...
int iL;       // L. index
void place1(int rest, int row) {
    int col = rest - 1;
    // .... .... ..
    for (int i = 0; i <= iL; i++) {
        if (row == L[i][0] || col == L[i][1]) return;
    }

    // ... .... ..
    for (int i = 0; i <= iL; i++) {
        if (ABS(row - L[i][0]) == ABS(col - L[i][1])) return;
    }
    if (rest == 1) {
        Answer++;
        return;
    }

    iL++;
    L[iL][0] = row;
    L[iL][1] = col;
    for (int i = 0; i < N; i++) {
        place1(rest - 1, i);
    }
    iL--;
}

int main() {
    int test_case, T;

    //freopen("sample_input.txt", "r", stdin);
    setbuf(stdout, NULL);

    scanf("%d", &T);
    for (test_case = 1; test_case <= T; ++test_case) {
        scanf("%d", &N);

        // ... place . .. .
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                B[i][j] = -1;
            }
        }

        // ... place . .. .
        iL = -1;

        Answer = 0;
        for (int i = 0; i < N; i++) {
            place1(N, i);
        }

        printf("%d\n", Answer);
    }
    return 0;
}
