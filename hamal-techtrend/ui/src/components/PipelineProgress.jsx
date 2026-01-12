import React, { useState } from 'react';
import { CheckCircle, Circle, RefreshCw, AlertCircle, FileText } from 'lucide-react';
import { usePipeline } from '../context/PipelineContext';
import OutputViewer from './OutputViewer';
import SummaryViewer from './SummaryViewer';
import ActivityLog from './ActivityLog';

const AGENTS = [
    { id: 'discovery', label: 'Discovery', description: 'Problem analysis', output: 'problem.md' },
    { id: 'research', label: 'Research', description: 'Market & precedent search', output: 'research.md' },
    { id: 'validation', label: 'Validation', description: 'Feasibility scoring', output: 'validation.md' },
    { id: 'architecture', label: 'Architecture', description: 'Stack & cost estimation', output: 'architecture.md' },
    { id: 'summary', label: 'Summary', description: 'Final report generation', output: 'summary.html' }
];

const PipelineProgress = ({ onComplete }) => {
    const { pipelineState, isPolling, error, logs, projectName } = usePipeline();
    const [selectedAgent, setSelectedAgent] = useState(null);

    const getAgentStatus = (agentId) => {
        if (!pipelineState?.agents) return 'pending';
        return pipelineState.agents[agentId]?.status || 'pending';
    };

    const isComplete = pipelineState?.status === 'complete';

    return (
        <div className="flex flex-col h-full space-y-6">
            {/* Progress Steps */}
            <div className="w-full bg-white dark:bg-gray-800 p-6 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700">
                <div className="flex justify-between items-center relative">
                    {/* Connecting Line */}
                    <div className="absolute left-0 top-1/2 w-full h-0.5 bg-gray-200 dark:bg-gray-700 -z-10" />

                    {AGENTS.map((agent, index) => {
                        const status = getAgentStatus(agent.id);
                        const isActive = status === 'running';
                        const isDone = status === 'complete';
                        const isFailed = status === 'failed';

                        let Icon = Circle;
                        let colorClass = "text-gray-400 bg-white dark:bg-gray-800";
                        let wrapperClass = "p-1 rounded-full z-10 transition-all duration-200 bg-white dark:bg-gray-800";

                        if (isActive) {
                            Icon = RefreshCw;
                            colorClass = "text-blue-500 animate-spin";
                            wrapperClass += " ring-4 ring-blue-100 dark:ring-blue-900 shadow-lg scale-110";
                        } else if (isDone) {
                            Icon = CheckCircle;
                            colorClass = "text-green-500";
                            wrapperClass += " text-green-500";
                        } else if (isFailed) {
                            Icon = AlertCircle;
                            colorClass = "text-red-500";
                            wrapperClass += " text-red-500";
                        }

                        return (
                            <div key={agent.id} className="flex flex-col items-center group cursor-pointer" onClick={() => setSelectedAgent(agent)}>
                                <div className={wrapperClass}>
                                    <Icon className={`w-8 h-8 ${colorClass}`} />
                                </div>
                                <div className="mt-2 text-center">
                                    <p className={`font-medium text-sm ${isActive ? 'text-blue-600 dark:text-blue-400 font-bold' : 'text-gray-900 dark:text-gray-100'}`}>
                                        {agent.label}
                                    </p>
                                    <p className="text-xs text-gray-500 dark:text-gray-400">{agent.description}</p>
                                </div>
                                {isDone && (
                                    <button
                                        onClick={(e) => { e.stopPropagation(); setSelectedAgent(agent); }}
                                        className="mt-1 text-xs text-blue-600 dark:text-blue-400 hover:underline flex items-center"
                                    >
                                        <FileText className="w-3 h-3 mr-1" /> View Output
                                    </button>
                                )}
                            </div>
                        );
                    })}
                </div>

                {error && (
                    <div className="mt-6 p-4 bg-red-50 dark:bg-red-900/20 text-red-700 dark:text-red-300 rounded-md flex items-center">
                        <AlertCircle className="w-5 h-5 mr-2" />
                        {error}
                    </div>
                )}
            </div>

            {/* Activity Log - Show when polling or if we have logs */}
            {(isPolling || logs) && (
                <ActivityLog logs={logs} />
            )}

            {/* Output Viewer Area */}
            {selectedAgent && (
                <div className="flex-1 flex flex-col">
                    <div className="flex justify-between items-center mb-4">
                        <h3 className="text-xl font-bold text-gray-800 dark:text-gray-100">
                            {selectedAgent.label} Output
                        </h3>
                        <button
                            onClick={() => setSelectedAgent(null)}
                            className="text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200"
                        >
                            Close
                        </button>
                    </div>

                    <div className="flex-1 min-h-[500px]">
                        {selectedAgent.id === 'summary' ? (
                            <SummaryViewer projectName={projectName} />
                        ) : (
                            <OutputViewer projectName={projectName} filename={selectedAgent.output} />
                        )}
                    </div>
                </div>
            )}
        </div>
    );
};

export default PipelineProgress;
