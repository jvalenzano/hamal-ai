import React, { useEffect, useRef, useState } from 'react';
import { Pause, Play, ArrowDown } from 'lucide-react';

const ActivityLog = ({ logs }) => {
    const containerRef = useRef(null);
    const [autoScroll, setAutoScroll] = useState(true);

    // Auto-scroll logic safely contained within the component
    useEffect(() => {
        if (autoScroll && containerRef.current) {
            const { scrollHeight, clientHeight } = containerRef.current;
            // Only scroll if there is content to scroll
            if (scrollHeight > clientHeight) {
                containerRef.current.scrollTo({
                    top: scrollHeight,
                    behavior: 'smooth'
                });
            }
        }
    }, [logs, autoScroll]);

    // Detect user manual scroll to pause auto-scroll
    const handleScroll = () => {
        if (!containerRef.current) return;
        const { scrollTop, scrollHeight, clientHeight } = containerRef.current;
        const isAtBottom = Math.abs(scrollHeight - clientHeight - scrollTop) < 50;

        // If user scrolls up, disable auto-scroll. If at bottom, enable it.
        if (isAtBottom && !autoScroll) {
            setAutoScroll(true);
        } else if (!isAtBottom && autoScroll) {
            setAutoScroll(false);
        }
    };

    return (
        <div className="bg-gray-900 dark:bg-black rounded-lg border border-slate-200 dark:border-slate-700 shadow-lg overflow-hidden flex flex-col h-96 font-mono text-sm relative group">
            <div className="bg-slate-100 dark:bg-slate-900 px-4 py-2 border-b border-slate-200 dark:border-slate-800 flex justify-between items-center z-10">
                <span className="text-slate-500 dark:text-slate-400 font-semibold tracking-wider text-xs flex items-center gap-2">
                    <span className={`w-2 h-2 rounded-full ${autoScroll ? 'bg-green-500 animate-pulse' : 'bg-yellow-500'}`}></span>
                </span>
                <div className="flex space-x-2">
                    <div className="w-3 h-3 rounded-full bg-red-500 opacity-20"></div>
                    <div className="w-3 h-3 rounded-full bg-yellow-500 opacity-20"></div>
                    <div className="w-3 h-3 rounded-full bg-green-500 opacity-20"></div>
                </div>
            </div>

            <div
                ref={containerRef}
                onScroll={handleScroll}
                className="p-4 overflow-y-auto flex-1 space-y-1 text-green-400 scroll-smooth custom-scrollbar"
            >
                <div className="whitespace-pre-wrap font-mono text-xs md:text-sm leading-relaxed">
                    {logs || "Waiting for pipeline to start..."}
                    {/* Blinking cursor at the end */}
                    <span className="inline-block w-2.5 h-4 bg-green-500 align-middle ml-1 animate-pulse"></span>
                </div>
            </div>

            {/* Resume Auto-scroll Button */}
            {!autoScroll && (
                <button
                    onClick={() => {
                        setAutoScroll(true);
                        // Force immediate scroll
                        if (containerRef.current) {
                            containerRef.current.scrollTop = containerRef.current.scrollHeight;
                        }
                    }}
                    className="absolute bottom-4 right-4 bg-slate-800 text-white p-2 rounded-full shadow-lg border border-slate-600 hover:bg-slate-700 transition-all opacity-80 hover:opacity-100 animate-bounce"
                    title="Resume Auto-scroll"
                >
                    <ArrowDown className="w-4 h-4" />
                </button>
            )}
        </div>
    );
};

export default ActivityLog;
