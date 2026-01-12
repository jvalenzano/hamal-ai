import React, { useEffect, useRef } from 'react';
import { Terminal } from 'lucide-react';

const ActivityLog = ({ logs }) => {
    const logEndRef = useRef(null);

    // Auto-scroll to bottom of logs
    useEffect(() => {
        logEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }, [logs]);

    return (
        <div className="bg-gray-900 rounded-lg shadow-lg border border-gray-700 overflow-hidden font-mono text-sm">
            <div className="bg-gray-800 px-4 py-2 flex items-center border-b border-gray-700">
                <Terminal className="text-green-400 w-4 h-4 mr-2" />
                <span className="text-gray-300 text-xs font-semibold uppercase tracking-wider">Live Activity</span>
            </div>
            <div className="p-4 h-64 overflow-y-auto whitespace-pre-wrap text-gray-300">
                {logs ? logs : <span className="text-gray-500 italic">Waiting for activity...</span>}
                <div ref={logEndRef} />
            </div>
        </div>
    );
};

export default ActivityLog;
