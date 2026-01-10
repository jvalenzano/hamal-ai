import { useState } from 'react';

interface Result {
    risk_score: number;
    reasoning: string;
    recommendation: string;
}

export default function ValidationDashboard() {
    const [idea, setIdea] = useState("");
    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState<Result | null>(null);

    const analyze = async () => {
        setLoading(true);
        try {
            // In production, this URL would be env var or relative proxy
            const res = await fetch('http://localhost:8000/analyze', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ idea })
            });
            const data = await res.json();
            setResult(data);
        } catch (err) {
            console.error(err);
            alert("Error contacting analysis engine.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
            <h1>Hamal AI 🚀</h1>
            <textarea
                value={idea}
                onChange={(e) => setIdea(e.target.value)}
                placeholder="Describe your startup idea..."
                style={{ width: '100%', height: '100px', marginBottom: '1rem' }}
            />
            <button onClick={analyze} disabled={loading}>
                {loading ? "Analyzing..." : "Validate Idea"}
            </button>

            {result && (
                <div style={{ marginTop: '2rem', border: '1px solid #ccc', padding: '1rem' }}>
                    <h2>Risk Score: {result.risk_score}/100</h2>
                    <p><strong>Recommendation:</strong> {result.recommendation}</p>
                    <p><strong>Reasoning:</strong> {result.reasoning}</p>
                </div>
            )}
        </div>
    );
}
