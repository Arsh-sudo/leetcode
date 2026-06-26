class Solution:
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)

        offset = n + 2
        size = 2 * n + 5

        bit = [0] * (size + 1)

        def update(idx):
            while idx <= size:
                bit[idx] += 1
                idx += idx & -idx

        def query(idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & -idx
            return s

        pref = 0
        ans = 0

        update(offset)

        for x in nums:
            if x == target:
                pref += 1
            else:
                pref -= 1

            idx = pref + offset

            ans += query(idx - 1)

            update(idx)

        return ans