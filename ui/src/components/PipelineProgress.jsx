import React, { useState } from 'react';
import { usePipeline } from '../context/PipelineContext';
import ActivityLog from './ActivityLog';
import OutputViewer from './OutputViewer';
import SummaryViewer from './SummaryViewer';

const AGENTS = [
    { id: 'discovery', name: 'Discovery', icon: '🔍', file: 'problem.md' },
    { id: 'research', name: 'Research', icon: '🌐', file: 'research.md' },
    { id: 'validation', name: 'Validation', icon: '📊', file: 'validation.md' },
    { id: 'architecture', name: 'Architecture', icon: '🏗️', file: 'architecture.md' },
    { id: 'summary', name: 'Summary', icon: '📄', file: 'summary.html' }
];

const PipelineProgress = () => {
    const { pipelineState, logs, projectName, resetPipeline } = usePipeline();
    const agentsState = pipelineState?.agents || {};
    const [selectedAgent, setSelectedAgent] = useState(null);

    const getStatusColor = (status) => {
        switch (status) {
            case 'complete': return 'bg-green-500 text-white';
            case 'running': return 'bg-[#FF4500] text-white animate-pulse';
            case 'failed': return 'bg-red-500 text-white';
            default: return 'bg-slate-700 text-slate-400';
        }
    };

    return (
        <div className="space-y-8">
            {/* Status Bar */}
            <div className="grid grid-cols-5 gap-4">
                {AGENTS.map((agent) => {
                    const status = agentsState[agent.id]?.status || 'pending';
                    const isComplete = status === 'complete';

                    return (
                        <div
                            key={agent.id}
                            onClick={() => isComplete && setSelectedAgent(agent)}
                            className={`
                                relative p-4 rounded-lg border-2 transition-all cursor-pointer
                                ${selectedAgent?.id === agent.id ? 'border-[#FF4500] ring-2 ring-orange-500/50' : 'border-slate-700'}
                                ${isComplete ? 'hover:border-green-400 hover:bg-slate-800' : ''}
                                bg-slate-800
                            `}
                        >
                            <div className="flex items-center justify-between mb-2">
                                <span className="text-2xl">{agent.icon}</span>
                                <div className={`px-2 py-0.5 rounded text-xs font-bold uppercase ${getStatusColor(status)}`}>
                                    {status}
                                </div>
                            </div>
                            <h3 className="font-semibold text-slate-200">{agent.name}</h3>
                        </div>
                    );
                })}
            </div>

            {/* Main Content Area */}
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                {/* Left: Artifact Viewer (Spans 2 cols) */}
                <div className="lg:col-span-2 space-y-4">
                    {selectedAgent ? (
                        <div className="space-y-2">
                            <div className="flex justify-between items-center">
                                <h3 className="text-xl font-bold text-[#FF4500]">
                                    {selectedAgent.name} Artifact
                                </h3>
                                <button
                                    onClick={() => setSelectedAgent(null)}
                                    className="text-sm text-slate-400 hover:text-white"
                                >
                                    Close Preview
                                </button>
                            </div>
                            {selectedAgent.id === 'summary' ? (
                                <SummaryViewer projectName={projectName} />
                            ) : (
                                <OutputViewer projectName={projectName} filename={selectedAgent.file} />
                            )}
                        </div>
                    ) : (
                        <div className="bg-slate-800/50 border border-slate-700 rounded-lg h-96 flex flex-col items-center justify-center text-slate-500 p-8 text-center">
                            <span className="text-4xl mb-4">🚀</span>
                            <p className="text-lg">Select a completed agent above to view its output.</p>
                            <p className="text-sm mt-2 opacity-70">Pipeline execution in progress...</p>
                        </div>
                    )}
                </div>

                {/* Right: Activity Log */}
                <div className="lg:col-span-1">
                    <h3 className="text-lg font-semibold text-slate-300 mb-2">System Terminal</h3>
                    <ActivityLog logs={logs} />
                </div>
            </div>

            <div className="flex justify-center pt-8">
                <button
                    onClick={resetPipeline}
                    className="text-slate-500 hover:text-white underline decoration-dashed"
                >
                    Start New Process
                </button>
            </div>
        </div>
    );
};

export default PipelineProgress;
