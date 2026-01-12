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
        <div className="max-w-4xl mx-auto p-8 bg-white dark:bg-glass-panel rounded-xl border border-slate-200 dark:border-brand-blue/30 backdrop-blur-md shadow-2xl relative overflow-hidden group transition-all duration-300">
            {/* Subtle glow effect */}
            <div className="absolute top-0 right-0 w-64 h-64 bg-brand-orange/5 dark:bg-brand-blue/20 rounded-full blur-3xl -z-10 group-hover:bg-brand-orange/10 dark:group-hover:bg-brand-blue/30 transition-all duration-700"></div>

            <h2 className="text-2xl font-mono font-bold mb-6 text-slate-800 dark:text-white flex items-center">
                <span className="text-brand-orange mr-2">➜</span> INITIALIZE_SEQUENCE
            </h2>
            <form onSubmit={handleSubmit} className="space-y-6">
                <div>
                    <label className="block text-xs font-mono uppercase tracking-widest text-slate-500 dark:text-brand-blue/80 mb-2">
                        Project Identification
                    </label>
                    <input
                        type="text"
                        value={localProjectName}
                        onChange={(e) => setLocalProjectName(e.target.value)}
                        className="w-full px-4 py-3 bg-slate-50 dark:bg-brand-dark/50 border border-slate-300 dark:border-brand-blue/30 rounded-none focus:ring-1 focus:ring-brand-orange focus:border-brand-orange text-slate-900 dark:text-white placeholder-slate-400 dark:placeholder-slate-600 font-mono transition-all"
                        placeholder="PROJECT_CODENAME"
                    />
                </div>

                <div>
                    <label className="block text-xs font-mono uppercase tracking-widest text-slate-500 dark:text-brand-blue/80 mb-2">
                        Directive Input / Charter
                    </label>
                    <textarea
                        value={charterText}
                        onChange={(e) => setCharterText(e.target.value)}
                        className="w-full h-64 px-4 py-4 bg-slate-50 dark:bg-brand-dark/50 border border-slate-300 dark:border-brand-blue/30 rounded-none focus:ring-1 focus:ring-brand-orange focus:border-brand-orange text-slate-800 dark:text-blue-100 font-mono text-sm leading-relaxed"
                        placeholder="// Enter mission parameters or paste project charter..."
                        required
                    />
                </div>

                <div className="flex justify-end pt-2">
                    <button
                        type="submit"
                        disabled={isLoading}
                        className={`px-8 py-4 font-mono font-bold text-sm tracking-widest uppercase transition-all relative overflow-hidden
                            ${isLoading
                                ? 'bg-slate-800 text-slate-500 cursor-not-allowed border border-slate-700'
                                : 'bg-brand-orange/10 border border-brand-orange text-brand-orange hover:bg-brand-orange hover:text-white hover:shadow-neon-orange shadow-[0_0_15px_rgba(255,69,0,0.2)]'
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
