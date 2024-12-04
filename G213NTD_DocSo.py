G213NTD_digit_to_word = {
    '0': 'Không', '1': 'Một', '2': 'Hai', '3': 'Ba', '4': 'Bốn',
    '5': 'Năm', '6': 'Sáu', '7': 'Bảy', '8': 'Tám', '9': 'Chín'
}
def G213NTD_Read_Number(number):
    num_str = str(number)
    words = [G213NTD_digit_to_word[digit] for digit in num_str]
    return ' '.join(words)
G213NTD_number_input = input("Nhập số: ")
if G213NTD_number_input.isdigit():
    print(G213NTD_Read_Number(G213NTD_number_input))
else:
    print("Vui lòng nhập một số hợp lệ.")
