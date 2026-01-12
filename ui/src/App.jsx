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
                    <div className="flex items-center justify-between h-24">
                        {/* Logo & Brand */}
                        <div
                            className="flex items-center space-x-5 cursor-pointer group"
                            onClick={resetPipeline}
                        >
                            {/* Master Geometric Logo */}
                            <div className="relative h-20 w-20 transition-transform transform group-hover:scale-105">
                                {/* Light Mode: Normal Transparent PNG */}
                                {/* Dark Mode: Brightness 0 -> Black, Invert -> White. Pure Flat White Icon. */}
                                <img
                                    src="/logo-master-v2.png"
                                    alt="Hamal Logo"
                                    className={`w-full h-full object-contain 
                                        ${darkMode
                                            ? 'filter brightness-0 invert drop-shadow-[0_0_8px_rgba(255,255,255,0.2)]'
                                            : 'drop-shadow-sm'
                                        }`}
                                />
                            </div>

                            <div className="flex flex-col justify-center">
                                <h1 className="text-3xl font-bold tracking-tight font-sans text-slate-900 dark:text-white leading-none">
                                    HAMAL
                                </h1>
                                <span className="text-xs font-semibold text-brand-orange uppercase tracking-[.25em] mt-1.5 opacity-90">
                                    Autonomous Validation
                                </span>
                            </div>
                        </div>

                        <div className="flex items-center space-x-6">
                            {/* Theme Toggle */}
                            <button
                                onClick={() => setDarkMode(!darkMode)}
                                className="p-2.5 rounded-full text-slate-500hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors focus:outline-none focus:ring-2 focus:ring-brand-blue/20"
                                title={darkMode ? "Switch to Light Mode" : "Switch to Dark Mode"}
                            >
                                <span className="text-xl opacity-80">{darkMode ? '☀️' : '🌙'}</span>
                            </button>

                            {/* Status Indicator */}
                            {pipelineState && (
                                <div className="flex items-center space-x-2 bg-slate-50 dark:bg-slate-800 px-3 py-1.5 rounded-md border border-slate-200 dark:border-slate-700 shadow-sm">
                                    <span className={`w-2 h-2 rounded-full ${pipelineState.status === 'running' ? 'bg-brand-orange animate-pulse' : 'bg-emerald-500'}`}></span>
                                    <span className="text-xs font-semibold uppercase text-slate-600 dark:text-slate-300 tracking-wide">
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
                    <div className="space-y-16 animate-fade-in-up">
                        {/* Branding Hero Section */}
                        <div className="text-center max-w-3xl mx-auto space-y-8 py-4">
                            {/* Updated Hierarchy: Brand Name as Hero */}
                            <div className="space-y-4">
                                <h1 className="text-6xl md:text-8xl font-bold tracking-tight text-slate-900 dark:text-white leading-none">
                                    HAMAL
                                </h1>
                                <p className="text-2xl md:text-3xl font-light text-slate-500 dark:text-slate-400 tracking-wide">
                                    The <span className="font-normal text-brand-orange">Head of the Ram</span>
                                </p>
                            </div>

                            {/* Left-Aligned professional quote block */}
                            <div className="relative bg-white dark:bg-slate-800/50 p-8 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm text-left backdrop-blur-sm">
                                <div className="absolute top-8 left-0 w-1 h-16 bg-brand-orange rounded-r-full"></div>
                                <p className="text-lg text-slate-600 dark:text-slate-300 font-normal leading-relaxed pl-4">
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
