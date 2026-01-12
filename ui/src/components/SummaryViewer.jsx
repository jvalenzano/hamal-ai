import React from 'react';
import { getArtifactUrl } from '../api/client';

const SummaryViewer = ({ projectName }) => {
    const url = getArtifactUrl(projectName, 'summary.html');

    return (
        <div className="bg-white rounded-lg shadow-lg overflow-hidden h-[800px]">
            <iframe
                src={url}
                className="w-full h-full border-none"
                title="Executive Summary"
            />
        </div>
    );
};

export default SummaryViewer;
