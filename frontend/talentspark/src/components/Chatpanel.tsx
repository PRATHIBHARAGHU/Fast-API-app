import { useState } from "react";

interface Message {
  role: "user" | "assistant";
  content: string;
}

function ChatPanel() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSend() {
    const trimmed = input.trim();
    if (!trimmed) return;

    const userMessage: Message = { role: "user", content: trimmed };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      const response = await fetch("http://localhost:8000/chat/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: trimmed }),
      });

      const data = await response.json();
      const assistantMessage: Message = {
        role: "assistant",
        content: data.answer || "No response",
      };
      setMessages((prev) => [...prev, assistantMessage]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: "Sorry, chat is unavailable right now." },
      ]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div style={{ maxWidth: 700, margin: "24px auto", padding: 16, border: "1px solid #ddd", borderRadius: 12 }}>
      <h3>Career Chat</h3>
      <div style={{ minHeight: 220, border: "1px solid #eee", padding: 12, borderRadius: 8, marginBottom: 12, background: "#fafafa" }}>
        {messages.length === 0 && <p style={{ color: "#666" }}>Ask me about careers, jobs, or skills.</p>}
        {messages.map((msg, index) => (
          <div key={index} style={{ marginBottom: 8 }}>
            <strong>{msg.role === "user" ? "You" : "Assistant"}:</strong> {msg.content}
          </div>
        ))}
        {loading && <div>Thinking...</div>}
      </div>
      <div style={{ display: "flex", gap: 8 }}>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your question"
          style={{ flex: 1, padding: 8, borderRadius: 6, border: "1px solid #ccc" }}
          onKeyDown={(e) => e.key === "Enter" && handleSend()}
        />
        <button onClick={handleSend} style={{ padding: "8px 12px", borderRadius: 6, border: "none", background: "#2563eb", color: "white" }}>
          Send
        </button>
      </div>
    </div>
  );
}

export default ChatPanel;