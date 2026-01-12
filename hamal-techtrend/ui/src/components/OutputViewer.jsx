import React, { useState, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import { usePipeline } from '../context/PipelineContext';

const OutputViewer = ({ projectName, filename }) => {
    const { getArtifactContent } = usePipeline();
    const [content, setContent] = useState('');
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        let mounted = true;

        const loadContent = async () => {
            if (!projectName || !filename) return;

            try {
                setLoading(true);
                const text = await getArtifactContent(projectName, filename);
                if (mounted) {
                    setContent(text);
                    setError(null);
                }
            } catch (err) {
                if (mounted) {
                    console.error(err);
                    setError("Failed to load content");
                }
            } finally {
                if (mounted) setLoading(false);
            }
        };

        loadContent();

        return () => { mounted = false; };
    }, [projectName, filename, getArtifactContent]);

    if (loading) return <div className="p-4 text-gray-500 animate-pulse">Loading output...</div>;
    if (error) return <div className="p-4 text-red-500">{error}</div>;

    return (
        <div className="prose dark:prose-invert max-w-none p-6 bg-white dark:bg-gray-800 rounded-lg shadow">
            <ReactMarkdown>{content}</ReactMarkdown>
        </div>
    );
};

export default OutputViewer;
