"""
Module to convert arabic numerals to devanagari
author: harisankarh
"""

# adapted from https://www.omniglot.com/language/numbers/hindi.htm
dict_str = """0	०	शून्य (śūnya)
1	१	एक (ek)
2	२	दो (do)
3	३	तीन (tīn)
4	४	चार (chār)
5	५	पाँच (pāṅc)
6	६	छे (chaḥ)
7	७	सात (sāt)
8	८	आठ (āṭh)
9	९	नौ (nau)
10	१०	दस (das)
11	११	ग्यारह (gyārah)
12	१२	बारह (bārah)
13	१३	तेरह (tērah)
14	१४	चौदह (caudah)
15	१५	पन्द्रह (paṃdrah)
16	१६	सोलह (solaha)
17	१७	सत्रह (satrah)
18	१८	अठारह (aṭṭhārah)
19	१९	उन्नीस (unnis)
20	२०	बीस (bīs)
21	२१	इक्कीस (ikkīs)
22	२२	बाईस (bāīs)
23	२३	तेईस (tēīs)
24	२४	चौबीस (chaubīs)
25	२५	पच्चीस (paccīs)
26	२६	छब्बीस (chabbī)
27	२७	सत्ताईस (sattāīs)
28	२८	अट्ठाईस (aṭṭhāīs)
29	२९	उनतीस (unatīs)
30	३०	तीस (tīs)
31	३१	इकतीस (ikatīs)
32	३२	बत्तीस (battīs)
33	३३	तैंतीस (taiṃtīs)
34	३४	चौंतीस (cauṃtīs)
35	३५	पैंतीस (paiṃtīs)
36	३६	छत्तीस (chattīs)
37	३७	सैंतीस (saiṃtīs)
38	३८	अड़तीस (aṛatīs)
39	३९	उनतालीस (unatālīs)
40	४०	चालीस (cālīs)
41	४१	इकतालीस (ikatālīsa)
42	४२	बयालीस (bayālīsa)
43	४३	तैंतालीस (taiṃtālīsa)
44	४४	चौवालीस (cauṃtālīsa)
45	४५	पैंतालीस (paiṃtālīsa)
46	४६	छियालीस (chiyālīsa)
47	४७	सैंतालीस (saiṃtālīsa)
48	४८	अड़तालीस (aṛatālīsa)
49	४९	उनचास (unacāsa)
50	५०	पचास (pacāsa)
51	५१	इक्यावन (ikyābana)
52	५२	बावन (bāvana)
53	५३	तिरेपन (tirēpana)
54	५४	चौवन (caubana)
55	५५	पचपन (pacapana)
56	५६	छप्पन (chappana)
57	५७	सत्तावन (sattāvana)
58	५८	अट्ठावन (aṭṭhāvana)
59	५९	उनसठ (unasaṭha)
60	६०	साठ (sāṭha)
61	६१	इकसठ (ikasaṭha)
62	६२	बासठ (bāsaṭha)
63	६३	तिरेसठ (tirasaṭha)
64	६४	चौंसठ (cauṃsaṭha)
65	६५	पैंसठ (paiṃsaṭha)
66	६६	छियासठ (chiyāsaṭha)
67	६७	सड़सठ (saṛasaṭha)
68	६८	अड़सठ (aṛasaṭha)
69	६९	उनहत्तर (unahattara)
70	७०	सत्तर (sattara)
71	७१	इकहत्तर (ikahattara)
72	७२	बहत्तर (bahattara)
73	७३	तिहत्तर (tihattara)
74	७४	चौहत्तर (cauhattara)
75	७५	पचहत्तर (pacahattara)
76	७६	छिहत्तर (chihattara)
77	७७	सतहत्तर (satahattara)
78	७८	अठहत्तर (aṭhahattara)
79	७९	उनासी (unāsī)
80	८०	अस्सी (assī)
81	८१	इक्यासी (ikyāsī)
82	८२	बयासी (bayāsī)
83	८३	तिरासी (tirāsī)
84	८४	चौरासी (caurāsī)
85	८५	पचासी (pacāsī)
86	८६	छियासी (chiyāsī)
87	८७	सतासी (satāsī)
88	८८	अट्ठासी (aṭhāsī)
89	८९	नवासी (navāsī)
90	९०	नब्बे (nabbē)
91	९१	इक्यानवे (ikyānabē)
92	९२	बानवे (bānavē)
93	९३	तिरानवे (tirānavē)
94	९४	चौरानवे (caurānavē)
95	९५	पचानवे (pacānavē)
96	९६	छियानवे (chiyānavē)
97	९७	सत्तानवे (sattānavē)
98	९८	अट्ठानवे (aṭṭhānavē)
99	९९	निन्यानवे (ninyānavē)
100	१००	सौ (sau)
1000	१,०००	हज़ार (hazār)
100000	१,००,०००	लाख (lākh)
10000000	१००,००,०००	करोड़ (karoṛ)"""


def _get_arabic_to_dev_atomic_map(dict_str):
    arabic_to_dev = {}
    for line in dict_str.split('\n'):
        line = line.strip()
        # print(line.split('\t'))
        assert len(line.split('\t')) == 3, line.split('\t')
        cols = line.split('\t')
        arabic_int = int(cols[0])
        devanagari_str = cols[2].split()[0]
        # print(arabic_int, devanagari_str)
        arabic_to_dev[arabic_int] = devanagari_str
    return arabic_to_dev


arabic_to_dev_atomic_map = _get_arabic_to_dev_atomic_map(dict_str)


def arabic_to_dev(arabic_int):
    """
    accepts integers and returns verbose string representation in
    devanagari script
    e.g., arabic_to_dev(23) returns 'तेईस'
    in case the number is not valid or any other error occurs,
    raises exception
    """
    if arabic_int in arabic_to_dev_atomic_map:
        return arabic_to_dev_atomic_map[arabic_int]
    arabic_str = str(arabic_int)
    sub_prefix = ''
    for idx in range(len(arabic_str)):
        sub_prefix += arabic_str[idx]
        base_exponent = int('1' + '0' * (len(arabic_str[idx:]) - 1))
        if base_exponent in arabic_to_dev_atomic_map:
            return ' '.join([arabic_to_dev(int(sub_prefix)),
                             arabic_to_dev_atomic_map[base_exponent],
                             arabic_to_dev(int(arabic_str[(idx + 1):]))])
    raise RuntimeError('error in arabic_to_dev conversion')


def main():
    assert arabic_to_dev(23) == 'तेईस'
    assert arabic_to_dev(2134) == 'दो हज़ार एक सौ चौंतीस'
    assert arabic_to_dev(
        23134787) == 'दो करोड़ इकतीस लाख चौंतीस हज़ार सात सौ सतासी'
    assert arabic_to_dev(399) == 'तीन सौ निन्यानवे'


if __name__ == "__main__":
    main()
