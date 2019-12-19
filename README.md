# hindi-numbers
Convert Arabic numerals to Devanagari text

e.g., 2134 to 'दो हज़ार एक सौ चौंतीस'
## Usage

    from hindi_numbers import arabic_to_dev

    assert arabic_to_dev(23) == 'तेईस'
	assert arabic_to_dev(2134) == 'दो हज़ार एक सौ चौंतीस'
	assert arabic_to_dev(23134787) == 'दो करोड़ इकतीस लाख चौंतीस हज़ार सात सौ सतासी'
	assert arabic_to_dev(399) == 'तीन सौ निन्यानवे'

## Compatibility
Tested with 3.6.8 and 3.7.4

## License
MIT license