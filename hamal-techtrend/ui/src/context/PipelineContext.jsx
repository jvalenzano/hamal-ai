import React, { createContext, useContext, useState, useEffect, useCallback } from 'react';
import { apiClient } from '../api/client';

const PipelineContext = createContext(null);

export const PipelineProvider = ({ children }) => {
    const [pipelineState, setPipelineState] = useState(null);
    const [logs, setLogs] = useState('');
    const [projectName, setProjectName] = useState(null);
    const [isPolling, setIsPolling] = useState(false);
    const [error, setError] = useState(null);

    const startPipeline = useCallback(async (charterText, optionalProjectName) => {
        try {
            setError(null);
            setLogs('');
            setPipelineState(null); // Reset state on new run
            const result = await apiClient.triggerPipeline(charterText, optionalProjectName);
            setProjectName(result.project_name);
            setIsPolling(true);
            return result.project_name;
        } catch (err) {
            setError(err.message);
            setIsPolling(false);
            throw err;
        }
    }, []);

    useEffect(() => {
        let intervalId;

        if (isPolling && projectName) {
            const poll = async () => {
                try {
                    const [status, logText] = await Promise.all([
                        apiClient.getPipelineStatus(projectName),
                        apiClient.getPipelineLogs(projectName)
                    ]);

                    if (logText) setLogs(logText);

                    if (status) {
                        setPipelineState(status);

                        if (status.status === 'complete' || status.status === 'failed') {
                            setIsPolling(false);
                        }
                    }
                } catch (err) {
                    console.error("Polling error:", err);
                }
            };

            poll();
            intervalId = setInterval(poll, 1000);
        }

        return () => {
            if (intervalId) clearInterval(intervalId);
        };
    }, [isPolling, projectName]);

    const value = {
        pipelineState,
        projectName,
        startPipeline,
        isPolling,
        logs,
        error,
        getArtifactUrl: (p, f) => apiClient.getArtifactUrl(p, f),
        getArtifactContent: (p, f) => apiClient.getArtifactContent(p, f)
    };

    return (
        <PipelineContext.Provider value={value}>
            {children}
        </PipelineContext.Provider>
    );
};

export const usePipeline = () => {
    const context = useContext(PipelineContext);
    if (!context) {
        throw new Error('usePipeline must be used within a PipelineProvider');
    }
    return context;
};
