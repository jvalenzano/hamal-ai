import { useState } from 'react';
import { useReactMediaRecorder } from 'react-media-recorder';
import { Mic, Square, Loader2, FileAudio } from 'lucide-react';

export default function EchoRecorder() {
    const [transcription, setTranscription] = useState("");
    const [isProcessing, setIsProcessing] = useState(false);

    const { status, startRecording, stopRecording, mediaBlobUrl } = useReactMediaRecorder({
        audio: true,
        onStop: (blobUrl, blob) => handleUpload(blob)
    });

    const handleUpload = async (blob: Blob) => {
        setIsProcessing(true);
        const formData = new FormData();
        formData.append("file", blob, "recording.webm");

        try {
            // Use relative path for production (proxy) or full path for local dev if CORS enabled
            // Assuming proxy is set up or same origin
            const response = await fetch("/transcribe", {
                method: "POST",
                body: formData
            });

            if (!response.ok) throw new Error("Transcription failed");

            const data = await response.json();
            setTranscription(data.text);
        } catch (error) {
            console.error("Error uploading audio:", error);
            alert("Failed to transcribe audio.");
        } finally {
            setIsProcessing(false);
        }
    };

    return (
        <div className="echo-recorder" style={{ maxWidth: '600px', margin: '0 auto', textAlign: 'center', padding: '2rem' }}>
            <h1>Echo 🧠</h1>
            <p style={{ color: '#666', marginBottom: '2rem' }}>Hands-free Second Brain Interface</p>

            <div className="controls" style={{ marginBottom: '2rem' }}>
                {status === 'recording' ? (
                    <button
                        onClick={stopRecording}
                        style={{
                            backgroundColor: '#ef4444',
                            color: 'white',
                            padding: '1rem 2rem',
                            borderRadius: '50px',
                            border: 'none',
                            fontSize: '1.2rem',
                            display: 'flex',
                            alignItems: 'center',
                            gap: '0.5rem',
                            cursor: 'pointer',
                            margin: '0 auto'
                        }}
                    >
                        <Square size={24} /> Stop & Process
                    </button>
                ) : (
                    <button
                        onClick={startRecording}
                        disabled={isProcessing}
                        style={{
                            backgroundColor: isProcessing ? '#94a3b8' : '#2563eb',
                            color: 'white',
                            padding: '1rem 2rem',
                            borderRadius: '50px',
                            border: 'none',
                            fontSize: '1.2rem',
                            display: 'flex',
                            alignItems: 'center',
                            gap: '0.5rem',
                            cursor: isProcessing ? 'not-allowed' : 'pointer',
                            margin: '0 auto',
                            boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)'
                        }}
                    >
                        {isProcessing ? <Loader2 className="animate-spin" /> : <Mic size={24} />}
                        {isProcessing ? "Processing..." : "Start Recording"}
                    </button>
                )}
            </div>

            {/* Debug/Preview Area */}
            {mediaBlobUrl && (
                <div style={{ marginBottom: '2rem' }}>
                    <audio src={mediaBlobUrl} controls style={{ width: '100%' }} />
                </div>
            )}

            {transcription && (
                <div style={{ textAlign: 'left', background: '#f8fafc', padding: '1.5rem', borderRadius: '12px', border: '1px solid #e2e8f0' }}>
                    <h3 style={{ marginTop: 0, display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                        <FileAudio size={20} /> Transcription
                    </h3>
                    <p style={{ lineHeight: '1.6', color: '#334155' }}>{transcription}</p>
                </div>
            )}
        </div>
    );
}
