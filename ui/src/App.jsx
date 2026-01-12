import React from 'react';
import { PipelineProvider, usePipeline } from './context/PipelineContext';
import InputForm from './components/InputForm';
import PipelineProgress from './components/PipelineProgress';

const HamalApp = () => {
    const { pipelineState, resetPipeline } = usePipeline();

    return (
        <div className="min-h-screen relative text-slate-100 selection:bg-brand-orange/30">
            <div className="stars"></div>


            {/* Main Content */}
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
