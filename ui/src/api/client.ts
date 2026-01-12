const API_URL = import.meta.env.VITE_API_URL || '';

export const triggerPipeline = async (charterText, projectName) => {
    const response = await fetch(`${API_URL}/api/pipeline/start`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            charter_text: charterText,
            project_name: projectName
        }),
    });

    if (!response.ok) {
        throw new Error('Failed to start pipeline');
    }

    return response.json();
};

export const getPipelineStatus = async (projectName) => {
    const response = await fetch(`${API_URL}/api/pipeline/${projectName}/status`);
    if (!response.ok) {
        throw new Error('Failed to fetch status');
    }
    return response.json();
};

export const getPipelineLogs = async (projectName) => {
    const response = await fetch(`${API_URL}/api/pipeline/${projectName}/artifacts/activity.log`);
    if (!response.ok) {
        if (response.status === 404) return ""; // Logs not created yet
        throw new Error('Failed to fetch logs');
    }
    return response.text();
};

export const getArtifactUrl = (projectName, filename) => {
    return `${API_URL}/api/pipeline/${projectName}/artifacts/${filename}`;
};

export const getArtifactContent = async (projectName, filename) => {
    const response = await fetch(getArtifactUrl(projectName, filename));
    if (!response.ok) {
        throw new Error(`Failed to fetch artifact: ${filename}`);
    }
    return response.text();
};
