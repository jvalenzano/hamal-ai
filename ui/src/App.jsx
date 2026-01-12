import { useState, useEffect } from 'react';
import { Compass } from 'lucide-react';
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
            {/* The Neural Constellation System - Interactive Background (z-0) */}
            <div className="fixed inset-0 z-0">
                <ParticlesBackground />
            </div>

            {/* Navigation / Header - PERSISTENT DARK MODE - (z-50) */}
            <nav className="border-b border-white/10 sticky top-0 z-50 bg-slate-900 transition-colors duration-500 backdrop-blur-md supports-[backdrop-filter]:bg-slate-900/90">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="flex items-center justify-between h-16">
                        {/* Logo & Brand */}
                        <div
                            className="flex items-center cursor-pointer group"
                            onClick={resetPipeline}
                        >
                            {/* Logo - Hand-coded Geometric Vector SVG - SCALED UP & DETAILED */}
                            <div className="relative h-8 w-8 text-brand-orange transition-transform transform group-hover:scale-110">
                                <Compass className="w-full h-full drop-shadow-[0_0_8px_rgba(234,88,12,0.5)]" />
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


                        </div>
                    </div>
                </div>
            </nav>
            <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 relative z-10">
                {!pipelineState ? (
                    <div className="animate-fade-in-up">
                        <p className="text-sm text-slate-500 dark:text-slate-400 mb-6 text-center">
                            Initialize your venture validation pipeline
                        </p>
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
