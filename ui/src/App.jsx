import React, { useState, useEffect } from 'react';
import { PipelineProvider, usePipeline } from './context/PipelineContext';
import InputForm from './components/InputForm';
import PipelineProgress from './components/PipelineProgress';

const HamalApp = () => {
    const { pipelineState, resetPipeline } = usePipeline();
    const [darkMode, setDarkMode] = useState(() => {
        if (typeof window !== 'undefined') {
            return localStorage.getItem('theme') === 'dark' ||
                (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches);
        }
        return true;
    });

    useEffect(() => {
        if (darkMode) {
            document.documentElement.classList.add('dark');
            localStorage.setItem('theme', 'dark');
        } else {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('theme', 'light');
        }
    }, [darkMode]);

    return (
        <div className="min-h-screen relative transition-colors duration-500 selection:bg-brand-orange/30 dark:text-slate-100 text-slate-900">
            <div className="stars"></div>

            {/* Navigation / Header */}
            <nav className="border-b border-brand-blue/10 dark:border-brand-blue/30 backdrop-blur-md sticky top-0 z-50 bg-white/70 dark:bg-brand-dark/50 transition-colors duration-500">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="flex items-center justify-between h-24"> {/* Increased height for larger logo */}
                        {/* Logo & Brand */}
                        <div
                            className="flex items-center space-x-6 cursor-pointer group"
                            onClick={resetPipeline}
                        >
                            <img
                                src={darkMode ? "/logo-dark-trans.png" : "/logo-light-trans.png"}
                                alt="Hamal Logo"
                                className={`h-24 w-24 object-contain transition-transform transform group-hover:scale-110 
                                    ${darkMode ? 'mix-blend-screen drop-shadow-neon-orange' : 'mix-blend-multiply drop-shadow-md'}`}
                            />
                            <div>
                                <h1 className="text-3xl font-bold tracking-widest font-mono text-slate-900 dark:text-white">
                                    HAMAL
                                </h1>
                                <span className="text-xs uppercase tracking-[0.4em] text-brand-orange font-semibold dark:text-glow">
                                    Autonomous Validation
                                </span>
                            </div>
                        </div>

                        <div className="flex items-center space-x-6">
                            {/* Theme Toggle */}
                            <button
                                onClick={() => setDarkMode(!darkMode)}
                                className="p-3 rounded-full hover:bg-slate-200 dark:hover:bg-brand-surface transition-colors border border-transparent hover:border-slate-300 dark:hover:border-brand-blue/50"
                                title={darkMode ? "Switch to Light Mode" : "Switch to Dark Mode"}
                            >
                                <span className="text-xl">{darkMode ? '☀️' : '🌙'}</span>
                            </button>

                            {/* Status Indicator */}
                            {pipelineState && (
                                <div className="flex items-center space-x-2 bg-white dark:bg-brand-surface px-4 py-1.5 rounded-sm border border-slate-200 dark:border-brand-blue/50 backdrop-blur-sm shadow-sm dark:shadow-neon-blue">
                                    <span className={`w-2 h-2 rounded-full ${pipelineState.status === 'running' ? 'bg-brand-orange animate-ping' : 'bg-emerald-400'}`}></span>
                                    <span className="text-xs font-mono uppercase text-slate-600 dark:text-blue-200 tracking-wider">
                                        {pipelineState.status}
                                    </span>
                                </div>
                            )}
                        </div>
                    </div>
                </div>
            </nav>
            <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
                {!pipelineState ? (
                    <div className="space-y-12 animate-fade-in-up">
                        {/* Branding Hero Section */}
                        <div className="text-center max-w-4xl mx-auto space-y-8 py-8">
                            <h2 className="text-5xl md:text-7xl font-bold text-slate-900 dark:text-white tracking-tight">
                                The <span className="text-transparent bg-clip-text bg-gradient-to-r from-brand-orange to-amber-500 drop-shadow-md dark:drop-shadow-neon-orange">Head of the Ram</span>
                            </h2>
                            <div className="relative bg-white dark:bg-brand-surface p-8 rounded-lg border border-slate-200 dark:border-brand-blue/30 backdrop-blur-sm max-w-2xl mx-auto shadow-sm dark:shadow-none">
                                <div className="absolute top-0 left-0 w-2 h-full bg-brand-orange/50 rounded-l-lg"></div>
                                <p className="text-lg text-slate-600 dark:text-blue-100 font-light leading-relaxed tracking-wide">
                                    "Hamal (Alpha Arietis) is the brightest star in Aries. Just as this star historically guided navigators,
                                    this intelligence layer serves as the <strong className="text-slate-900 dark:text-white font-medium">brain of the constellation</strong>—guiding ideas from the chaos of conception to the clarity of execution."
                                </p>
                            </div>
                        </div>

                        {/* Input Form */}
                        <InputForm />
                    </div>
                ) : (
                    /* Pipeline Visualization */
                    <PipelineProgress />
                )}
            </main>

            {/* Footer */}
            <footer className="border-t border-slate-900 mt-20 py-8 text-center text-slate-600 text-sm">
                <p>&copy; {new Date().getFullYear()} Hamal. Powered by Aries Digital.</p>
            </footer>
        </div>
    );
};

function App() {
    return (
        <PipelineProvider>
            <HamalApp />
        </PipelineProvider>
    );
}

export default App;
