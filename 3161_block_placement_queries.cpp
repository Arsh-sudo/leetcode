#include <vector>
#include <set>
#include <algorithm>
#include <cstring>

using namespace std;

class Solution {
    int tree[200020];
    int MAX_X = 50005;

    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = val;
            return;
        }
        int mid = start + (end - start) / 2;
        if (idx <= mid) {
            update(2 * node, start, mid, idx, val);
        } else {
            update(2 * node + 1, mid + 1, end, idx, val);
        }
        tree[node] = max(tree[2 * node], tree[2 * node + 1]);
    }

    int query(int node, int start, int end, int L, int R) {
        if (R < start || L > end) return 0;
        if (L <= start && end <= R) return tree[node];
        int mid = start + (end - start) / 2;
        return max(query(2 * node, start, mid, L, R),
                   query(2 * node + 1, mid + 1, end, L, R));
    }

public:
    vector<bool> getResults(vector<vector<int>>& queries) {
        set<int> obstacles;
        obstacles.insert(0);
        vector<bool> res;
        
        memset(tree, 0, sizeof(tree));

        for (const auto& q : queries) {
            if (q[0] == 1) {
                int x = q[1];
                auto it = obstacles.upper_bound(x);
                int next_obs = (it == obstacles.end()) ? -1 : *it;
                it--;
                int prev_obs = *it;

                obstacles.insert(x);
                update(1, 0, MAX_X, x, x - prev_obs);

                if (next_obs != -1) {
                    update(1, 0, MAX_X, next_obs, next_obs - x);
                }
            } else {
                int x = q[1], sz = q[2];
                auto it = obstacles.upper_bound(x);
                it--;
                int prev_obs = *it;

                int max_gap_in_tree = query(1, 0, MAX_X, 0, prev_obs);
                int last_gap = x - prev_obs;

                res.push_back(max(max_gap_in_tree, last_gap) >= sz);
            }
        }
        return res;
    }
};