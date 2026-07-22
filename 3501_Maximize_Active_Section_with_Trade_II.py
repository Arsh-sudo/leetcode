#include <bits/stdc++.h>
using namespace std;

const int NEG = -1e9;
const int INF = 1e9;

struct SegMax {
    int n;
    vector<int> st;

    SegMax() {}
    SegMax(const vector<int>& a) { init(a); }

    void init(const vector<int>& a) {
        n = (int)a.size();
        st.assign(4 * max(1, n) + 5, NEG);
        if (n) build(1, 0, n - 1, a);
    }

    void build(int node, int l, int r, const vector<int>& a) {
        if (l == r) {
            st[node] = a[l];
            return;
        }
        int mid = (l + r) / 2;
        build(node * 2, l, mid, a);
        build(node * 2 + 1, mid + 1, r, a);
        st[node] = max(st[node * 2], st[node * 2 + 1]);
    }

    int query(int ql, int qr) {
        if (ql > qr || n == 0) return NEG;
        return query(1, 0, n - 1, ql, qr);
    }

    int query(int node, int l, int r, int ql, int qr) {
        if (ql <= l && r <= qr) return st[node];
        int mid = (l + r) / 2;
        int res = NEG;
        if (ql <= mid) res = max(res, query(node * 2, l, mid, ql, qr));
        if (qr > mid) res = max(res, query(node * 2 + 1, mid + 1, r, ql, qr));
        return res;
    }
};

struct SegMin {
    int n;
    vector<pair<int, int>> st; // {value, index}

    SegMin() {}
    SegMin(const vector<int>& a) { init(a); }

    void init(const vector<int>& a) {
        n = (int)a.size();
        st.assign(4 * max(1, n) + 5, {INF, -1});
        if (n) build(1, 0, n - 1, a);
    }

    pair<int, int> combine(pair<int, int> a, pair<int, int> b) {
        if (a.first != b.first) return (a.first < b.first ? a : b);
        return (a.second < b.second ? a : b);
    }

    void build(int node, int l, int r, const vector<int>& a) {
        if (l == r) {
            st[node] = {a[l], l};
            return;
        }
        int mid = (l + r) / 2;
        build(node * 2, l, mid, a);
        build(node * 2 + 1, mid + 1, r, a);
        st[node] = combine(st[node * 2], st[node * 2 + 1]);
    }

    pair<int, int> query(int ql, int qr) {
        if (ql > qr || n == 0) return {INF, -1};
        return query(1, 0, n - 1, ql, qr);
    }

    pair<int, int> query(int node, int l, int r, int ql, int qr) {
        if (ql <= l && r <= qr) return st[node];
        int mid = (l + r) / 2;
        pair<int, int> res = {INF, -1};
        if (ql <= mid) res = combine(res, query(node * 2, l, mid, ql, qr));
        if (qr > mid) res = combine(res, query(node * 2 + 1, mid + 1, r, ql, qr));
        return res;
    }
};

class Solution {
public:
    vector<int> maxActiveSectionsAfterTrade(string s, vector<vector<int>>& queries) {
        int n = (int)s.size();
        int totalOnes = 0;
        for (char c : s) totalOnes += (c == '1');

        vector<int> zStart, zEnd, zLen;
        for (int i = 0; i < n; ) {
            if (s[i] == '1') { i++; continue; }
            int j = i;
            while (j < n && s[j] == '0') j++;
            zStart.push_back(i);
            zEnd.push_back(j - 1);
            zLen.push_back(j - i);
            i = j;
        }

        int M = (int)zLen.size();

        vector<int> oneLen(max(0, M - 1)), adjSum(max(0, M - 1));
        for (int i = 0; i + 1 < M; i++) {
            oneLen[i] = zStart[i + 1] - zEnd[i] - 1;
            adjSum[i] = zLen[i] + zLen[i + 1];
        }

        SegMax segZero(zLen);
        SegMax segAdj(adjSum);
        SegMin segMinOne(oneLen);

        auto queryMaxZeroExcl = [&](int l, int r, vector<int> ex) -> int {
            if (l > r) return NEG;
            sort(ex.begin(), ex.end());
            ex.erase(unique(ex.begin(), ex.end()), ex.end());

            int cur = l;
            int res = NEG;
            for (int e : ex) {
                if (e < cur) continue;
                if (e > r) break;
                if (cur <= e - 1) res = max(res, segZero.query(cur, e - 1));
                cur = e + 1;
            }
            if (cur <= r) res = max(res, segZero.query(cur, r));
            return res;
        };

        auto queryMinOneExcl = [&](int l, int r, vector<int> ex) -> pair<int, int> {
            if (l > r) return {INF, -1};
            sort(ex.begin(), ex.end());
            ex.erase(unique(ex.begin(), ex.end()), ex.end());

            int cur = l;
            pair<int, int> res = {INF, -1};
            for (int e : ex) {
                if (e < cur) continue;
                if (e > r) break;
                if (cur <= e - 1) {
                    res = (res.first < INF ? combineMin(res, segMinOne.query(cur, e - 1))
                                            : segMinOne.query(cur, e - 1));
                }
                cur = e + 1;
            }
            if (cur <= r) {
                res = (res.first < INF ? combineMin(res, segMinOne.query(cur, r))
                                        : segMinOne.query(cur, r));
            }
            return res;
        };

        vector<int> ans;
        ans.reserve(queries.size());

        for (auto &q : queries) {
            int l = q[0], r = q[1];

            int P = lower_bound(zEnd.begin(), zEnd.end(), l) - zEnd.begin();
            int Q = upper_bound(zStart.begin(), zStart.end(), r) - zStart.begin() - 1;

            if (P > Q || Q < P || P >= M || Q < 0) {
                ans.push_back(totalOnes);
                continue;
            }

            int zeroCnt = Q - P + 1;
            if (zeroCnt < 2) {
                ans.push_back(totalOnes);
                continue;
            }

            int bLeft = (l < zStart[P] ? zLen[P] : zEnd[P] - l + 1);
            int bRight = (r > zEnd[Q] ? zLen[Q] : r - zStart[Q] + 1);

            auto getB = [&](int idx) -> int {
                if (idx == P) return bLeft;
                if (idx == Q) return bRight;
                return zLen[idx];
            };

            auto maxZeroExcl = [&](vector<int> ex) -> int {
                int res = NEG;
                sort(ex.begin(), ex.end());
                ex.erase(unique(ex.begin(), ex.end()), ex.end());

                auto inEx = [&](int x) {
                    return binary_search(ex.begin(), ex.end(), x);
                };

                if (!inEx(P)) res = max(res, bLeft);
                if (P != Q && !inEx(Q)) res = max(res, bRight);

                int inner = queryMaxZeroExcl(P + 1, Q - 1, ex);
                res = max(res, inner);
                return res;
            };

            auto evalSpecialZero = [&](int h) -> int {
                if (h < P || h > Q) return NEG;
                int bh = getB(h);
                auto mn = queryMinOneExcl(P, Q - 1, {h - 1, h});
                if (mn.second == -1) return NEG;
                return bh - mn.first;
            };

            // Merged block gain
            int merged = NEG;

            // first adjacent pair
            int left1 = getB(P);
            int right1 = (P + 1 == Q ? bRight : zLen[P + 1]);
            merged = max(merged, left1 + right1);

            if (zeroCnt >= 3) {
                // last adjacent pair
                int leftLast = zLen[Q - 1];
                int rightLast = bRight;
                merged = max(merged, leftLast + rightLast);

                // internal pairs
                int lk = P + 1, rk = Q - 2;
                if (lk <= rk) merged = max(merged, segAdj.query(lk, rk));
            }

            // Other zero block gain
            int other = NEG;

            if (zeroCnt >= 2) {
                int lk = P, rk = Q - 1;

                auto first = queryMinOneExcl(lk, rk, {});
                if (first.second != -1) {
                    int minVal = first.first;

                    auto second = queryMinOneExcl(lk, rk, {first.second});

                    if (second.second != -1 && second.first == minVal) {
                        auto third = queryMinOneExcl(lk, rk, {first.second, second.second});

                        if (third.second != -1 && third.first == minVal) {
                            // At least 3 equal minima -> every zero-run has access to minVal
                            other = maxZeroExcl({}) - minVal;
                        } else {
                            int idx1 = first.second, idx2 = second.second;
                            if (idx1 > idx2) swap(idx1, idx2);

                            if (idx2 == idx1 + 1) {
                                int specialZero = idx2;
                                other = max(other, maxZeroExcl({specialZero}) - minVal);
                                other = max(other, evalSpecialZero(specialZero));
                            } else {
                                other = maxZeroExcl({}) - minVal;
                            }
                        }
                    } else {
                        // Unique minimum one-run at p
                        int p = first.second;
                        vector<int> specialSet = {p, p + 1};

                        other = max(other, maxZeroExcl(specialSet) - minVal);
                        for (int h : specialSet) {
                            other = max(other, evalSpecialZero(h));
                        }
                    }
                }
            }

            int gain = max(0, max(merged, other));
            ans.push_back(totalOnes + gain);
        }

        return ans;
    }

private:
    static pair<int, int> combineMin(pair<int, int> a, pair<int, int> b) {
        if (a.first != b.first) return (a.first < b.first ? a : b);
        return (a.second < b.second ? a : b);
    }
};