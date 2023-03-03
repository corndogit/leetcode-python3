class Solution:
    @classmethod
    def _find_prefix_length(cls, pattern: str) -> list[int]:
        prefix_array = [0] * int(len(pattern) + 1)
        prefix_array[0] = -1
        prefix_array[1] = 0

        prefix_length = 0
        i = 1
        while i < len(pattern):
            if pattern[prefix_length] == pattern[i]:
                prefix_length += 1
                i += 1
                prefix_array[i] = prefix_length

            elif prefix_length > 0:
                prefix_length = prefix_array[prefix_length]

            else:
                i += 1
                prefix_array[i] = 0
        return prefix_array

    def str_str(self, haystack: str, needle: str) -> int:
        # char pointers and table of prefix lengths
        h = 0
        n = 0
        t = self._find_prefix_length(needle)

        while h < len(haystack):
            if needle[n] == haystack[h]:
                h += 1
                n += 1
                if n == len(needle):
                    return h - n
            else:
                n = t[n]
                if n < 0:
                    h += 1
                    n += 1
        return -1


if __name__ == "__main__":
    s = Solution()
    txt = "sadbutsad"
    ptn = "sad"
    print(f"haystack: {txt}, needle: {ptn}\n{s.str_str(txt, ptn)}")
