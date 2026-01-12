import React, { useState, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import { getArtifactContent } from '../api/client';

const OutputViewer = ({ projectName, filename }) => {
    const [content, setContent] = useState('');
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchContent = async () => {
            try {
                const text = await getArtifactContent(projectName, filename);
                setContent(text);
            } catch (err) {
                setError(err.message);
            }
        };
        if (projectName && filename) fetchContent();
    }, [projectName, filename]);

    if (error) return <div className="text-red-400 p-4">Error loading file: {error}</div>;

    return (
        <div className="bg-white dark:bg-slate-800 p-8 rounded-lg border border-slate-200 dark:border-slate-700 shadow-lg prose dark:prose-invert max-w-none prose-slate dark:prose-blue">
            <ReactMarkdown>{content}</ReactMarkdown>
        </div>
    );
};

export default OutputViewer;
