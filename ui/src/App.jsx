import React from 'react';
import { PipelineProvider, usePipeline } from './context/PipelineContext';
import InputForm from './components/InputForm';
import PipelineProgress from './components/PipelineProgress';

const HamalApp = () => {
    const { pipelineState, resetPipeline } = usePipeline();

    return (
        <div className="min-h-screen bg-slate-950 text-slate-100 selection:bg-orange-500/30">
            {/* Navigation / Header */}
            <nav className="bg-slate-900 border-b border-slate-800 sticky top-0 z-50">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="flex items-center justify-between h-20">
                        {/* Logo & Brand */}
                        <div
                            className="flex items-center space-x-4 cursor-pointer group"
                            onClick={resetPipeline}
                        >
                            <img
                                src="/logo.png"
                                alt="Hamal Logo"
                                className="h-12 w-12 transition-transform transform group-hover:scale-110 drop-shadow-[0_0_10px_rgba(255,69,0,0.5)]"
                            />
                            <div>
                                <h1 className="text-2xl font-bold tracking-wider text-white">
                                    HAMAL
                                </h1>
                                <span className="text-[10px] uppercase tracking-[0.2em] text-[#FF4500]">
                                    Autonomous Validation
                                </span>
                            </div>
                        </div>

                        {/* Status Indicator */}
                        {pipelineState && (
                            <div className="flex items-center space-x-2 bg-slate-800 px-3 py-1 rounded-full border border-slate-700">
                                <span className={`w-2 h-2 rounded-full ${pipelineState.status === 'running' ? 'bg-[#FF4500] animate-pulse' : 'bg-green-500'}`}></span>
                                <span className="text-xs font-mono uppercase text-slate-300">
                                    {pipelineState.status}
                                </span>
                            </div>
                        )}
                    </div>
                </div>
            </nav>

            {/* Main Content */}
            <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
                {!pipelineState ? (
                    <div className="space-y-12 animate-fade-in-up">
                        {/* Branding Hero Section */}
                        <div className="text-center max-w-3xl mx-auto space-y-6">
                            <h2 className="text-4xl md:text-5xl font-extrabold text-white">
                                The <span className="text-transparent bg-clip-text bg-gradient-to-r from-[#FF4500] to-orange-400">Head of the Ram</span>
                            </h2>
                            <div className="relative">
                                <span className="absolute -top-4 -left-4 text-6xl text-slate-800 font-serif opacity-50">"</span>
                                <p className="text-xl text-slate-300 font-light italic leading-relaxed px-8">
                                    Hamal (Alpha Arietis) is the brightest star in Aries. Just as this star historically guided navigators,
                                    this intelligence layer serves as the <strong className="text-white font-normal">brain of the constellation</strong>—guiding ideas from the chaos of conception to the clarity of execution.
                                </p>
                                <span className="absolute -bottom-8 -right-4 text-6xl text-slate-800 font-serif opacity-50">"</span>
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
