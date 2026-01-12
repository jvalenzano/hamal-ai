import React, { createContext, useContext, useState, useEffect } from 'react';
import { getPipelineStatus, getPipelineLogs } from '../api/client';

const PipelineContext = createContext();

export const usePipeline = () => {
    const context = useContext(PipelineContext);
    if (!context) {
        throw new Error('usePipeline must be used within a PipelineProvider');
    }
    return context;
};

export const PipelineProvider = ({ children }) => {
    const [pipelineState, setPipelineState] = useState(null);
    const [logs, setLogs] = useState("");
    const [projectName, setProjectName] = useState(null);
    const [isPolling, setIsPolling] = useState(false);
    const [error, setError] = useState(null);

    const startPolling = (name) => {
        setProjectName(name);
        setIsPolling(true);
    };

    useEffect(() => {
        let intervalId;

        if (isPolling && projectName) {
            const fetchStatus = async () => {
                try {
                    // Fetch status
                    const statusData = await getPipelineStatus(projectName);
                    setPipelineState(statusData);

                    // Fetch logs (ignore 404s early on)
                    try {
                        const logData = await getPipelineLogs(projectName);
                        setLogs(logData);
                    } catch (e) {
                        // Logs might not exist yet, that's fine
                    }

                    if (statusData.status === 'complete' || statusData.status === 'failed') {
                        setIsPolling(false);
                    }
                } catch (err) {
                    console.error("Polling error:", err);
                    setError(err.message);
                    setIsPolling(false);
                }
            };

            fetchStatus(); // Initial call
            intervalId = setInterval(fetchStatus, 1000); // Poll every 1s
        }

        return () => {
            if (intervalId) clearInterval(intervalId);
        };
    }, [isPolling, projectName]);

    const resetPipeline = () => {
        setPipelineState(null);
        setLogs("");
        setProjectName(null);
        setIsPolling(false);
        setError(null);
    };

    const value = {
        pipelineState,
        logs,
        projectName,
        isPolling,
        error,
        startPolling,
        resetPipeline
    };

    return (
        <PipelineContext.Provider value={value}>
            {children}
        </PipelineContext.Provider>
    );
};
