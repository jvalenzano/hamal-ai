import React, { useEffect, useRef } from 'react';

const ActivityLog = ({ logs }) => {
    const logEndRef = useRef(null);

    useEffect(() => {
        logEndRef.current?.scrollIntoView({ behavior: "smooth" });
    }, [logs]);

    return (
        <div className="bg-gray-900 dark:bg-black rounded-lg border border-slate-200 dark:border-slate-700 shadow-lg overflow-hidden flex flex-col h-96 font-mono text-sm">
            <div className="bg-slate-100 dark:bg-slate-900 px-4 py-2 border-b border-slate-200 dark:border-slate-800 flex justify-between items-center">
                <span className="text-slate-500 dark:text-slate-400 font-semibold tracking-wider text-xs">TERMINAL_OUTPUT</span>
                <div className="flex space-x-2">
                    <div className="w-3 h-3 rounded-full bg-red-500"></div>
                    <div className="w-3 h-3 rounded-full bg-yellow-500"></div>
                    <div className="w-3 h-3 rounded-full bg-green-500"></div>
                </div>
            </div>
            <div className="p-4 overflow-y-auto flex-1 space-y-1 text-green-400">
                <pre className="whitespace-pre-wrap font-mono text-xs md:text-sm">
                    {logs || "Waiting for pipeline to start..."}
                </pre>
                <div ref={logEndRef} />
            </div>
        </div>
    );
};

export default ActivityLog;
