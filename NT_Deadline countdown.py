""""NHÓM NT
1. Hoàng Thị Phương Nguyên K214061743
2. Phạm Nguyễn Thanh Tân-K214060411
3. Lê Bảo Phương Nhi-K214060406
4. Nguyễn Ngọc Phương Trúc-K214060419
5. Nguyễn Trọng Nghĩa-K214060403"""


from datetime import *

task = []
def main_screen():
	global task
	print('\n1. Thêm deadline.')
	print('2. Xem các deadline hiện có.')
	print('3. Thoát')
	while True:
		try:
			choice = int(input('\nNhập lựa chọn của bạn: '))
		except ValueError:
			print('Lựa chọn không tồn tại')
		else:
			if choice > 3 or choice < 1:
				print('Lựa chọn không tồn tại.')
			else:
				mode(choice)
				main_screen()


def mode(choice):
	if choice == 1:
		while True:
			try:
				print('Để hủy lệnh thêm đếm ngược, hãy nhập cancel vào khu vực nhập tên Deadline.')
				mission = input('Nhập tên deadline: ')
				if mission == 'cancel':
					print('Bạn đã hủy lệnh.')
					return
				day = int(input('Nhập ngày hết hạn: '))
				month = int(input('Nhập tháng hết hạn: '))
				year = int(input('Nhập năm hết hạn: '))
				hour = int(input('Nhập giờ hết hạn: '))
				minute = int(input('Nhập phút hết hạn: '))
				second = int(input('Nhập giây hết hạn: '))
			except:
				print('Giá trị bạn vừa nhập không hợp lệ, vui lòng nhập lại.')
			else:
				try:
					if datetime(year, month, day, hour, minute, second) - datetime.now() <= timedelta(0):
						print('Ngày giờ nhập vào bé hơn ngày giờ hệ thống.\n')
						continue		
				except:
					print('Giá trị ngày giờ nhập vào không hợp lệ.\n')
				else:
					task.append([mission, [year, month, day, hour, minute, second]])
					return


	if choice == 2:
		if len(task) == 0:
			print('Không có bất kỳ deadline nào được lưu trữ.\n')
		else:
			task_show()
		return

	if choice == 3:
		print('Thoát chương trình.')
		exit()


def task_show():
	for i in task:
		if datetime(i[1][0], i[1][1], i[1][2], i[1][3], i[1][4], i[1][5]) - datetime.now() >= timedelta(0):
			print(i[0], 'còn', datetime(i[1][0], i[1][1], i[1][2], i[1][3], i[1][4], i[1][5]) - datetime.now())
		else:
			print('Deadline', i[0], 'đã hết hạn.')

main_screen()
