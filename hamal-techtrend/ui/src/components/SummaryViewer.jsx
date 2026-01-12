import React from 'react';
import { usePipeline } from '../context/PipelineContext';

const SummaryViewer = ({ projectName }) => {
    const { getArtifactUrl } = usePipeline();
    const summaryUrl = getArtifactUrl(projectName, 'summary.html');

    return (
        <div className="w-full h-[800px] bg-white rounded-lg shadow overflow-hidden">
            <iframe
                src={summaryUrl}
                className="w-full h-full border-0"
                title="Project Summary"
                sandbox="allow-scripts allow-same-origin"
            />
        </div>
    );
};

export default SummaryViewer;
