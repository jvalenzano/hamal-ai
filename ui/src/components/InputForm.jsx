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

    return (
        <div className="max-w-4xl mx-auto p-6 bg-slate-800 rounded-lg shadow-xl border border-slate-700">
            <h2 className="text-xl font-semibold mb-4 text-slate-200">Start New Validation</h2>
            <form onSubmit={handleSubmit} className="space-y-4">
                <div>
                    <label className="block text-sm font-medium text-slate-400 mb-1">
                        Project Name (Optional)
                    </label>
                    <input
                        type="text"
                        value={localProjectName}
                        onChange={(e) => setLocalProjectName(e.target.value)}
                        className="w-full px-4 py-2 bg-slate-900 border border-slate-600 rounded-md focus:ring-2 focus:ring-[#FF4500] focus:border-transparent text-white"
                        placeholder="e.g., project-phoenix"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-slate-400 mb-1">
                        Project Charter / Problem Statement
                    </label>
                    <textarea
                        value={charterText}
                        onChange={(e) => setCharterText(e.target.value)}
                        className="w-full h-64 px-4 py-2 bg-slate-900 border border-slate-600 rounded-md focus:ring-2 focus:ring-[#FF4500] focus:border-transparent text-white font-mono text-sm"
                        placeholder="Paste your project charter or email request here..."
                        required
                    />
                </div>

                <div className="flex justify-end pt-4">
                    <button
                        type="submit"
                        disabled={isLoading}
                        className={`px-6 py-3 rounded-md font-bold text-white transition-all
                            ${isLoading
                                ? 'bg-slate-600 cursor-not-allowed'
                                : 'bg-[#FF4500] hover:bg-orange-600 hover:shadow-lg hover:shadow-orange-900/50'
                            }`}
                    >
                        {isLoading ? 'Igniting Engines...' : 'Launch Validation'}
                    </button>
                </div>
            </form>
        </div>
    );
};

export default InputForm;
