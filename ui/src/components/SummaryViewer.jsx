import React from 'react';
import { getArtifactUrl } from '../api/client';

const SummaryViewer = ({ projectName }) => {
    const url = getArtifactUrl(projectName, 'summary.html');

    return (
        <div className="bg-white dark:bg-slate-900 rounded-lg shadow-lg border border-slate-200 dark:border-slate-700 overflow-hidden h-[800px]">
            <iframe
                src={url}
                className="w-full h-full border-none bg-white" // iframe content is usually white HTML, keeping bg-white to avoid jarring transitions
                title="Executive Summary"
            />
        </div>
    );
};

export default SummaryViewer;
