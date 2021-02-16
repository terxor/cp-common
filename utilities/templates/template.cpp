#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ii = pair<int, int>;
using pll = pair<ll, ll>;

#define sz(x) (int)(x).size()

template <typename T> bool ckmin (T& a, T b) { return (b < a) ? a = b, 1 : 0; }
template <typename T> bool ckmax (T& a, T b) { return (b > a) ? a = b, 1 : 0; }

#ifdef XVENOM
  #define dbg(...) cerr << "[" << #__VA_ARGS__ << "]: " << dbg_str(__VA_ARGS__)
#else
  #define dbg(...) ;
#endif
template <typename U, typename V> string to_string (pair<U, V>);
string to_string (const char* e) { return "\"" + string(e) + "\""; }
string to_string (string& e) { return "\"" + e + "\""; }
string to_string (char e) { return "\'" + string(1, e) + "\'"; }
string to_string (bool e) { return e ? "true" : "false"; }
template <typename T> string to_string (T e) {
  string s = "[ "; for (auto& x : e) s += to_string(x) + " "; return s + "]";
}
template <typename U, typename V> string to_string (pair<U, V> e) {
  return "(" + to_string(e.first) + ", " + to_string(e.second) + ")";
}
string dbg_str () { return " \n"; }
template <typename U, typename... V> string dbg_str (U u, V... v) {
  return " " + to_string(u) + dbg_str(v...);
}
/* *** */
int main() {
  ios_base::sync_with_stdio(0); cin.tie(0);
}
