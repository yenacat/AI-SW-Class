import os
import requests
import json

# --- 설정 ---
# 1. Google Cloud API 키 설정
#    - Google Cloud Console (https://console.cloud.google.com/)에서 API 키를 생성하세요.
#    - 생성된 키를 환경 변수로 설정하는 것이 안전합니다.
#      (예: Linux/macOS: export GOOGLE_API_KEY="YOUR_API_KEY")
#      (예: Windows: set GOOGLE_API_KEY=YOUR_API_KEY)
#    - 또는 아래 코드에 직접 키를 입력할 수도 있지만, 보안상 권장되지 않습니다.
api_key = os.getenv("GOOGLE_API_KEY")
# api_key = "YOUR_API_KEY" # 직접 입력 시 (보안 주의)

if not api_key:
    raise ValueError("GOOGLE_API_KEY 환경 변수를 설정해주세요.")

# 2. 사용할 Gemini 모델 선택
#    - 'gemini-pro': 텍스트 생성에 최적화된 모델
#    - 'gemini-pro-vision': 텍스트 및 이미지 입력 처리 가능 모델 (API 호출 방식이 약간 다름)
model_name = "gemini-pro"

# 3. Gemini API 엔드포인트 URL
#    - v1beta 버전을 사용합니다.
api_url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"

# 4. API에 전달할 프롬프트 (질문)
prompt = "대한민국의 수도는 어디인가요?"

# --- API 호출 및 응답 처리 ---

def call_gemini_api(prompt_text):
    """
    Google Gemini API를 호출하고 응답 결과를 반환합니다.

    Args:
        prompt_text (str): 모델에게 전달할 질문 또는 지시사항.

    Returns:
        dict: API 응답 결과를 파싱한 딕셔너리. 오류 발생 시 None 반환.
    """
    headers = {
        'Content-Type': 'application/json',
    }

    # API 요청 본문 (JSON 형식)
    data = {
        "contents": [{
            "parts": [{
                "text": prompt_text
            }]
        }]
        # 필요에 따라 generationConfig, safetySettings 등을 추가할 수 있습니다.
        # "generationConfig": {
        #     "temperature": 0.9,
        #     "topK": 1,
        #     "topP": 1,
        #     "maxOutputTokens": 2048,
        #     "stopSequences": []
        # },
        # "safetySettings": [
        #     {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        #     # ... 다른 안전 설정
        # ]
    }

    try:
        # POST 요청 보내기
        response = requests.post(api_url, headers=headers, data=json.dumps(data))

        # HTTP 오류 확인 (4xx, 5xx 상태 코드)
        response.raise_for_status()

        # 응답 결과를 JSON으로 파싱
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"API 호출 중 오류 발생: {e}")
        # 응답 내용이 있다면 출력 (오류 메시지 확인용)
        if hasattr(e, 'response') and e.response is not None:
            try:
                print(f"오류 응답 내용: {e.response.json()}")
            except json.JSONDecodeError:
                print(f"오류 응답 내용 (텍스트): {e.response.text}")
        return None
    except json.JSONDecodeError:
        print(f"API 응답 JSON 파싱 중 오류 발생. 응답 내용: {response.text}")
        return None

def parse_and_display_response(response_data):
    """
    파싱된 Gemini API 응답에서 텍스트 결과를 추출하여 화면에 표시합니다.

    Args:
        response_data (dict): API 응답 딕셔너리.
    """
    if not response_data:
        print("응답 데이터가 없습니다.")
        return

    try:
        # Gemini API 응답 구조에 따라 텍스트 결과 추출
        # response_data -> candidates -> [0] -> content -> parts -> [0] -> text
        candidates = response_data.get('candidates', [])
        if candidates:
            content = candidates[0].get('content', {})
            parts = content.get('parts', [])
            if parts:
                generated_text = parts[0].get('text', '')
                print("\n--- Gemini 응답 ---")
                print(generated_text)
            else:
                print("응답 데이터에서 'parts'를 찾을 수 없습니다.")
        else:
            print("응답 데이터에서 'candidates'를 찾을 수 없습니다.")
            # 응답 데이터에 'promptFeedback'이 있는지 확인 (차단 등의 이유)
            if 'promptFeedback' in response_data:
                print(f"프롬프트 피드백: {response_data['promptFeedback']}")


    except (KeyError, IndexError, TypeError) as e:
        print(f"응답 데이터 파싱 중 오류 발생: {e}")
        print("전체 응답 데이터:")
        print(json.dumps(response_data, indent=2, ensure_ascii=False)) # 전체 응답 구조 확인

# --- 실행 ---
if __name__ == "__main__":
    print(f"Google Gemini API 호출 ({model_name})")
    print(f"프롬프트: {prompt}")

    # 1. API 호출
    api_response = call_gemini_api(prompt)

    # 2. 응답 파싱 및 표시
    if api_response:
        parse_and_display_response(api_response)

        # 전체 JSON 응답을 보고 싶다면 주석 해제
        # print("\n--- 전체 JSON 응답 ---")
        # print(json.dumps(api_response, indent=2, ensure_ascii=False))