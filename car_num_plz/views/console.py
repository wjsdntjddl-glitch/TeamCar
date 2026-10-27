# class Console:
#     """사용자 입출력을 전담하는 클래스"""

#     @staticmethod
#     def show_main_menu():
#         print("\n" + "="*40)
#         print("     🚗 주차장 출입 통제 및 관리 시스템")
#         print("="*40)
#         print("1. 조회 (차량 목록 및 검색)")
#         print("2. 관리 (차량 등록/수정/삭제)")
#         print("3. 요금 계산 (외부 차량 정산)")
#         print("4. 프로그램 종료")
#         print("="*40)
#         return input("메뉴를 선택하세요: ").strip()

#     @staticmethod
#     def show_search_menu():
#         print("\n--- [조회 메뉴] ---")
#         print("1. 차량 목록 조회")
#         print("2. 차량 상세 조회")
#         print("3. 제조회사 기준 조회")
#         print("4. 차주 이름으로 조회")
#         print("5. 시간대별 입차 조회")
#         print("0. 이전 메뉴로 돌아가기")
#         return input("조회 방식을 선택하세요: ").strip()

#     @staticmethod
#     def show_manage_menu():
#         print("\n--- [관리 메뉴] ---")
#         print("1. 차량 정보 등록 (입차)")
#         print("2. 차량 정보 수정")
#         print("3. 차량 정보 삭제 (출차)")
#         print("0. 이전 메뉴로 돌아가기")
#         return input("관리 작업을 선택하세요: ").strip()

#     @staticmethod
#     def display_message(success, message):
#         prefix = "✅ [성공]" if success else "❌ [오류]"
#         print(f"\n{prefix} {message}")

#     @staticmethod
#     def display_car_list(cars):
#         print("\n" + "-"*55)
#         print(f"{'차량번호':<12} | {'차주':<10} | {'제조회사':<10} | {'입차 시간'}")
#         print("-" * 55)
#         if not cars:
#             print("조건에 해당하는 차량이 없습니다.")
#         else:
#             for car in cars:
#                 print(f"{car.car_number:<12} | {car.owner_name:<10} | {car.brand:<10} | {car.entry_time.strftime('%H:%M:%S')}")
#         print("-" * 55)