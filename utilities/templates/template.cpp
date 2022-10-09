#include <bits/stdc++.h>
using namespace std;
#define long int64_t
#define sz(x) (int)(x).size()
using ii = pair<int, int>;
using ll = pair<long, long>;
#ifdef XVENOM
  #define dbg(...) cerr<<"["<< __func__<<":"<< __LINE__<<"] "<<#__VA_ARGS__<<" ="<<dbg_str(__VA_ARGS__)
#else
  #define dbg(...) ;
#endif
#define v1ts template<typename U>string to_string
#define v2ts template<typename U,typename V>string to_string
template<typename U>string dbg_cntnr(U);
v2ts(pair<U,V>);
string to_string(const char*e){return "\""+string(e)+"\"";}
string to_string(string& e){return "\""+e+"\"";}
string to_string(char e){return "\'"+string(1,e)+"\'";}
string to_string(bool e){return e?"true":"false";}
v1ts(vector<U> e){return dbg_cntnr(e);}
v1ts(set<U> e){return dbg_cntnr(e);}
v1ts(queue<U> e){return dbg_cntnr(e);}
v2ts(map<U,V> e){return dbg_cntnr(e);}
v2ts(pair<U,V> e){return "("+to_string(e.first)+", "+to_string(e.second)+")";}
template<typename U>string dbg_cntnr(U e){string s="[";int f=1;for(auto& x:e){if(!f)s+=", ";s+=to_string(x);f=0;}return s+"]";}
string dbg_str(){return" \n";}
template<typename U,typename... V>string dbg_str(U u,V... v){return " "+to_string(u)+dbg_str(v...);}

int main() {
  ios_base::sync_with_stdio(0);
}
