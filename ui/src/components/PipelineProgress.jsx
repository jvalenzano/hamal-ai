import React, { useState } from 'react';
import { usePipeline } from '../context/PipelineContext';
import ActivityLog from './ActivityLog';
import OutputViewer from './OutputViewer';
import SummaryViewer from './SummaryViewer';
import { getArtifactUrl } from '../api/client';
import { Check, Loader2, FileDown, Printer } from 'lucide-react';

const AGENTS = [
    {
        id: 'discovery',
        name: 'Discovery',
        file: 'problem.md',
        description: 'Interrogates the initial charter using "5 Whys" methodology to refine the problem statement.',
        activeText: 'Running 5-Whys analysis and gathering context...'
    },
    {
        id: 'research',
        name: 'Research',
        file: 'research.md',
        description: 'Searches for government precedents, commercial solutions, and historical failure cases.',
        activeText: 'Scanning web for competitors and precedents...'
    },
    {
        id: 'validation',
        name: 'Validation',
        file: 'validation.md',
        description: 'Scores feasibility and identifies critical risks (Compliance, Technical, Budget).',
        activeText: 'Evaluating feasibility and calculating risk scores...'
    },
    {
        id: 'architecture',
        name: 'Architecture',
        file: 'architecture.md',
        description: 'Designs the technical stack and provides a rough order-of-magnitude cost estimate.',
        activeText: 'Generating stack recommendations and cost analysis...'
    },
    {
        id: 'summary',
        name: 'Summary',
        file: 'summary.html',
        description: 'Synthesizes all findings into a structured "Go/No-Go" executive report.',
        activeText: 'Compiling final executive validation report...'
    }
];

const PipelineProgress = () => {
    const { pipelineState, logs, projectName, resetPipeline } = usePipeline();
    const agentsState = pipelineState?.agents || {};
    const [selectedAgent, setSelectedAgent] = useState(null);

    const handleDownload = (agent) => {
        const url = getArtifactUrl(projectName, agent.file);
        const link = document.createElement('a');
        link.href = url;
        link.download = agent.file;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    };

    const handlePrint = () => {
        try {
            const iframe = document.querySelector('iframe[title="Executive Summary"]');
            if (iframe && iframe.contentWindow) {
                iframe.contentWindow.focus();
                iframe.contentWindow.print();
            } else {
                throw new Error("Summary iframe not found");
            }
        } catch (error) {
            console.error("Print failed:", error);
            alert("Could not print the report. Try downloading the HTML file instead.");
        }
    };

    return (
        <div className="space-y-12">
            {/* Status Bar - Vertical Text Cards Layout */}
            <div className="sticky top-0 z-20 bg-slate-50/95 dark:bg-slate-950/95 backdrop-blur-md pb-6 pt-4 -mx-4 px-4 border-b border-slate-200 dark:border-slate-800 shadow-sm transition-all duration-300">
                <div className="grid grid-cols-1 md:grid-cols-5 gap-4">
                    {AGENTS.map((agent) => {
                        const status = agentsState[agent.id]?.status || 'pending';
                        const isComplete = status === 'complete';
                        const isRunning = status === 'running';

                        return (
                            <div
                                key={agent.id}
                                onClick={() => isComplete && setSelectedAgent(agent)}
                                className={`
                                relative p-6 rounded-xl border transition-all duration-300 flex flex-col justify-between min-h-[180px] group
                                ${isComplete
                                        ? 'cursor-pointer hover:border-emerald-500/50 bg-white dark:bg-slate-900 border-slate-200 dark:border-slate-800 shadow-sm hover:shadow-lg'
                                        : ''}
                                ${isRunning
                                        ? 'bg-slate-50 dark:bg-slate-900 border-brand-orange ring-1 ring-brand-orange/50 shadow-[0_0_20px_rgba(234,88,12,0.1)]'
                                        : 'bg-slate-50 dark:bg-slate-900 border-slate-200 dark:border-slate-800'}
                                ${!isComplete && !isRunning ? 'opacity-60 grayscale' : ''}
                            `}
                            >
                                <div>
                                    <div className="flex justify-between items-start mb-4">
                                        <h3 className={`font-bold text-sm uppercase tracking-wider ${isRunning ? 'text-brand-orange' : 'text-slate-900 dark:text-white'
                                            }`}>
                                            {agent.name}
                                        </h3>

                                        {/* Status Icon */}
                                        <div className="flex items-center justify-center w-8 h-8">
                                            {isComplete && (
                                                <div className="bg-emerald-100 dark:bg-emerald-500/20 p-1.5 rounded-full ring-1 ring-emerald-500/30">
                                                    <Check className="w-4 h-4 text-emerald-600 dark:text-emerald-400" strokeWidth={3} />
                                                </div>
                                            )}
                                            {isRunning && (
                                                <Loader2 className="w-5 h-5 text-brand-orange animate-spin" />
                                            )}
                                            {!isComplete && !isRunning && (
                                                <div className="w-2 h-2 rounded-full bg-slate-300 dark:bg-slate-700" />
                                            )}
                                        </div>
                                    </div>

                                    <p className={`text-xs leading-relaxed ${isRunning ? 'text-slate-700 dark:text-slate-200 font-medium' : 'text-slate-500 dark:text-slate-400'
                                        }`}>
                                        {isRunning ? agent.activeText : agent.description}
                                    </p>
                                </div>

                                {/* Active Progress Bar */}
                                {isRunning && (
                                    <div className="mt-4 w-full h-1 bg-brand-orange/20 rounded-full overflow-hidden">
                                        <div className="h-full bg-brand-orange animate-progress-indeterminate"></div>
                                    </div>
                                )}

                                {/* Completed Indicator */}
                                {isComplete && (
                                    <div className="mt-4 flex items-center text-xs text-emerald-600 dark:text-emerald-400 font-medium opacity-0 group-hover:opacity-100 transition-opacity">
                                        <span>View Artifact</span>
                                        <span className="ml-1">→</span>
                                    </div>
                                )}
                            </div>
                        );
                    })}
                </div>
            </div>

            {/* Main Content Area */}
            <div className="grid grid-cols-1 gap-8">
                {/* Artifact Viewer */}
                <div className="min-h-[400px]">
                    {selectedAgent ? (
                        <div className="space-y-4 animate-fade-in-up">
                            <div className="flex justify-between items-center bg-slate-50 dark:bg-slate-800/50 p-4 rounded-lg border border-slate-200 dark:border-slate-700">
                                <div className="flex items-center space-x-3">
                                    <h3 className="text-xl font-bold text-slate-900 dark:text-white">
                                        {selectedAgent.name} Output
                                    </h3>
                                </div>
                                <div className="flex items-center space-x-3">
                                    {/* Print/Save to PDF Action for Summary */}
                                    {selectedAgent.id === 'summary' && (
                                        <button
                                            onClick={handlePrint}
                                            className="px-3 py-1 text-sm text-slate-700 dark:text-slate-300 hover:text-white hover:bg-slate-700 dark:hover:bg-slate-600 rounded border border-slate-300 dark:border-slate-600 transition-colors flex items-center group"
                                            title="Print or Save as PDF"
                                        >
                                            <Printer className="w-4 h-4 mr-1 group-hover:scale-110 transition-transform" />
                                            Print Report
                                        </button>
                                    )}

                                    {/* Standard Download */}
                                    <button
                                        onClick={() => handleDownload(selectedAgent)}
                                        className="px-3 py-1 text-sm text-brand-blue hover:text-white hover:bg-brand-blue rounded border border-brand-blue/30 transition-colors flex items-center group"
                                        title={`Download ${selectedAgent.file}`}
                                    >
                                        <FileDown className="w-4 h-4 mr-2 group-hover:translate-y-1 transition-transform" />
                                        Download {selectedAgent.file.split('.').pop().toUpperCase()}
                                    </button>

                                    <button
                                        onClick={() => setSelectedAgent(null)}
                                        className="px-3 py-1 text-sm text-slate-500 hover:text-slate-900 dark:hover:text-white transition-colors"
                                    >
                                        Close Preview ✕
                                    </button>
                                </div>
                            </div>
                            {selectedAgent.id === 'summary' ? (
                                <SummaryViewer projectName={projectName} />
                            ) : (
                                <OutputViewer projectName={projectName} filename={selectedAgent.file} />
                            )}
                        </div>
                    ) : (
                        <div className="h-full flex flex-col items-center justify-center text-slate-400 dark:text-slate-500 space-y-4 p-12 border-2 border-dashed border-slate-200 dark:border-slate-800 rounded-xl">
                            <span className="text-6xl opacity-20">⚡️</span>
                            <div className="text-center">
                                <p className="text-lg font-medium">Pipeline Active</p>
                                <p className="text-sm opacity-70">Monitor the terminal below or select a completed stage above.</p>
                            </div>
                        </div>
                    )}
                </div>

                {/* Bottom Terminal */}
                <div className="w-full">
                    <div className="flex items-center justify-between mb-2 px-1">
                        <h3 className="text-sm font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider font-mono">
                            >_ System Terminal
                        </h3>
                    </div>
                    <ActivityLog logs={logs} />
                </div>
            </div>

            <div className="flex justify-center pt-8 border-t border-slate-200 dark:border-slate-800">
                <button
                    onClick={resetPipeline}
                    className="flex items-center space-x-2 text-slate-500 hover:text-brand-orange transition-colors group"
                >
                    <span className="group-hover:-translate-x-1 transition-transform">←</span>
                    <span className="underline decoration-dashed underline-offset-4">Start New Process</span>
                </button>
            </div>
        </div>
    );
};

export default PipelineProgress;
