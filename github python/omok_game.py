import sys

# --- 상수 정의 ---
BOARD_SIZE = 15  # 오목판 크기 (일반적으로 15x15)
EMPTY = "."  # 빈 칸 표시
BLACK = "●"  # 흑돌 표시
WHITE = "○"  # 백돌 표시
WIN_LENGTH = 5  # 승리 조건 (연속된 돌 개수)

# --- 게임 보드 관련 함수 ---


def initialize_board(size):
    """지정된 크기의 빈 오목판을 생성합니다."""
    return [[EMPTY for _ in range(size)] for _ in range(size)]


def print_board(board):
    """현재 오목판 상태를 CMD에 보기 좋게 출력합니다."""
    size = len(board)

    # 상단 열 번호 출력
    print("    ", end="")
    for i in range(size):
        print(f"{i + 1:<2}", end=" ")  # 1부터 시작, 2칸 너비 확보
    print("\n" + "---" * (size + 1))  # 구분선

    # 행 번호와 보드 내용 출력
    for r in range(size):
        print(f"{r + 1:>2}|", end=" ")  # 1부터 시작, 오른쪽 정렬, 2칸 너비
        for c in range(size):
            print(f"{board[r][c]:<2}", end=" ")
        print()  # 줄바꿈
    print("-" * (size * 3 + 4))  # 하단 구분선


def is_valid_move(board, r, c):
    """(r, c) 위치에 돌을 놓을 수 있는지 확인합니다."""
    size = len(board)
    if 0 <= r < size and 0 <= c < size:  # 보드 범위 내인지 확인
        return board[r][c] == EMPTY  # 해당 칸이 비어있는지 확인
    return False  # 범위를 벗어남


def place_stone(board, r, c, player_stone):
    """(r, c) 위치에 플레이어의 돌을 놓습니다."""
    if is_valid_move(board, r, c):
        board[r][c] = player_stone
        return True
    return False


# --- 승리 조건 확인 함수 ---


def check_win(board, player_stone):
    """현재 플레이어가 승리했는지 확인합니다."""
    size = len(board)

    # 모든 칸에 대해 가로, 세로, 대각선 방향으로 확인
    for r in range(size):
        for c in range(size):
            if board[r][c] == player_stone:
                # 가로 확인 (오른쪽)
                if c + WIN_LENGTH <= size:
                    if all(board[r][c + i] == player_stone for i in range(WIN_LENGTH)):
                        return True
                # 세로 확인 (아래)
                if r + WIN_LENGTH <= size:
                    if all(board[r + i][c] == player_stone for i in range(WIN_LENGTH)):
                        return True
                # 대각선 확인 (오른쪽 아래)
                if r + WIN_LENGTH <= size and c + WIN_LENGTH <= size:
                    if all(
                        board[r + i][c + i] == player_stone for i in range(WIN_LENGTH)
                    ):
                        return True
                # 대각선 확인 (오른쪽 위)
                if r - WIN_LENGTH + 1 >= 0 and c + WIN_LENGTH <= size:
                    if all(
                        board[r - i][c + i] == player_stone for i in range(WIN_LENGTH)
                    ):
                        return True
    return False  # 승리 조건을 만족하지 못함


def is_board_full(board):
    """보드가 가득 찼는지 확인합니다 (무승부 조건)."""
    for row in board:
        if EMPTY in row:
            return False  # 빈 칸이 하나라도 있으면 가득 차지 않음
    return True  # 모든 칸이 채워짐


# --- 게임 진행 함수 ---


def get_player_input(player_name, player_stone):
    """플레이어로부터 좌표 입력을 받고 유효성을 검사합니다."""
    while True:
        try:
            coord_str = input(
                f"{player_name} ({player_stone}) 차례입니다. 좌표를 '행,열' 형식으로 입력하세요 (예: 8,8): "
            )
            coords = coord_str.split(",")
            if len(coords) != 2:
                raise ValueError("','로 구분하여 행과 열을 입력해야 합니다.")

            row_str = coords[0].strip()
            col_str = coords[1].strip()

            if not row_str.isdigit() or not col_str.isdigit():
                raise ValueError("행과 열은 숫자로 입력해야 합니다.")

            # 사용자 입력은 1부터 시작, 내부 처리는 0부터 시작하므로 1을 빼줌
            row = int(row_str) - 1
            col = int(col_str) - 1

            return row, col  # 0 기반 인덱스로 반환

        except ValueError as e:
            print(f"입력 오류: {e}. 다시 입력해주세요.")
        except Exception as e:
            print(f"예상치 못한 오류 발생: {e}. 다시 입력해주세요.")


# --- 메인 게임 루프 ---


def play_omok():
    """오목 게임을 시작하고 진행합니다."""
    board = initialize_board(BOARD_SIZE)
    current_player_stone = BLACK
    current_player_name = "흑돌"
    game_over = False

    while not game_over:
        print_board(board)

        # 유효한 입력 받을 때까지 반복
        while True:
            row, col = get_player_input(current_player_name, current_player_stone)

            if is_valid_move(board, row, col):
                place_stone(board, row, col, current_player_stone)
                break  # 유효한 수를 두었으므로 입력 루프 탈출
            else:
                # 사용자 입력은 1 기반이므로 다시 1을 더해서 보여줌
                print(
                    f"잘못된 위치입니다 ({row + 1},{col + 1}). 해당 위치가 보드 범위 내에 있고 비어있는지 확인하세요."
                )

        # 승리 확인
        if check_win(board, current_player_stone):
            print_board(board)  # 마지막 보드 상태 출력
            print(
                f"\n*** {current_player_name}({current_player_stone}) 플레이어가 승리했습니다! ***"
            )
            game_over = True
        # 무승부 확인 (보드가 가득 찼는지)
        elif is_board_full(board):
            print_board(board)
            print("\n*** 보드가 가득 찼습니다. 무승부입니다! ***")
            game_over = True
        # 게임 계속 진행 (플레이어 교체)
        else:
            if current_player_stone == BLACK:
                current_player_stone = WHITE
                current_player_name = "백돌"
            else:
                current_player_stone = BLACK
                current_player_name = "흑돌"


if __name__ == "__main__":
    print("=== 오목 게임 (Gomoku) ===")
    print(f"판 크기: {BOARD_SIZE}x{BOARD_SIZE}")
    print(f"승리 조건: {WIN_LENGTH}개의 돌을 연속으로 놓기")
    print("좌표는 1부터 시작합니다 (예: 가장 왼쪽 위는 1,1)")
    play_omok()
    input("\n아무 키나 눌러 종료하세요...")  # 게임 종료 후 바로 창이 닫히는 것을 방지
