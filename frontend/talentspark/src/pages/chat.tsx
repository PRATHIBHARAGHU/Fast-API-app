import { useState, type FormEvent } from "react";
import { askChatbot } from "../Services/chat";
import type { ChatMessage } from "../types/chat";

const initialMessages: ChatMessage[] = [
  {
    role: "assistant",
    content: "Hi! I can help with career guidance, skill recommendations, and learning paths.",
  },
];

function ChatPage() {
  const [messages, setMessages] = useState<ChatMessage[]>(initialMessages);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleSend(event: FormEvent) {
    event.preventDefault();

    const message = input.trim();
    if (!message) {
      return;
    }

    setMessages((current) => [
      ...current,
      { role: "user", content: message },
    ]);
    setInput("");
    setIsLoading(true);
    setError(null);

    try {
      const response = await askChatbot(message, "user1");
      setMessages((current) => [
        ...current,
        { role: "assistant", content: response.response },
      ]);
    } catch (err) {
      setError("Unable to reach the chat service right now.");
      setMessages((current) => [
        ...current,
        { role: "assistant", content: "Sorry, I could not answer that request." },
      ]);
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <section style={{ maxWidth: 800, margin: "2rem auto", padding: "1.5rem", borderRadius: 16, boxShadow: "0 8px 24px rgba(0,0,0,0.08)", background: "#fff" }}>
      <div style={{ marginBottom: "1rem" }}>
        <h2 style={{ marginBottom: 8 }}>Career Chat Assistant</h2>
        <p style={{ color: "#555", margin: 0 }}>Ask for career advice, study paths, or job guidance.</p>
      </div>

      <div style={{ minHeight: 320, maxHeight: 420, overflowY: "auto", padding: "1rem", border: "1px solid #e5e7eb", borderRadius: 12, background: "#f9fafb" }}>
        {messages.map((message, index) => (
          <div key={index} style={{ display: "flex", justifyContent: message.role === "user" ? "flex-end" : "flex-start", marginBottom: "0.75rem" }}>
            <div style={{ maxWidth: "80%", padding: "0.75rem 1rem", borderRadius: 12, background: message.role === "user" ? "#2563eb" : "#e5e7eb", color: message.role === "user" ? "#fff" : "#111827" }}>
              {message.content}
            </div>
          </div>
        ))}

        {isLoading && (
          <div style={{ display: "flex", justifyContent: "flex-start" }}>
            <div style={{ padding: "0.75rem 1rem", borderRadius: 12, background: "#e5e7eb", color: "#111827" }}>
              Thinking...
            </div>
          </div>
        )}
      </div>

      <form onSubmit={handleSend} style={{ display: "flex", gap: "0.75rem", marginTop: "1rem" }}>
        <input
          value={input}
          onChange={(event) => setInput(event.target.value)}
          placeholder="Type your question here..."
          style={{ flex: 1, padding: "0.8rem 1rem", borderRadius: 10, border: "1px solid #d1d5db" }}
        />
        <button type="submit" disabled={isLoading || !input.trim()} style={{ padding: "0.8rem 1rem", borderRadius: 10, border: "none", background: "#2563eb", color: "#fff", cursor: "pointer" }}>
          Send
        </button>
      </form>

      {error && <p style={{ color: "#dc2626", marginTop: "0.75rem" }}>{error}</p>}
    </section>
  );
}

export default ChatPage;

