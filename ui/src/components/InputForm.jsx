import React, { useState } from 'react';
import { triggerPipeline } from '../api/client';
import { usePipeline } from '../context/PipelineContext';

const InputForm = () => {
    const [charterText, setCharterText] = useState('');
    const [localProjectName, setLocalProjectName] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const { startPolling } = usePipeline();

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!charterText.trim()) return;

        setIsLoading(true);
        try {
            const result = await triggerPipeline(charterText, localProjectName || null);
            startPolling(result.project_name);
        } catch (error) {
            console.error(error);
            alert('Failed to start pipeline');
            setIsLoading(false);
        }
    };

    const handleFileUpload = (e) => {
        const file = e.target.files[0];
        if (!file) return;

        const reader = new FileReader();
        reader.onload = (event) => {
            setCharterText(event.target.result);
        };
        reader.readAsText(file);
    };

    const hasContent = charterText.trim().length > 0;

    return (
        <div className="max-w-4xl mx-auto p-8 bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 shadow-xl transition-all duration-300">
            {/* Clean header, no gaming underscores */}
            <div className="flex justify-between items-center mb-6">
                <h2 className="text-2xl font-semibold text-slate-900 dark:text-white flex items-center tracking-tight">
                    <span className="text-brand-orange mr-3">➜</span> Project Initialization
                </h2>
                <div className="flex space-x-3">
                    {/* Template Option */}
                    <button
                        type="button"
                        onClick={() => {
                            setLocalProjectName("");
                            setCharterText(`# PROJECT CHARTER TEMPLATE

## 1. Problem Statement
**What is the core issue?**
[Describe the specific pain point, inefficiency, or gap. Focus on the 'current state' and why it is unsustainable.]
*Tip: Be specific. Instead of "Efficiency is low," say "Staff spend 40% of their time on manual data entry."*

## 2. Impact & Urgency
**Why does this matter now?**
[Quantify the negative impact of the problem (e.g., cost, time, risk). Explain the consequences of inaction.]

## 3. Proposed Solution (Hypothesis)
**What are we building?**
[Briefly describe the proposed intervention or product. What does the 'future state' look like?]
*Note: This is a starting hypothesis. The validation process will challenge this.*

## 4. Key Constraints
**What are the boundaries?**
- **Technical**: [e.g., Must run on-premise, must use specific language]
- **Regulatory**: [e.g., GDPR compliance, FedRAMP, HIPAA]
- **Operational**: [e.g., Budget cap, timeline, existing team skills]
- **Strategic**: [e.g., Must align with 2026 Digital Strategy]`);
                        }}
                        className="cursor-pointer inline-flex items-center px-3 py-1.5 text-xs font-medium text-slate-600 dark:text-slate-400 bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 rounded-md transition-colors border border-slate-200 dark:border-slate-700"
                    >
                        <span className="mr-2">📝</span> Use Template
                    </button>

                    {/* File Upload Option */}
                    <div className="relative">
                        <input
                            type="file"
                            id="charter-upload"
                            className="hidden"
                            accept=".txt,.md,.pdf" // Basic text formats
                            onChange={handleFileUpload}
                        />
                        <label
                            htmlFor="charter-upload"
                            className="cursor-pointer inline-flex items-center px-3 py-1.5 text-xs font-medium text-slate-600 dark:text-slate-400 bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 rounded-md transition-colors border border-slate-200 dark:border-slate-700"
                        >
                            <span className="mr-2">📂</span> Upload Charter
                        </label>
                    </div>
                </div>
            </div>

            <form onSubmit={handleSubmit} className="space-y-8">
                <div>
                    <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">
                        Project Name
                    </label>
                    <input
                        type="text"
                        value={localProjectName}
                        onChange={(e) => setLocalProjectName(e.target.value)}
                        className="w-full px-4 py-3 bg-slate-50 dark:bg-slate-900 border border-slate-300 dark:border-slate-600 rounded-lg focus:ring-2 focus:ring-brand-orange/20 focus:border-brand-orange text-slate-900 dark:text-white placeholder-slate-400 dark:placeholder-slate-500 transition-all shadow-sm"
                        placeholder="e.g. Venus Exploration"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">
                        Charter / Directive
                    </label>
                    <textarea
                        value={charterText}
                        onChange={(e) => setCharterText(e.target.value)}
                        className="w-full h-64 px-4 py-4 bg-slate-50 dark:bg-slate-900 border border-slate-300 dark:border-slate-600 rounded-lg focus:ring-2 focus:ring-brand-orange/20 focus:border-brand-orange text-slate-900 dark:text-white placeholder-slate-400 dark:placeholder-slate-500 text-sm leading-relaxed shadow-sm font-mono"
                        placeholder="Paste your project charter or mission parameters here..."
                        required
                    />
                </div>

                <div className="flex justify-end pt-2">
                    <button
                        type="submit"
                        disabled={isLoading || !hasContent}
                        className={`px-8 py-4 font-mono font-bold text-sm tracking-widest uppercase transition-all relative overflow-hidden
                            ${isLoading
                                ? 'bg-slate-800 text-slate-500 cursor-not-allowed border border-slate-700'
                                : hasContent
                                    ? 'bg-brand-orange/10 border border-brand-orange text-brand-orange hover:bg-brand-orange hover:text-white hover:shadow-neon-orange shadow-[0_0_15px_rgba(255,69,0,0.2)] cursor-pointer'
                                    : 'bg-slate-100 dark:bg-slate-800 text-slate-400 dark:text-slate-600 border border-slate-200 dark:border-slate-700 cursor-not-allowed'
                            }`}
                    >
                        {isLoading ? (
                            <span className="flex items-center">
                                <span className="animate-spin mr-2">⟳</span> PROCESSING...
                            </span>
                        ) : 'INITIATE VALIDATION'}
                    </button>
                </div>
            </form>
        </div>
    );
};

export default InputForm;
