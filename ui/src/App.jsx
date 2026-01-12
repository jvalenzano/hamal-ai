import { useState, useEffect } from 'react';
import { PipelineProvider, usePipeline } from './context/PipelineContext';
import InputForm from './components/InputForm';
import PipelineProgress from './components/PipelineProgress';
import ActivityLog from './components/ActivityLog';
import OutputViewer from './components/OutputViewer';
import ParticlesBackground from './components/ParticlesBackground';

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
        <div className="min-h-screen relative transition-colors duration-500 selection:bg-brand-orange/30 dark:text-slate-100 text-slate-900 bg-slate-50 dark:bg-slate-950">
            {/* The Neural Constellation System */}
            <div className="fixed inset-0 pointer-events-none z-0">
                <ParticlesBackground />
            </div>

            {/* Navigation / Header - PERSISTENT DARK MODE */}
            <nav className="border-b border-white/10 sticky top-0 z-50 bg-slate-900 transition-colors duration-500 backdrop-blur-md supports-[backdrop-filter]:bg-slate-900/90">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="flex items-center justify-between h-24">
                        {/* Logo & Brand */}
                        <div
                            className="flex items-center space-x-5 cursor-pointer group"
                            onClick={resetPipeline}
                        >
                            {/* Logo - Hand-coded Geometric Vector SVG - SCALED UP & DETAILED */}
                            <div className="relative h-20 w-20 transition-transform transform group-hover:scale-105">
                                <svg
                                    viewBox="0 0 100 100"
                                    fill="none"
                                    xmlns="http://www.w3.org/2000/svg"
                                    className="w-full h-full text-white drop-shadow-[0_0_12px_rgba(255,255,255,0.4)]"
                                >
                                    {/* Central Star - The "Alpha Arietis" (Slightly larger, glowing) */}
                                    <path
                                        d="M50 15 L56 32 L74 38 L56 44 L50 62 L44 44 L26 38 L44 32 L50 15 Z"
                                        fill="#EA580C"
                                        stroke="white"
                                        strokeWidth="1.5"
                                        strokeLinejoin="round"
                                        className="animate-pulse-slow"
                                    />

                                    {/* Complex Geometric Ram Construction */}
                                    {/* Brow / Nose Bridge - Stronger, Angular */}
                                    <path
                                        d="M38 42 L38 65 L50 78 L62 65 L62 42"
                                        stroke="white"
                                        strokeWidth="3"
                                        strokeLinecap="round"
                                        strokeLinejoin="round"
                                    />

                                    {/* Eyes - Aggressive Slit */}
                                    <path d="M38 52 L30 48" stroke="white" strokeWidth="3" strokeLinecap="round" />
                                    <path d="M62 52 L70 48" stroke="white" strokeWidth="3" strokeLinecap="round" />

                                    {/* Powerful Spiral Horns - The "Awesome" Element */}
                                    {/* Left Horn */}
                                    <path
                                        d="M38 42 C 20 42, 10 30, 10 50 C 10 70, 25 80, 35 70 C 40 65, 30 55, 25 60"
                                        stroke="white"
                                        strokeWidth="3"
                                        strokeLinecap="round"
                                        strokeLinejoin="round"
                                    />

                                    {/* Right Horn */}
                                    <path
                                        d="M62 42 C 80 42, 90 30, 90 50 C 90 70, 75 80, 65 70 C 60 65, 70 55, 75 60"
                                        stroke="white"
                                        strokeWidth="3"
                                        strokeLinecap="round"
                                        strokeLinejoin="round"
                                    />
                                </svg>
                            </div>

                            <div className="flex flex-col justify-center">
                                <h1 className="text-3xl font-bold tracking-tight font-sans text-white leading-none">
                                    HAMAL
                                </h1>
                                <span className="text-xs font-semibold text-brand-orange uppercase tracking-[.25em] mt-1.5 opacity-90">
                                    Autonomous Validation
                                </span>
                            </div>
                        </div>

                        <div className="flex items-center space-x-6">
                            {/* Theme Toggle - Always white/light on dark header */}
                            <button
                                onClick={() => setDarkMode(!darkMode)}
                                className="p-2.5 rounded-full text-slate-300 hover:text-white hover:bg-white/10 transition-colors focus:outline-none focus:ring-2 focus:ring-brand-blue/50"
                                title={darkMode ? "Switch to Light Mode" : "Switch to Dark Mode"}
                            >
                                <span className="text-xl opacity-90">{darkMode ? '☀️' : '🌙'}</span>
                            </button>

                            {/* Status Indicator */}
                            {pipelineState && (
                                <div className="flex items-center space-x-2 bg-slate-800 px-3 py-1.5 rounded-md border border-slate-700 shadow-sm">
                                    <span className={`w - 2 h - 2 rounded - full ${pipelineState.status === 'running' ? 'bg-brand-orange animate-pulse' : 'bg-emerald-500'} `}></span>
                                    <span className="text-xs font-semibold uppercase text-slate-300 tracking-wide">
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
