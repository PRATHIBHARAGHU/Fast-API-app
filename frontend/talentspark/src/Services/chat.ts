import axios from "axios";
import type { ChatRequest, ChatResponse } from "../types/chat";

const API_BASE_URL = "http://localhost:8000";

export async function askChatbot(
  message: string,
  sessionId = "user1"
): Promise<ChatResponse> {
  const payload: ChatRequest = {
    message,
    session_id: sessionId,
  };

  const response = await axios.post<ChatResponse>(`${API_BASE_URL}/chat/ask`, null, {
    params: payload,
  });

  return response.data;
}
